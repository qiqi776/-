#!/usr/bin/env python3
"""一次性生成项目拼装包，包含选型 JSON、组件清单、风险报告和实施计划。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from assemble_stack import (
    build_stack_decisions,
    capability_label,
    component_name,
    format_component_manifest,
    format_stack_json,
    first_integration_action,
    load_components,
    license_needs_review,
)
from check_stack import build_component_checks, format_risk_table
from stack_presets import format_presets, preset_exists, resolve_modules


COST_RANK = {"低": 0, "中": 1, "高": 2}


def selected_primary_names(decisions: list[dict]) -> list[str]:
    """从技术栈决策中提取已选主组件名称，供风险检查复用。"""
    names = []
    for decision in decisions:
        primary = decision["primary"]
        if not primary:
            continue
        name = str(primary.get("name", "")).strip()
        if name:
            names.append(name)
    return names


def integration_priority_key(decision: dict) -> tuple[int, int, str]:
    """按真实落地风险排序：缺失组件、许可证风险和高接入成本优先验证。"""
    primary = decision["primary"]
    if not primary:
        return (-100, 0, str(decision["category"]))

    priority = 0
    license_text = str(primary.get("license", ""))
    integration_cost = str(primary.get("integration_cost", ""))
    if license_needs_review(license_text):
        priority += 50
    priority += COST_RANK.get(integration_cost, 0) * 10
    return (-priority, COST_RANK.get(integration_cost, 9), component_name(primary))


def integration_risk_reason(decision: dict) -> str:
    """生成实施计划中的风险原因，帮助团队决定先验证什么。"""
    primary = decision["primary"]
    if not primary:
        return "目录中暂未收录该模块组件。"
    risk = str(decision["risk"]).strip()
    return risk or "需要确认许可证、托管方式和数据边界。"


def format_integration_plan(decisions: list[dict]) -> str:
    """生成按风险排序的集成实施计划，指导新项目先验证关键模块。"""
    lines = [
        "# 集成实施计划",
        "",
        "按许可证、接入成本和缺失组件风险排序，先验证最可能影响项目落地的集成项。",
        "",
        "| 顺序 | 集成项 | 风险原因 | 首个动作 | 通过标准 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for index, decision in enumerate(sorted(decisions, key=integration_priority_key), start=1):
        primary = decision["primary"]
        integration_name = f"{capability_label(decision)} / {component_name(primary) or '待选组件'}"
        lines.append(
            "| {index} | {integration} | {risk} | {action} | {acceptance} |".format(
                index=index,
                integration=integration_name,
                risk=integration_risk_reason(decision),
                action=first_integration_action(primary),
                acceptance="能跑通最小样例，并记录配置、限制、失败回退方案和负责人。",
            )
        )
    return "\n".join(lines)


def package_readme(project_name: str) -> str:
    """生成拼装包说明，帮助用户理解每个文件的用途。"""
    title = project_name or "未命名项目"
    lines = [
        f"# {title} 组件拼装包",
        "",
        "这个目录由组件库工具生成，用来把新项目的组件选型结果集中保存。",
        "",
        "## 文件说明",
        "",
        "- `stack-plan.json`: 机器可读技术栈清单，适合交给脚手架或后续自动化读取。",
        "- `component-manifest.md`: 可放入新项目仓库的组件清单，记录能力、主组件、链接、首个动作和待确认事项。",
        "- `risk-check.md`: 根据目录字段生成的风险检查表，用于先复核许可证、接入成本和缺失组件。",
        "- `integration-plan.md`: 按风险排序的集成实施计划，用于决定先验证哪个组件。",
        "",
        "## 使用建议",
        "",
        "1. 先阅读 `risk-check.md`，处理高风险许可证和高接入成本组件。",
        "2. 按 `integration-plan.md` 的顺序跑通最小集成，先验证最可能影响项目落地的模块。",
        "3. 把 `component-manifest.md` 放进新项目仓库，作为后续集成和替换组件的追踪清单。",
        "4. 保留 `stack-plan.json`，让模板、脚手架或其他自动化工具继续消费。",
        "",
        "这些文件只是第一版草案，真实项目仍需要人工确认许可证、托管方式、数据边界和业务合规。",
    ]
    return "\n".join(lines) + "\n"


def generate_project_package(
    components: list[dict],
    modules: list[str],
    project_name: str,
    output_dir: Path,
) -> list[Path]:
    """生成项目拼装包文件，并返回写出的文件路径。"""
    decisions = build_stack_decisions(components, modules)
    primary_names = selected_primary_names(decisions)
    risk_checks = build_component_checks(components, primary_names)

    output_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "README.md": package_readme(project_name),
        "stack-plan.json": format_stack_json(decisions) + "\n",
        "component-manifest.md": format_component_manifest(decisions) + "\n",
        "risk-check.md": format_risk_table(risk_checks) + "\n",
        "integration-plan.md": format_integration_plan(decisions) + "\n",
    }

    written_paths = []
    for filename, content in files.items():
        path = output_dir / filename
        path.write_text(content, encoding="utf-8")
        written_paths.append(path)
    return written_paths


def main(argv: list[str] | None = None) -> int:
    """命令行入口：按模块或预设生成项目拼装包。"""
    parser = argparse.ArgumentParser(description="生成项目拼装包")
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("catalog/index.json"),
        help="组件索引 JSON 文件路径",
    )
    parser.add_argument(
        "--modules",
        default="",
        help="逗号分隔的模块分类，例如 frontend,backend,auth,database",
    )
    parser.add_argument(
        "--preset",
        help="内置项目预设，例如 saas-starter、AI RAG 应用、内部管理后台；显式 --modules 会优先生效。",
    )
    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="列出内置项目预设及其包含的模块，不生成拼装包",
    )
    parser.add_argument("--project-name", default="", help="项目名称，会写入拼装包 README")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("project-package"),
        help="输出目录，默认写入 project-package",
    )
    args = parser.parse_args(argv)

    if args.list_presets:
        # 只查看预设时不读取索引，便于先确认项目蓝图。
        print(format_presets())
        return 0

    components = load_components(args.index)
    modules = resolve_modules(args.modules, args.preset)
    if not modules:
        if args.preset and not preset_exists(args.preset):
            parser.error(f"未知项目预设: {args.preset}。请先运行 --list-presets 查看可用写法。")
        parser.error("必须提供 --modules 或 --preset。")

    written_paths = generate_project_package(components, modules, args.project_name, args.output_dir)
    print(f"已生成项目拼装包: {args.output_dir}")
    for path in written_paths:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
