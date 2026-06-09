#!/usr/bin/env python3
"""按分类、接入成本、关键词和成熟开源条件搜索组件索引。"""

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

MIN_MATURE_SCORE = 4
NON_OPEN_LICENSE_KEYWORDS = ("商业许可证", "SOURCE-AVAILABLE", "BUSL", "BSL", "SSPL", "ELASTIC")


def score_value(component: dict[str, Any]) -> int:
    """把 4/5 这类评分转换成整数，无法解析时按 0 分处理。"""
    raw_score = str(component.get("score", "0/5"))
    try:
        return int(raw_score.split("/", 1)[0])
    except ValueError:
        return 0


def has_github_repo(component: dict[str, Any]) -> bool:
    """判断组件是否有可追踪的 GitHub 仓库地址。"""
    return str(component.get("github", "")).startswith("https://github.com/")


def has_clear_open_source_license(component: dict[str, Any]) -> bool:
    """判断许可证字段是否清楚且没有明显非标准开源或商业限制关键词。"""
    license_text = str(component.get("license", "")).strip()
    if not license_text:
        return False
    normalized = license_text.upper()
    return not any(keyword.upper() in normalized for keyword in NON_OPEN_LICENSE_KEYWORDS)


def is_mature_open_source(component: dict[str, Any]) -> bool:
    """判断组件是否适合作为成熟开源候选：有 GitHub、许可证清楚且评分不低于 4/5。"""
    return (
        has_github_repo(component)
        and has_clear_open_source_license(component)
        and score_value(component) >= MIN_MATURE_SCORE
    )


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
    mature_only: bool,
) -> list[dict[str, Any]]:
    """根据分类、接入成本、关键词和成熟开源条件筛选组件。"""
    result = []
    for component in components:
        if category and component.get("category") != category:
            continue
        if integration_cost and component.get("integration_cost") != integration_cost:
            continue
        if keyword and not contains_keyword(component, keyword):
            continue
        if mature_only and not is_mature_open_source(component):
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
    parser.add_argument(
        "--mature-only",
        action="store_true",
        help="只显示有 GitHub、许可证清楚且评分不低于 4/5 的成熟开源候选",
    )
    args = parser.parse_args(argv)

    components = load_index(args.index)
    result = filter_components(
        components,
        category=args.category,
        integration_cost=args.cost,
        keyword=args.keyword,
        mature_only=args.mature_only,
    )

    print(format_markdown_table(result))
    print(f"\n共找到 {len(result)} 个组件。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
