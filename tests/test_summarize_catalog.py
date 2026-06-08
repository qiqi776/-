"""验证组件分类概览脚本能生成模块级摘要。"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "summarize_catalog.py"


def load_summary_tool():
    # 动态加载分类概览脚本，便于直接测试汇总逻辑。
    spec = importlib.util.spec_from_file_location("summarize_catalog", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CatalogSummaryTests(unittest.TestCase):
    def setUp(self):
        # 构造最小组件索引，覆盖组件数量、最高评分和最低接入成本统计。
        self.components = [
            {
                "name": "FastAPI",
                "category": "backend",
                "module": "后端 / API",
                "integration_cost": "低",
                "score": "5/5",
            },
            {
                "name": "NestJS",
                "category": "backend",
                "module": "后端 / API",
                "integration_cost": "中",
                "score": "4/5",
            },
            {
                "name": "Keycloak",
                "category": "auth",
                "module": "认证 / IAM",
                "integration_cost": "高",
                "score": "4/5",
            },
        ]

    def test_summarize_categories_groups_components(self):
        # 验证分类汇总会按模块聚合数量、最高评分组件和最低接入成本。
        summary_tool = load_summary_tool()

        summaries = summary_tool.summarize_categories(self.components)

        self.assertEqual(summaries[0]["category"], "auth")
        self.assertEqual(summaries[0]["component_count"], 1)
        self.assertEqual(summaries[0]["top_component"], "Keycloak")
        self.assertEqual(summaries[0]["lowest_cost"], "高")
        self.assertEqual(summaries[1]["category"], "backend")
        self.assertEqual(summaries[1]["component_count"], 2)
        self.assertEqual(summaries[1]["top_component"], "FastAPI")
        self.assertEqual(summaries[1]["lowest_cost"], "低")

    def test_cli_outputs_markdown_summary_table(self):
        # 验证命令行能读取索引并输出方便复制到文档的 Markdown 表格。
        tmp_index = ROOT / "tmp" / "summary-test-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--index", str(tmp_index)],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("| 分类 | 组件数量 | 最高评分组件 | 最低接入成本 |", result.stdout)
        self.assertIn("| backend | 2 | FastAPI | 低 |", result.stdout)
        self.assertIn("| auth | 1 | Keycloak | 高 |", result.stdout)


if __name__ == "__main__":
    unittest.main()
