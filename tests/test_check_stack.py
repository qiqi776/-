"""验证技术栈风险检查脚本能按组件名输出决策风险。"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "check_stack.py"


def load_check_tool():
    # 动态加载风险检查脚本，便于直接测试匹配和风险分析逻辑。
    spec = importlib.util.spec_from_file_location("check_stack", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StackCheckTests(unittest.TestCase):
    def setUp(self):
        # 构造最小组件索引，覆盖低风险、高成本和强约束许可证三类结果。
        self.components = [
            {
                "name": "FastAPI",
                "category": "backend",
                "license": "MIT",
                "integration_cost": "低",
                "avoid_when": "需要完整全栈框架。",
            },
            {
                "name": "Grafana",
                "category": "observability",
                "license": "AGPL-3.0",
                "integration_cost": "中",
                "avoid_when": "团队不能接受 AGPL 义务。",
            },
            {
                "name": "Keycloak",
                "category": "auth",
                "license": "Apache-2.0",
                "integration_cost": "高",
                "avoid_when": "只需要轻量登录。",
            },
            {
                "name": "Phoenix",
                "category": "llm-observability-evaluation",
                "license": "Elastic-2.0",
                "integration_cost": "中",
                "avoid_when": "计划作为托管服务对外提供。",
            },
        ]

    def test_build_component_checks_marks_license_and_cost_risks(self):
        # 验证强约束许可证和高接入成本会进入风险提示。
        check_tool = load_check_tool()

        checks = check_tool.build_component_checks(self.components, ["FastAPI", "Grafana", "Keycloak"])

        self.assertEqual(checks[0]["component"], "FastAPI")
        self.assertEqual(checks[0]["risk_level"], "低")
        self.assertIn("暂未发现明显目录风险", checks[0]["risk_notes"])
        self.assertEqual(checks[1]["risk_level"], "高")
        self.assertIn("许可证需要重点审查", checks[1]["risk_notes"])
        self.assertEqual(checks[2]["risk_level"], "高")
        self.assertIn("接入成本高", checks[2]["risk_notes"])

    def test_build_component_checks_marks_elastic_license_for_review(self):
        # 验证 Elastic License 这类非宽松许可证也会进入重点审查提示。
        check_tool = load_check_tool()

        checks = check_tool.build_component_checks(self.components, ["Phoenix"])

        self.assertEqual(checks[0]["component"], "Phoenix")
        self.assertEqual(checks[0]["risk_level"], "高")
        self.assertIn("许可证需要重点审查", checks[0]["risk_notes"])
        self.assertIn("计划作为托管服务对外提供", checks[0]["risk_notes"])

    def test_build_component_checks_reports_missing_component(self):
        # 验证输入了目录中不存在的组件名时会保留缺失项，方便人工补录。
        check_tool = load_check_tool()

        checks = check_tool.build_component_checks(self.components, ["Unknown"])

        self.assertEqual(checks[0]["component"], "Unknown")
        self.assertEqual(checks[0]["category"], "")
        self.assertEqual(checks[0]["risk_level"], "高")
        self.assertIn("目录中未找到该组件", checks[0]["risk_notes"])

    def test_cli_outputs_markdown_risk_table(self):
        # 验证命令行能读取索引并输出可复制到技术栈决策文档的风险表。
        tmp_index = ROOT / "tmp" / "check-stack-index.json"
        tmp_index.parent.mkdir(parents=True, exist_ok=True)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--index", str(tmp_index), "--components", "FastAPI,Grafana"],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("| 组件 | 分类 | 许可证 | 接入成本 | 风险等级 | 风险提示 |", result.stdout)
        self.assertIn("| FastAPI | backend | MIT | 低 | 低 |", result.stdout)
        self.assertIn("| Grafana | observability | AGPL-3.0 | 中 | 高 |", result.stdout)


if __name__ == "__main__":
    unittest.main()
