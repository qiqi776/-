"""验证项目组合生成脚本能从组件索引中生成技术栈决策草案。"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
SCRIPT = ROOT / "tools" / "assemble_stack.py"


def load_assemble_tool():
    # 动态加载组合生成脚本，便于直接测试选择逻辑。
    tools_path = str(TOOLS_DIR)
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    spec = importlib.util.spec_from_file_location("assemble_stack", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AssembleStackTests(unittest.TestCase):
    def setUp(self):
        # 构造最小组件索引，覆盖同一分类下主组件和备选组件排序。
        self.components = [
            {
                "name": "FastAPI",
                "category": "backend",
                "github": "https://github.com/fastapi/fastapi",
                "module": "后端 / API",
                "license": "MIT",
                "integration_cost": "低",
                "score": "5/5",
                "notes": "适合 AI 项目。",
            },
            {
                "name": "NestJS",
                "category": "backend",
                "github": "https://github.com/nestjs/nest",
                "module": "后端 / API",
                "license": "MIT",
                "integration_cost": "中",
                "score": "4/5",
                "notes": "适合 TypeScript 团队。",
            },
            {
                "name": "Keycloak",
                "category": "auth",
                "github": "https://github.com/keycloak/keycloak",
                "module": "认证 / IAM",
                "license": "Apache-2.0",
                "integration_cost": "高",
                "score": "4/5",
                "notes": "适合企业身份。",
            },
        ]

    def test_select_components_returns_primary_and_fallback(self):
        # 验证同一模块下按评分和接入成本选择主组件与备选组件。
        assemble_tool = load_assemble_tool()

        decision = assemble_tool.select_for_category(self.components, "backend")

        self.assertEqual(decision["primary"]["name"], "FastAPI")
        self.assertEqual(decision["fallback"]["name"], "NestJS")

    def test_build_stack_decisions_handles_missing_category(self):
        # 验证缺失模块会保留空决策，方便人工后续补齐。
        assemble_tool = load_assemble_tool()

        decisions = assemble_tool.build_stack_decisions(self.components, ["backend", "payment"])

        self.assertEqual(decisions[0]["category"], "backend")
        self.assertIsNone(decisions[1]["primary"])
        self.assertEqual(decisions[1]["risk"], "目录中暂未收录该模块组件。")

    def test_resolve_modules_accepts_named_preset(self):
        # 验证快速技术栈草案也能复用常见项目蓝图，避免和工作表生成器入口不一致。
        assemble_tool = load_assemble_tool()

        modules = assemble_tool.resolve_modules("", "internal-admin")

        self.assertIn("frontend", modules)
        self.assertIn("internal-tools", modules)
        self.assertIn("backend", modules)
        self.assertIn("observability", modules)

    def test_cli_lists_available_presets(self):
        # 验证命令行可以先查看预设，方便用户决定使用蓝图还是手写模块。
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--list-presets",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("saas-starter", result.stdout)
        self.assertIn("ai-rag-app", result.stdout)
        self.assertIn("internal-admin", result.stdout)

    def test_cli_outputs_stack_decision_table(self):
        # 验证命令行能读取索引并输出可复制的技术栈决策表。
        tmp_index = ROOT / "tmp" / "assemble-test-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--modules",
                "backend,auth",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("| 模块 | 主组件 | 许可证 | 接入成本 | 备选组件 | 选择理由 | 主要风险 |", result.stdout)
        self.assertIn("FastAPI", result.stdout)
        self.assertIn("| backend | FastAPI | MIT | 低 | NestJS |", result.stdout)
        self.assertIn("Keycloak", result.stdout)

    def test_cli_outputs_machine_readable_stack_json(self):
        # 验证命令行可以输出机器可读技术栈清单，方便后续脚手架或模板继续消费。
        tmp_index = ROOT / "tmp" / "assemble-json-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--modules",
                "backend,auth",
                "--format",
                "json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["module_count"], 2)
        self.assertEqual(payload["modules"][0]["category"], "backend")
        self.assertEqual(payload["modules"][0]["primary"]["name"], "FastAPI")
        self.assertEqual(payload["modules"][0]["primary"]["license"], "MIT")
        self.assertEqual(payload["modules"][0]["primary"]["integration_cost"], "低")
        self.assertEqual(payload["modules"][0]["fallback"]["name"], "NestJS")
        self.assertEqual(payload["modules"][1]["category"], "auth")
        self.assertEqual(payload["modules"][1]["primary"]["name"], "Keycloak")
        self.assertIn("适合企业身份", payload["modules"][1]["reason"])

    def test_cli_writes_stack_plan_to_output_file(self):
        # 验证技术栈清单可以直接写入文件，便于复制到新项目仓库或交给后续自动化。
        tmp_dir = ROOT / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_index = tmp_dir / "assemble-output-index.json"
        tmp_output = tmp_dir / "stack-plan.json"
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )
        if tmp_output.exists():
            tmp_output.unlink()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--modules",
                "backend,auth",
                "--format",
                "json",
                "--output",
                str(tmp_output),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertTrue(tmp_output.exists())
        payload = json.loads(tmp_output.read_text(encoding="utf-8"))
        self.assertEqual(payload["modules"][0]["primary"]["name"], "FastAPI")
        self.assertIn("已生成技术栈清单", result.stdout)
        self.assertNotIn("\"modules\"", result.stdout)

    def test_cli_outputs_project_component_manifest(self):
        # 验证组合生成器可以输出项目组件清单，便于新项目仓库追踪每个模块的落地组件。
        tmp_index = ROOT / "tmp" / "assemble-manifest-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--modules",
                "backend,auth",
                "--format",
                "manifest",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("# 项目组件清单", result.stdout)
        self.assertIn(
            "| 能力 | 主组件 | GitHub | 官网 | 许可证 | 接入成本 | 备选组件 | 首个动作 | 待确认事项 |",
            result.stdout,
        )
        self.assertIn(
            "| 后端 / API | FastAPI | https://github.com/fastapi/fastapi |  | MIT | 低 | NestJS | 先阅读快速开始并跑通最小样例 | 按项目数据边界人工确认 |",
            result.stdout,
        )
        self.assertIn(
            "| 认证 / IAM | Keycloak | https://github.com/keycloak/keycloak |  | Apache-2.0 | 高 |  | 先确认许可证和部署方式，再跑通最小样例 | 接入成本高；适合企业身份。 |",
            result.stdout,
        )

    def test_cli_outputs_stack_decision_table_from_preset(self):
        # 验证命令行可以通过项目预设直接生成技术栈草案。
        tmp_index = ROOT / "tmp" / "assemble-preset-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--preset",
                "internal-admin",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("FastAPI", result.stdout)
        self.assertIn("Keycloak", result.stdout)
        self.assertIn("| observability |", result.stdout)

    def test_cli_accepts_chinese_project_preset_name(self):
        # 验证用户可以直接输入中文项目类型，不必记住英文预设 slug。
        tmp_index = ROOT / "tmp" / "assemble-chinese-preset-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

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
        self.assertIn("FastAPI", result.stdout)
        self.assertIn("Keycloak", result.stdout)
        self.assertIn("| observability |", result.stdout)

    def test_cli_reports_unknown_preset_name(self):
        # 验证输错项目预设时给出明确错误，而不是误报为没有传入参数。
        tmp_index = ROOT / "tmp" / "assemble-unknown-preset-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--preset",
                "未知项目",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 2)
        self.assertIn("未知项目预设", result.stderr)


if __name__ == "__main__":
    unittest.main()
