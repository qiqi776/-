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
                "integration_cost": "低",
                "score": "5/5",
                "notes": "适合 AI 项目。",
            },
            {
                "name": "NestJS",
                "category": "backend",
                "github": "https://github.com/nestjs/nest",
                "module": "后端 / API",
                "integration_cost": "中",
                "score": "4/5",
                "notes": "适合 TypeScript 团队。",
            },
            {
                "name": "Keycloak",
                "category": "auth",
                "github": "https://github.com/keycloak/keycloak",
                "module": "认证 / IAM",
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
        self.assertIn("| 模块 | 主组件 | 备选组件 | 选择理由 | 主要风险 |", result.stdout)
        self.assertIn("FastAPI", result.stdout)
        self.assertIn("Keycloak", result.stdout)

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


if __name__ == "__main__":
    unittest.main()
