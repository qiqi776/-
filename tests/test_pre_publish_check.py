"""验证 GitHub 发布前检查脚本能串起本地关键校验。"""

import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "pre_publish_check.py"


def load_pre_publish_module():
    """按文件路径加载发布前检查脚本，便于直接检查默认配置。"""
    spec = importlib.util.spec_from_file_location("pre_publish_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class PrePublishCheckTests(unittest.TestCase):
    def test_default_test_modules_include_pre_publish_check_tests(self):
        # 确认完整发布前检查不会遗漏自检脚本自己的回归测试。
        module = load_pre_publish_module()

        self.assertIn("tests.test_pre_publish_check", module.DEFAULT_TEST_MODULES)
        self.assertIn("tests.test_generate_project_package", module.DEFAULT_TEST_MODULES)

    def test_cli_runs_selected_validation_and_tests(self):
        # 验证脚本能运行选定目录校验和测试模块。
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(ROOT),
                "--check",
                "validate",
                "--check",
                "tests",
                "--test-module",
                "tests.test_stack_presets",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("组件目录校验通过", result.stdout)
        self.assertIn("tests.test_stack_presets", result.stdout)

    def test_validation_heading_prints_before_child_output(self):
        # 确认父脚本标题先输出，避免发布前检查日志顺序倒置。
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(ROOT),
                "--check",
                "validate",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertLess(result.stdout.index("== 组件目录校验 =="), result.stdout.index("组件目录校验通过"))

    def test_cli_warns_when_remote_missing(self):
        # 使用临时 Git 仓库隔离远端状态，避免测试依赖当前工作区或 CI 环境。
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            subprocess.run(["git", "init"], cwd=temp_root, check=True, capture_output=True)

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--root",
                    str(temp_root),
                    "--check",
                    "remote",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0)
        self.assertIn("未配置 GitHub 远端", result.stdout)


if __name__ == "__main__":
    unittest.main()
