"""验证项目预设由共享模块统一提供，避免不同拼装工具蓝图漂移。"""

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
ASSEMBLE_SCRIPT = ROOT / "tools" / "assemble_stack.py"
WORKSHEET_SCRIPT = ROOT / "tools" / "generate_worksheet.py"


def load_module(module_name, path):
    # 动态加载脚本模块，便于在没有安装包的仓库结构中直接测试共享对象。
    tools_path = str(TOOLS_DIR)
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StackPresetTests(unittest.TestCase):
    def test_tools_share_stack_presets(self):
        # 验证两个项目拼装入口都引用同一份预设定义，后续新增蓝图只需要改一个地方。
        tools_path = str(TOOLS_DIR)
        if tools_path not in sys.path:
            sys.path.insert(0, tools_path)
        import stack_presets

        assemble_stack = load_module("assemble_stack", ASSEMBLE_SCRIPT)
        generate_worksheet = load_module("generate_worksheet", WORKSHEET_SCRIPT)

        self.assertIs(assemble_stack.STACK_PRESETS, stack_presets.STACK_PRESETS)
        self.assertIs(generate_worksheet.STACK_PRESETS, stack_presets.STACK_PRESETS)
        self.assertIn("saas-starter", stack_presets.STACK_PRESETS)
        self.assertIn("ai-rag-app", stack_presets.STACK_PRESETS)
        self.assertIn("internal-admin", stack_presets.STACK_PRESETS)


if __name__ == "__main__":
    unittest.main()
