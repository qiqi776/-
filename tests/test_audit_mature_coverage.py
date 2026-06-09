"""验证成熟开源组件覆盖审计能发现项目拼装缺口。"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
SCRIPT = ROOT / "tools" / "audit_mature_coverage.py"


def load_audit_tool():
    # 动态加载审计脚本，便于直接测试分类覆盖统计函数。
    tools_path = str(TOOLS_DIR)
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    spec = importlib.util.spec_from_file_location("audit_mature_coverage", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class MatureCoverageAuditTests(unittest.TestCase):
    def setUp(self):
        # 构造最小组件索引：backend 有 2 个成熟开源候选，auth 只有低分或商业许可证候选。
        self.index = {
            "component_count": 5,
            "components": [
                {
                    "name": "FastAPI",
                    "category": "backend",
                    "github": "https://github.com/fastapi/fastapi",
                    "license": "MIT",
                    "integration_cost": "低",
                    "score": "5/5",
                },
                {
                    "name": "NestJS",
                    "category": "backend",
                    "github": "https://github.com/nestjs/nest",
                    "license": "MIT",
                    "integration_cost": "中",
                    "score": "4/5",
                },
                {
                    "name": "PrototypeAuth",
                    "category": "auth",
                    "github": "https://github.com/example/prototype-auth",
                    "license": "MIT",
                    "integration_cost": "低",
                    "score": "2/5",
                },
                {
                    "name": "ClosedAuth",
                    "category": "auth",
                    "github": "https://github.com/example/closed-auth",
                    "license": "商业许可证",
                    "integration_cost": "低",
                    "score": "5/5",
                },
                {
                    "name": "NoRepoBI",
                    "category": "business-intelligence",
                    "github": "",
                    "license": "Apache-2.0",
                    "integration_cost": "中",
                    "score": "4/5",
                },
            ],
        }

    def test_audit_categories_counts_mature_candidates_and_missing_modules(self):
        # 验证审计结果会统计每个模块的成熟开源候选数量，并标出缺口。
        audit_tool = load_audit_tool()

        rows = audit_tool.audit_categories(self.index["components"], ["backend", "auth", "database"])

        self.assertEqual(rows[0]["category"], "backend")
        self.assertEqual(rows[0]["mature_count"], 2)
        self.assertEqual(rows[0]["examples"], ["FastAPI", "NestJS"])
        self.assertEqual(rows[0]["status"], "通过")
        self.assertEqual(rows[1]["category"], "auth")
        self.assertEqual(rows[1]["mature_count"], 0)
        self.assertEqual(rows[1]["status"], "缺口")
        self.assertEqual(rows[2]["category"], "database")
        self.assertEqual(rows[2]["total_count"], 0)
        self.assertEqual(rows[2]["status"], "缺口")

    def test_cli_reports_missing_coverage_without_failing_by_default(self):
        # 验证命令行默认只报告缺口，方便人工先审计目录而不打断日常查看。
        tmp_index = ROOT / "tmp" / "mature-coverage-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(json.dumps(self.index, ensure_ascii=False), encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--modules",
                "backend,auth,database",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("| backend | 2 | 2 | 通过 | FastAPI, NestJS |", result.stdout)
        self.assertIn("| auth | 2 | 0 | 缺口 | - |", result.stdout)
        self.assertIn("成熟开源覆盖缺口: auth, database", result.stdout)

    def test_cli_can_fail_when_required_modules_lack_mature_candidates(self):
        # 验证 CI 或发布前检查可以通过 --fail-on-missing 阻断成熟开源覆盖不足的项目蓝图。
        tmp_index = ROOT / "tmp" / "mature-coverage-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(json.dumps(self.index, ensure_ascii=False), encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--modules",
                "backend,auth",
                "--fail-on-missing",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("成熟开源覆盖缺口: auth", result.stdout)

    def test_cli_accepts_project_preset_for_coverage_audit(self):
        # 验证审计命令可以直接复用项目预设，和拼装生成器保持相同入口。
        tmp_index = ROOT / "tmp" / "mature-coverage-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(json.dumps(self.index, ensure_ascii=False), encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--preset",
                "内部管理后台",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("| 分类 | 组件总数 | 成熟开源数 | 状态 | 示例 |", result.stdout)
        self.assertIn("frontend", result.stdout)


if __name__ == "__main__":
    unittest.main()
