"""验证组件搜索脚本能按分类、成本、关键词和成熟开源条件筛选组件。"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "search_catalog.py"


def load_search_tool():
    # 动态加载搜索脚本，便于直接测试筛选函数。
    spec = importlib.util.spec_from_file_location("search_catalog", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CatalogSearchTests(unittest.TestCase):
    def setUp(self):
        # 使用内存中的最小索引，避免测试依赖真实 catalog 内容。
        self.index = {
            "component_count": 6,
            "components": [
                {
                    "name": "FastAPI",
                    "category": "backend",
                    "github": "https://github.com/fastapi/fastapi",
                    "module": "后端 / API",
                    "tech_stack": "Python",
                    "license": "MIT",
                    "best_for": "Python API。",
                    "avoid_when": "需要完整全栈框架。",
                    "integration_cost": "低",
                    "score": "5/5",
                    "notes": "适合 AI 项目。",
                },
                {
                    "name": "Keycloak",
                    "category": "auth",
                    "github": "https://github.com/keycloak/keycloak",
                    "module": "认证 / IAM",
                    "tech_stack": "Java",
                    "license": "Apache-2.0",
                    "best_for": "企业身份。",
                    "avoid_when": "只需要轻量登录。",
                    "integration_cost": "高",
                    "score": "4/5",
                    "notes": "能力强但运维重。",
                },
                {
                    "name": "LlamaIndex",
                    "category": "ai",
                    "github": "https://github.com/run-llama/llama_index",
                    "module": "AI / RAG",
                    "tech_stack": "Python",
                    "license": "MIT",
                    "best_for": "RAG 应用。",
                    "avoid_when": "不需要检索。",
                    "integration_cost": "中",
                    "score": "4/5",
                    "notes": "适合私有数据问答。",
                },
                {
                    "name": "PrototypeAuth",
                    "category": "auth",
                    "github": "https://github.com/example/prototype-auth",
                    "module": "认证 / 原型",
                    "tech_stack": "TypeScript",
                    "license": "MIT",
                    "best_for": "内部 Demo。",
                    "avoid_when": "需要生产身份系统。",
                    "integration_cost": "低",
                    "score": "2/5",
                    "notes": "成熟度不足。",
                },
                {
                    "name": "ClosedCRM",
                    "category": "crm",
                    "github": "https://github.com/example/closed-crm",
                    "module": "CRM / 销售",
                    "tech_stack": "Ruby",
                    "license": "商业许可证",
                    "best_for": "托管 CRM。",
                    "avoid_when": "需要标准开源许可证。",
                    "integration_cost": "中",
                    "score": "5/5",
                    "notes": "许可证不适合开源优先目录。",
                },
                {
                    "name": "NoRepoBI",
                    "category": "business-intelligence",
                    "github": "",
                    "module": "BI / 报表",
                    "tech_stack": "Java",
                    "license": "Apache-2.0",
                    "best_for": "报表。",
                    "avoid_when": "需要可追踪源码仓库。",
                    "integration_cost": "中",
                    "score": "4/5",
                    "notes": "缺少 GitHub 地址。",
                },
            ],
        }

    def test_filter_components_by_category_and_cost(self):
        # 验证分类和接入成本可以组合筛选。
        search_tool = load_search_tool()

        result = search_tool.filter_components(
            self.index["components"],
            category="backend",
            integration_cost="低",
            keyword=None,
            mature_only=False,
        )

        self.assertEqual([component["name"] for component in result], ["FastAPI"])

    def test_filter_components_by_keyword_across_text_fields(self):
        # 验证关键词能匹配名称、模块、技术栈、适合场景和备注。
        search_tool = load_search_tool()

        result = search_tool.filter_components(
            self.index["components"],
            category=None,
            integration_cost=None,
            keyword="RAG",
            mature_only=False,
        )

        self.assertEqual([component["name"] for component in result], ["LlamaIndex"])

    def test_filter_components_can_keep_only_mature_open_source_options(self):
        # 验证成熟开源筛选会保留评分高、许可证清楚且有 GitHub 的组件。
        search_tool = load_search_tool()

        result = search_tool.filter_components(
            self.index["components"],
            category=None,
            integration_cost=None,
            keyword=None,
            mature_only=True,
        )

        self.assertEqual([component["name"] for component in result], ["FastAPI", "Keycloak", "LlamaIndex"])

    def test_cli_outputs_markdown_rows(self):
        # 验证命令行能读取 index.json 并输出便于复制的 Markdown 表格。
        tmp_index = ROOT / "tmp" / "search-test-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(json.dumps(self.index, ensure_ascii=False), encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--category",
                "auth",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("Keycloak", result.stdout)
        self.assertIn("| 名称 | 分类 | 接入成本 | 评分 | GitHub |", result.stdout)

    def test_cli_accepts_mature_only_filter(self):
        # 验证命令行可以直接输出成熟开源候选，方便项目选型前先过滤目录。
        tmp_index = ROOT / "tmp" / "search-test-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(json.dumps(self.index, ensure_ascii=False), encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--mature-only",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("FastAPI", result.stdout)
        self.assertIn("Keycloak", result.stdout)
        self.assertNotIn("PrototypeAuth", result.stdout)
        self.assertNotIn("ClosedCRM", result.stdout)
        self.assertNotIn("NoRepoBI", result.stdout)
        self.assertIn("共找到 3 个组件。", result.stdout)


if __name__ == "__main__":
    unittest.main()
