#!/usr/bin/env python3
"""根据需要的模块生成项目技术栈决策草案。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from stack_presets import STACK_PRESETS, format_presets, preset_exists, resolve_modules


COST_RANK = {"低": 0, "中": 1, "高": 2}


def load_components(path: Path) -> list[dict[str, Any]]:
    """读取 catalog/index.json 并返回组件列表。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("components", [])


def score_value(component: dict[str, Any]) -> int:
    """把 4/5 这类评分转换成整数，无法解析时按 0 分处理。"""
    raw_score = str(component.get("score", "0/5"))
    try:
        return int(raw_score.split("/", 1)[0])
    except ValueError:
        return 0


def component_sort_key(component: dict[str, Any]) -> tuple[int, int, str]:
    """排序规则：评分高优先，接入成本低优先，名称稳定排序。"""
    cost = COST_RANK.get(str(component.get("integration_cost", "")), 9)
    return (-score_value(component), cost, str(component.get("name", "")))


def select_for_category(
    components: list[dict[str, Any]],
    category: str,
) -> dict[str, Any]:
    """为单个模块选择主组件和备选组件。"""
    candidates = [component for component in components if component.get("category") == category]
    ordered = sorted(candidates, key=component_sort_key)
    primary = ordered[0] if ordered else None
    fallback = ordered[1] if len(ordered) > 1 else None

    if primary is None:
        reason = "目录中暂未收录该模块组件。"
        risk = reason
    else:
        reason = primary.get("notes") or primary.get("best_for") or "评分和接入成本综合排序最高。"
        risk = primary.get("avoid_when") or "需要进一步验证许可证、托管方式和团队经验。"

    return {
        "category": category,
        "primary": primary,
        "fallback": fallback,
        "reason": reason,
        "risk": risk,
    }


def build_stack_decisions(
    components: list[dict[str, Any]],
    categories: list[str],
) -> list[dict[str, Any]]:
    """为多个模块生成技术栈决策草案。"""
    return [select_for_category(components, category) for category in categories]


def component_name(component: dict[str, Any] | None) -> str:
    """返回组件名称；缺失时返回空字符串，方便 Markdown 表格显示。"""
    if component is None:
        return ""
    return str(component.get("name", ""))


def component_license(component: dict[str, Any] | None) -> str:
    """返回主组件许可证；缺失组件时返回空字符串，便于人工后续补齐。"""
    if component is None:
        return ""
    return str(component.get("license", ""))


def component_integration_cost(component: dict[str, Any] | None) -> str:
    """返回主组件接入成本；缺失组件时返回空字符串，避免误导决策。"""
    if component is None:
        return ""
    return str(component.get("integration_cost", ""))


def format_stack_table(decisions: list[dict[str, Any]]) -> str:
    """把技术栈决策草案格式化成 Markdown 表格。"""
    lines = [
        "# 技术栈决策草案",
        "",
        "| 模块 | 主组件 | 许可证 | 接入成本 | 备选组件 | 选择理由 | 主要风险 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for decision in decisions:
        lines.append(
            "| {category} | {primary} | {license} | {cost} | {fallback} | {reason} | {risk} |".format(
                category=decision["category"],
                primary=component_name(decision["primary"]),
                license=component_license(decision["primary"]),
                cost=component_integration_cost(decision["primary"]),
                fallback=component_name(decision["fallback"]),
                reason=decision["reason"],
                risk=decision["risk"],
            )
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """命令行入口：读取索引并输出技术栈决策草案。"""
    parser = argparse.ArgumentParser(description="生成项目技术栈决策草案")
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
        help="列出内置项目预设及其包含的模块，不生成技术栈草案",
    )
    args = parser.parse_args(argv)

    if args.list_presets:
        # 只查看预设时不读取组件索引，便于在生成索引前先确认模块范围。
        print(format_presets())
        return 0

    components = load_components(args.index)
    modules = resolve_modules(args.modules, args.preset)
    if not modules:
        if args.preset and not preset_exists(args.preset):
            parser.error(f"未知项目预设: {args.preset}。请先运行 --list-presets 查看可用写法。")
        parser.error("必须提供 --modules 或 --preset。")
    decisions = build_stack_decisions(components, modules)
    print(format_stack_table(decisions))
    return 0


if __name__ == "__main__":
    sys.exit(main())
