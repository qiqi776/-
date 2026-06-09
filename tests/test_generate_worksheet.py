"""验证项目拼装工作表生成脚本能把模块选择直接落成文档。"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "generate_worksheet.py"


def load_generate_tool():
    # 动态加载工作表生成脚本，便于直接测试格式化逻辑。
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
                "license": "MIT",
                "integration_cost": "低",
                "score": "5/5",
                "notes": "适合 AI 项目。",
                "avoid_when": "需要完整全栈框架。",
            },
            {
                "name": "Django",
                "category": "backend",
                "license": "BSD-3-Clause",
                "integration_cost": "中",
                "score": "4/5",
                "notes": "适合完整后台。",
                "avoid_when": "只需要轻量 API。",
            },
            {
                "name": "Grafana",
                "category": "observability",
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
        self.assertIn("| backend | 是 | FastAPI | Django | 适合 AI 项目。 | 需要完整全栈框架。 |", worksheet)
        self.assertIn("| observability | 是 | Grafana |  | 适合仪表盘。 | 团队不能接受 AGPL 义务。 |", worksheet)
        self.assertIn("| Grafana | AGPL-3.0 | 待确认 | 许可证需要重点审查", worksheet)

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
                "--modules",
                "backend,observability",
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


if __name__ == "__main__":
    unittest.main()
