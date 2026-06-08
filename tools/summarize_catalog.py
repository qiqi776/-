#!/usr/bin/env python3
"""生成组件目录的分类概览，帮助快速判断有哪些模块可拼装。"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


COST_RANK = {"低": 0, "中": 1, "高": 2}


def load_components(path: Path) -> list[dict[str, Any]]:
    """读取 catalog/index.json 并返回组件列表。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("components", [])


def score_value(component: dict[str, Any]) -> int:
    """把 5/5 这类评分转换成整数，无法解析时按 0 分处理。"""
    raw_score = str(component.get("score", "0/5"))
    try:
        return int(raw_score.split("/", 1)[0])
    except ValueError:
        return 0


def cost_value(component: dict[str, Any]) -> int:
    """把中文接入成本转换成可排序的数字，未知成本排到最后。"""
    return COST_RANK.get(str(component.get("integration_cost", "")), 9)


def top_component_name(components: list[dict[str, Any]]) -> str:
    """返回评分最高、成本更低的组件名称，用作分类里的优先候选。"""
    ordered = sorted(
        components,
        key=lambda component: (-score_value(component), cost_value(component), str(component.get("name", ""))),
    )
    return str(ordered[0].get("name", "")) if ordered else ""


def lowest_cost_label(components: list[dict[str, Any]]) -> str:
    """返回该分类中出现过的最低接入成本。"""
    known_costs = [str(component.get("integration_cost", "")) for component in components]
    known_costs = [cost for cost in known_costs if cost in COST_RANK]
    if not known_costs:
        return ""
    return min(known_costs, key=lambda cost: COST_RANK[cost])


def summarize_categories(components: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按分类汇总组件数量、最高评分组件和最低接入成本。"""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for component in components:
        category = str(component.get("category", "")).strip()
        if category:
            grouped[category].append(component)

    summaries = []
    for category in sorted(grouped):
        category_components = grouped[category]
        summaries.append(
            {
                "category": category,
                "component_count": len(category_components),
                "top_component": top_component_name(category_components),
                "lowest_cost": lowest_cost_label(category_components),
            }
        )
    return summaries


def format_summary_table(summaries: list[dict[str, Any]]) -> str:
    """把分类概览格式化成 Markdown 表格。"""
    lines = [
        "# 组件分类概览",
        "",
        "| 分类 | 组件数量 | 最高评分组件 | 最低接入成本 |",
        "| --- | ---: | --- | --- |",
    ]
    for summary in summaries:
        lines.append(
            "| {category} | {component_count} | {top_component} | {lowest_cost} |".format(
                category=summary["category"],
                component_count=summary["component_count"],
                top_component=summary["top_component"],
                lowest_cost=summary["lowest_cost"],
            )
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """命令行入口：读取索引并输出分类概览表。"""
    parser = argparse.ArgumentParser(description="生成组件分类概览")
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("catalog/index.json"),
        help="组件索引 JSON 文件路径",
    )
    args = parser.parse_args(argv)

    components = load_components(args.index)
    summaries = summarize_categories(components)
    print(format_summary_table(summaries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
