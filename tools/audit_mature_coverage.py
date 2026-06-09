#!/usr/bin/env python3
"""审计项目模块是否已有成熟开源组件候选。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from search_catalog import is_mature_open_source
from stack_presets import format_presets, preset_exists, resolve_modules


EXAMPLE_LIMIT = 3


def load_index(path: Path) -> list[dict[str, Any]]:
    """读取 catalog/index.json 并返回组件列表。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("components", [])


def audit_categories(components: list[dict[str, Any]], categories: list[str]) -> list[dict[str, Any]]:
    """按模块统计组件总数、成熟开源候选数量和示例名称。"""
    rows: list[dict[str, Any]] = []
    for category in categories:
        category_components = [component for component in components if component.get("category") == category]
        mature_components = [component for component in category_components if is_mature_open_source(component)]
        rows.append(
            {
                "category": category,
                "total_count": len(category_components),
                "mature_count": len(mature_components),
                "status": "通过" if mature_components else "缺口",
                "examples": [str(component.get("name", "")) for component in mature_components[:EXAMPLE_LIMIT]],
            }
        )
    return rows


def missing_categories(rows: list[dict[str, Any]]) -> list[str]:
    """返回缺少成熟开源候选的模块列表。"""
    return [str(row["category"]) for row in rows if int(row["mature_count"]) == 0]


def format_markdown_table(rows: list[dict[str, Any]]) -> str:
    """把覆盖审计结果格式化成 Markdown 表格，方便复制进项目文档。"""
    lines = [
        "| 分类 | 组件总数 | 成熟开源数 | 状态 | 示例 |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for row in rows:
        examples = ", ".join(row["examples"]) if row["examples"] else "-"
        lines.append(
            f"| {row['category']} | {row['total_count']} | {row['mature_count']} | {row['status']} | {examples} |"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """命令行入口：审计指定模块或项目预设的成熟开源覆盖情况。"""
    parser = argparse.ArgumentParser(description="审计成熟开源组件覆盖情况")
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("catalog/index.json"),
        help="组件索引 JSON 文件路径",
    )
    parser.add_argument("--modules", default="", help="逗号分隔的模块分类，支持常用中文别名")
    parser.add_argument("--preset", help="项目预设 slug 或中文项目类型")
    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="列出可用项目预设后退出",
    )
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="如果任一模块缺少成熟开源候选，则返回非零退出码",
    )
    args = parser.parse_args(argv)

    if args.list_presets:
        print(format_presets())
        return 0

    if args.preset and not preset_exists(args.preset):
        parser.error(f"未知项目预设: {args.preset}。请先运行 --list-presets 查看可用写法。")

    categories = resolve_modules(args.modules, args.preset)
    if not categories:
        parser.error("必须提供 --modules 或 --preset。")

    components = load_index(args.index)
    rows = audit_categories(components, categories)
    gaps = missing_categories(rows)

    print(format_markdown_table(rows))
    if gaps:
        print(f"\n成熟开源覆盖缺口: {', '.join(gaps)}")
    else:
        print("\n所有模块都有成熟开源候选。")

    return 1 if args.fail_on_missing and gaps else 0


if __name__ == "__main__":
    sys.exit(main())
