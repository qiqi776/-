#!/usr/bin/env python3
"""按分类、接入成本和关键词搜索组件索引。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SEARCH_FIELDS = [
    "name",
    "category",
    "module",
    "tech_stack",
    "license",
    "best_for",
    "avoid_when",
    "integration_cost",
    "alternatives",
    "score",
    "notes",
]


def load_index(path: Path) -> list[dict[str, Any]]:
    """读取 catalog/index.json 并返回组件列表。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("components", [])


def contains_keyword(component: dict[str, Any], keyword: str) -> bool:
    """在组件的主要文本字段中做大小写不敏感匹配。"""
    needle = keyword.casefold()
    for field in SEARCH_FIELDS:
        value = str(component.get(field, ""))
        if needle in value.casefold():
            return True
    return False


def filter_components(
    components: list[dict[str, Any]],
    *,
    category: str | None,
    integration_cost: str | None,
    keyword: str | None,
) -> list[dict[str, Any]]:
    """根据分类、接入成本和关键词筛选组件。"""
    result = []
    for component in components:
        if category and component.get("category") != category:
            continue
        if integration_cost and component.get("integration_cost") != integration_cost:
            continue
        if keyword and not contains_keyword(component, keyword):
            continue
        result.append(component)
    return result


def format_markdown_table(components: list[dict[str, Any]]) -> str:
    """把搜索结果格式化成便于复制到项目文档的 Markdown 表格。"""
    lines = [
        "| 名称 | 分类 | 接入成本 | 评分 | GitHub |",
        "| --- | --- | --- | --- | --- |",
    ]
    for component in components:
        name = component.get("name", "")
        category = component.get("category", "")
        cost = component.get("integration_cost", "")
        score = component.get("score", "")
        github = component.get("github", "")
        lines.append(f"| {name} | {category} | {cost} | {score} | {github} |")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """命令行入口：读取索引、筛选组件、输出 Markdown 表格。"""
    parser = argparse.ArgumentParser(description="搜索开源组件目录")
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("catalog/index.json"),
        help="组件索引 JSON 文件路径",
    )
    parser.add_argument("--category", help="按 catalog 分类筛选，例如 backend、ai、auth")
    parser.add_argument("--cost", choices=["低", "中", "高"], help="按接入成本筛选")
    parser.add_argument("--keyword", help="按名称、模块、技术栈、备注等字段搜索")
    args = parser.parse_args(argv)

    components = load_index(args.index)
    result = filter_components(
        components,
        category=args.category,
        integration_cost=args.cost,
        keyword=args.keyword,
    )

    print(format_markdown_table(result))
    print(f"\n共找到 {len(result)} 个组件。")
    return 0


if __name__ == "__main__":
    sys.exit(main())

