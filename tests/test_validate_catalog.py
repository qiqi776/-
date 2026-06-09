"""验证组件目录校验脚本的解析、报错和索引生成能力。"""

from contextlib import contextmanager
import importlib.util
import json
import shutil
import subprocess
import sys
from uuid import uuid4
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
SCRIPT = ROOT / "tools" / "validate_catalog.py"
TEST_TMP = ROOT / "tmp" / "tests"


def load_validator():
    # 动态加载校验脚本，方便测试直接调用脚本里的解析函数。
    tools_path = str(TOOLS_DIR)
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    spec = importlib.util.spec_from_file_location("validate_catalog", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@contextmanager
def temporary_workspace():
    # Windows 沙箱中 tempfile 创建的目录可能无法继续写入子目录；这里手动创建可写目录。
    TEST_TMP.mkdir(parents=True, exist_ok=True)
    root = TEST_TMP / f"workspace-{uuid4().hex}"
    root.mkdir()
    try:
        yield root
    finally:
        shutil.rmtree(root, ignore_errors=True)


class CatalogValidationTests(unittest.TestCase):
    def test_parse_catalog_entries_extracts_component_fields(self):
        # 验证 Markdown 条目能被解析成结构化组件数据。
        validator = load_validator()
        with temporary_workspace() as tmp:
            root = Path(tmp)
            catalog = root / "catalog"
            catalog.mkdir()
            (catalog / "backend.md").write_text(
                """# Backend Components

## FastAPI

- GitHub: https://github.com/fastapi/fastapi
- 官网: https://fastapi.tiangolo.com
- 模块: 后端 / API
- 技术栈: Python, Starlette, Pydantic
- 许可证: MIT
- 适合: Python API。
- 不适合: 需要完整全栈框架。
- 接入成本: 低
- 替代方案: Django REST Framework, Flask
- 评分: 5/5
- 备注: Python 服务的好默认选择。
""",
                encoding="utf-8",
            )

            entries = validator.parse_catalog(root)

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["name"], "FastAPI")
        self.assertEqual(entries[0]["category"], "backend")
        self.assertEqual(entries[0]["fields"]["许可证"], "MIT")

    def test_validate_catalog_reports_missing_required_fields(self):
        # 验证缺少必填字段时能给出包含组件名和字段名的错误。
        validator = load_validator()
        with temporary_workspace() as tmp:
            root = Path(tmp)
            catalog = root / "catalog"
            catalog.mkdir()
            (catalog / "ai.md").write_text(
                """# AI Components

## Example AI

- GitHub: https://github.com/example/ai
- 模块: AI
- 许可证: MIT
""",
                encoding="utf-8",
            )

            errors = validator.validate_repository(root)

        self.assertTrue(
            any("Example AI" in error and "技术栈" in error for error in errors),
            errors,
        )

    def test_validate_repository_reports_unknown_preset_category(self):
        # 验证项目预设引用了不存在的分类时会报错，避免拼装蓝图在 GitHub 上腐化。
        validator = load_validator()
        with temporary_workspace() as tmp:
            root = Path(tmp)
            catalog = root / "catalog"
            catalog.mkdir()
            (catalog / "backend.md").write_text(
                """# Backend Components

## FastAPI

- GitHub: https://github.com/fastapi/fastapi
- 官网: https://fastapi.tiangolo.com
- 模块: 后端 / API
- 技术栈: Python, Starlette, Pydantic
- 许可证: MIT
- 适合: Python API。
- 不适合: 需要完整全栈框架。
- 接入成本: 低
- 替代方案: Django REST Framework, Flask
- 评分: 5/5
- 备注: Python 服务的好默认选择。
""",
                encoding="utf-8",
            )

            errors = validator.validate_repository(
                root,
                stack_presets={"broken-stack": ["backend", "missing-module"]},
            )

        self.assertTrue(
            any("broken-stack" in error and "missing-module" in error for error in errors),
            errors,
        )

    def test_validate_repository_reports_missing_stack_blueprint_file(self):
        # 验证脚本内置预设必须有同名 stacks 文档，保证机器蓝图和人工说明同步。
        validator = load_validator()
        with temporary_workspace() as tmp:
            root = Path(tmp)
            catalog = root / "catalog"
            catalog.mkdir()
            (catalog / "backend.md").write_text(
                """# Backend Components

## FastAPI

- GitHub: https://github.com/fastapi/fastapi
- 官网: https://fastapi.tiangolo.com
- 模块: 后端 / API
- 技术栈: Python, Starlette, Pydantic
- 许可证: MIT
- 适合: Python API。
- 不适合: 需要完整全栈框架。
- 接入成本: 低
- 替代方案: Django REST Framework, Flask
- 评分: 5/5
- 备注: Python 服务的好默认选择。
""",
                encoding="utf-8",
            )

            errors = validator.validate_repository(root, stack_presets={"broken-stack": ["backend"]})

        self.assertTrue(
            any("broken-stack" in error and "stacks/broken-stack.md" in error for error in errors),
            errors,
        )

    def test_write_index_outputs_all_components_as_json(self):
        # 验证脚本能生成机器可读的 catalog/index.json。
        validator = load_validator()
        with temporary_workspace() as tmp:
            root = Path(tmp)
            catalog = root / "catalog"
            catalog.mkdir()
            (catalog / "auth.md").write_text(
                """# Auth Components

## Auth.js

- GitHub: https://github.com/nextauthjs/next-auth
- 官网: https://authjs.dev
- 模块: 认证 / Web
- 技术栈: TypeScript, JavaScript
- 许可证: ISC
- 适合: Web OAuth。
- 不适合: 需要企业 IAM。
- 接入成本: 低
- 替代方案: Supabase Auth, Keycloak
- 评分: 4/5
- 备注: 好用的 Web 认证选项。
""",
                encoding="utf-8",
            )

            output = root / "catalog" / "index.json"
            validator.write_index(root, output)
            data = json.loads(output.read_text(encoding="utf-8"))

        self.assertEqual(data["component_count"], 1)
        self.assertEqual(data["components"][0]["name"], "Auth.js")
        self.assertEqual(data["components"][0]["github"], "https://github.com/nextauthjs/next-auth")

    def test_cli_fails_when_catalog_has_errors(self):
        # 验证命令行入口在 catalog 有错误时返回非零退出码。
        with temporary_workspace() as tmp:
            root = Path(tmp)
            catalog = root / "catalog"
            catalog.mkdir()
            (catalog / "frontend.md").write_text(
                """# Frontend Components

## Broken UI

- GitHub: not-a-url
- 模块: 前端
- 技术栈: TypeScript
- 许可证: MIT
- 适合: 测试。
- 不适合: URL 必须有效的场景。
- 接入成本: 低
- 替代方案: Other UI
- 评分: 4/5
- 备注: 无效 URL 应该失败。
""",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(root)],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Broken UI", result.stdout)


if __name__ == "__main__":
    unittest.main()
