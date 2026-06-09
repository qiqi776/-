#!/usr/bin/env python3
"""发布到 GitHub 前运行本地校验、单元测试和远端配置检查。"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_TEST_MODULES = [
    "tests.test_validate_catalog",
    "tests.test_search_catalog",
    "tests.test_stack_presets",
    "tests.test_assemble_stack",
    "tests.test_summarize_catalog",
    "tests.test_check_stack",
    "tests.test_generate_worksheet",
    "tests.test_generate_project_package",
    "tests.test_pre_publish_check",
]
CHECK_CHOICES = ["validate", "tests", "remote"]


def run_command(command: list[str], root: Path) -> int:
    """运行子命令并把输出直接透传给终端，便于定位失败步骤。"""
    result = subprocess.run(command, cwd=root, check=False)
    return result.returncode


def run_catalog_validation(root: Path) -> int:
    """运行目录校验，确认组件条目、预设和蓝图结构都可发布。"""
    print("== 组件目录校验 ==", flush=True)
    return run_command([sys.executable, "tools/validate_catalog.py"], root)


def run_unit_tests(root: Path, test_modules: list[str]) -> int:
    """逐个运行 unittest 模块，输出和 GitHub Actions 保持接近。"""
    print("== 单元测试 ==", flush=True)
    for module in test_modules:
        print(f"-- {module}", flush=True)
        exit_code = run_command([sys.executable, "-m", "unittest", module, "-v"], root)
        if exit_code != 0:
            return exit_code
    return 0


def configured_remotes(root: Path) -> list[str]:
    """读取 git remote 列表；没有 Git 仓库或没有远端时返回空列表。"""
    result = subprocess.run(
        ["git", "remote"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def check_git_remote(root: Path) -> int:
    """检查是否已配置 GitHub 远端；缺失时只提示，不阻断本地校验。"""
    print("== GitHub 远端检查 ==", flush=True)
    remotes = configured_remotes(root)
    if not remotes:
        print("未配置 GitHub 远端。发布前请按 docs/github-publish-guide.md 添加 origin。", flush=True)
        return 0
    print(f"已配置 Git 远端: {', '.join(remotes)}", flush=True)
    return 0


def main(argv: list[str] | None = None) -> int:
    """命令行入口：按选择的检查项执行发布前自检。"""
    parser = argparse.ArgumentParser(description="运行 GitHub 发布前本地检查")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="仓库根目录")
    parser.add_argument(
        "--check",
        action="append",
        choices=CHECK_CHOICES,
        help="要运行的检查项，可重复传入；默认运行全部检查",
    )
    parser.add_argument(
        "--test-module",
        action="append",
        help="指定要运行的 unittest 模块，可重复传入；默认运行完整测试清单",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    checks = args.check or CHECK_CHOICES
    test_modules = args.test_module or DEFAULT_TEST_MODULES

    if "validate" in checks:
        exit_code = run_catalog_validation(root)
        if exit_code != 0:
            return exit_code

    if "tests" in checks:
        exit_code = run_unit_tests(root, test_modules)
        if exit_code != 0:
            return exit_code

    if "remote" in checks:
        exit_code = check_git_remote(root)
        if exit_code != 0:
            return exit_code
    elif not configured_remotes(root):
        print("未配置 GitHub 远端。发布前请按 docs/github-publish-guide.md 添加 origin。", flush=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
