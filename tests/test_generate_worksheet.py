"""验证项目拼装工作表生成脚本能把模块选择直接落成文档。"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
SCRIPT = ROOT / "tools" / "generate_worksheet.py"


def load_generate_tool():
    # 动态加载工作表生成脚本，便于直接测试格式化逻辑。
    tools_path = str(TOOLS_DIR)
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    spec = importlib.util.spec_from_file_location("generate_worksheet", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GenerateWorksheetTests(unittest.TestCase):
    def setUp(self):
        # 构造最小组件索引，覆盖主组件、备选组件和许可证风险三类输出。
        self.components = [
            {
                "name": "FastAPI",
                "category": "backend",
                "module": "后端 / API",
                "license": "MIT",
                "integration_cost": "低",
                "score": "5/5",
                "notes": "适合 AI 项目。",
                "avoid_when": "需要完整全栈框架。",
            },
            {
                "name": "Django",
                "category": "backend",
                "module": "后端 / 全栈框架",
                "license": "BSD-3-Clause",
                "integration_cost": "中",
                "score": "4/5",
                "notes": "适合完整后台。",
                "avoid_when": "只需要轻量 API。",
            },
            {
                "name": "Grafana",
                "category": "observability",
                "module": "监控 / 指标 / 仪表盘",
                "license": "AGPL-3.0",
                "integration_cost": "中",
                "score": "4/5",
                "notes": "适合仪表盘。",
                "avoid_when": "团队不能接受 AGPL 义务。",
            },
        ]

    def test_build_worksheet_fills_selected_modules(self):
        # 验证选中的模块会被标记为需要，并填入主组件、备选组件和风险。
        generate_tool = load_generate_tool()

        worksheet = generate_tool.build_worksheet(self.components, ["backend", "observability"], "SaaS 示例")

        self.assertIn("- 项目名称: SaaS 示例", worksheet)
        self.assertIn("| 后端 / API | 是 | FastAPI | Django | 适合 AI 项目。 | 需要完整全栈框架。 |", worksheet)
        self.assertIn("| 监控 / 指标 / 仪表盘 | 是 | Grafana |  | 适合仪表盘。 | 团队不能接受 AGPL 义务。 |", worksheet)
        self.assertIn("| Grafana | AGPL-3.0 | 待确认 | 许可证需要重点审查", worksheet)

    def test_validation_table_orders_high_risk_integrations_first(self):
        # 验证优先验证表会把许可证或高接入成本风险更高的模块排在前面。
        generate_tool = load_generate_tool()
        decisions = [
            generate_tool.select_for_category(self.components, "backend"),
            generate_tool.select_for_category(self.components, "observability"),
        ]

        validation_table = generate_tool.format_validation_table(decisions)

        self.assertLess(validation_table.index("Grafana"), validation_table.index("FastAPI"))

    def test_resolve_modules_accepts_named_preset(self):
        # 验证常见项目蓝图可以直接展开成目录分类，减少手写模块名的成本。
        generate_tool = load_generate_tool()

        modules = generate_tool.resolve_modules("", "saas-starter")

        self.assertIn("frontend", modules)
        self.assertIn("backend", modules)
        self.assertIn("billing-invoicing", modules)
        self.assertIn("observability", modules)

    def test_cli_lists_available_presets(self):
        # 验证命令行可以直接列出预设名称，方便用户在生成工作表前发现可用蓝图。
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

    def test_cli_writes_worksheet_file(self):
        # 验证命令行能读取索引并写出可复制到项目仓库的工作表文件。
        tmp_dir = ROOT / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_index = tmp_dir / "generate-worksheet-index.json"
        tmp_output = tmp_dir / "stack-selection.md"
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
                "--preset",
                "internal-admin",
                "--project-name",
                "SaaS 示例",
                "--output",
                str(tmp_output),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertTrue(tmp_output.exists())
        output_text = tmp_output.read_text(encoding="utf-8")
        self.assertIn("# 项目拼装工作表", output_text)
        self.assertIn("SaaS 示例", output_text)
        self.assertIn("FastAPI", output_text)

    def test_cli_accepts_chinese_project_preset_name(self):
        # 验证工作表生成器也能直接接受中文项目类型，保持两个拼装入口体验一致。
        tmp_dir = ROOT / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_index = tmp_dir / "generate-worksheet-chinese-preset-index.json"
        tmp_output = tmp_dir / "stack-selection-chinese-preset.md"
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
                "--preset",
                "内部管理后台",
                "--project-name",
                "内部管理后台示例",
                "--output",
                str(tmp_output),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertTrue(tmp_output.exists())
        output_text = tmp_output.read_text(encoding="utf-8")
        self.assertIn("# 项目拼装工作表", output_text)
        self.assertIn("内部管理后台示例", output_text)
        self.assertIn("FastAPI", output_text)

    def test_cli_reports_unknown_preset_name(self):
        # 验证输错项目预设时提示查看预设列表，避免用户误以为命令参数缺失。
        tmp_dir = ROOT / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_index = tmp_dir / "generate-worksheet-unknown-preset-index.json"
        tmp_output = tmp_dir / "stack-selection-unknown-preset.md"
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
                "--preset",
                "未知项目",
                "--output",
                str(tmp_output),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 2)
        self.assertFalse(tmp_output.exists())
        self.assertIn("未知项目预设", result.stderr)


if __name__ == "__main__":
    unittest.main()
