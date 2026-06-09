#!/usr/bin/env python3
"""校验组件目录，并按需生成机器可读索引。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from stack_presets import STACK_PRESETS


# catalog 条目的中文必填字段；GitHub 保持英文是为了和平台名称一致。
REQUIRED_FIELDS = [
    "GitHub",
    "官网",
    "模块",
    "技术栈",
    "许可证",
    "适合",
    "不适合",
    "接入成本",
    "替代方案",
    "评分",
    "备注",
]

VALID_COSTS = {"低", "中", "高"}
GITHUB_URL_RE = re.compile(r"^https://github\.com/[^/\s]+/[^/\s]+/?$")
SCORE_RE = re.compile(r"^[1-5]/5$")


def catalog_categories(root: Path) -> set[str]:
    """返回 catalog 目录中实际存在的分类文件名集合。"""
    catalog_dir = root / "catalog"
    if not catalog_dir.exists():
        return set()
    return {path.stem for path in catalog_dir.glob("*.md")}


def parse_catalog(root: Path) -> list[dict[str, Any]]:
    """从 catalog/*.md 中提取组件条目。"""
    catalog_dir = root / "catalog"
    entries: list[dict[str, Any]] = []

    if not catalog_dir.exists():
        return entries

    for path in sorted(catalog_dir.glob("*.md")):
        category = path.stem
        current: dict[str, Any] | None = None

        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()

            if line.startswith("## "):
                if current is not None:
                    entries.append(current)
                current = {
                    "name": line.removeprefix("## ").strip(),
                    "category": category,
                    "file": str(path.relative_to(root)).replace("\\", "/"),
                    "fields": {},
                }
                continue

            if current is None or not line.startswith("- "):
                continue

            # 只解析 "- 字段: 值" 格式，避免把普通列表误当成组件字段。
            field_text = line.removeprefix("- ")
            if ":" not in field_text:
                continue
            key, value = field_text.split(":", 1)
            current["fields"][key.strip()] = value.strip()

        if current is not None:
            entries.append(current)

    return entries


def validate_stack_presets(root: Path, stack_presets: dict[str, list[str]]) -> list[str]:
    """检查项目预设引用的分类是否都已经存在于 catalog 目录。"""
    errors: list[str] = []
    categories = catalog_categories(root)

    for preset_name, preset_categories in sorted(stack_presets.items()):
        for category in preset_categories:
            if category not in categories:
                errors.append(f"项目预设 {preset_name}: 引用了不存在的 catalog 分类 {category}。")

    return errors


def validate_repository(root: Path, stack_presets: dict[str, list[str]] | None = None) -> list[str]:
    """检查组件目录结构和每个条目的必填字段。"""
    errors: list[str] = []
    entries = parse_catalog(root)
    presets = STACK_PRESETS if stack_presets is None else stack_presets

    if not entries:
        errors.append("catalog 中没有找到任何组件条目。")
        return errors

    seen_names: set[str] = set()
    for entry in entries:
        name = entry["name"]
        fields = entry["fields"]
        location = f"{entry['file']} > {name}"

        if name in seen_names:
            errors.append(f"{location}: 组件名称重复。")
        seen_names.add(name)

        for field in REQUIRED_FIELDS:
            if not fields.get(field):
                errors.append(f"{location}: 缺少必填字段 {field}。")

        github = fields.get("GitHub", "")
        if github and not GITHUB_URL_RE.match(github):
            errors.append(f"{location}: GitHub 地址格式无效: {github}")

        cost = fields.get("接入成本", "")
        if cost and cost not in VALID_COSTS:
            errors.append(f"{location}: 接入成本必须是 低 / 中 / 高。")

        score = fields.get("评分", "")
        if score and not SCORE_RE.match(score):
            errors.append(f"{location}: 评分必须是 1/5 到 5/5。")

    errors.extend(validate_stack_presets(root, presets))
    return errors


def build_index(root: Path) -> dict[str, Any]:
    """把 Markdown 目录转换成便于程序读取的 JSON 数据。"""
    components = []
    for entry in parse_catalog(root):
        fields = entry["fields"]
        components.append(
            {
                "name": entry["name"],
                "category": entry["category"],
                "file": entry["file"],
                "github": fields.get("GitHub", ""),
                "website": fields.get("官网", ""),
                "module": fields.get("模块", ""),
                "tech_stack": fields.get("技术栈", ""),
                "license": fields.get("许可证", ""),
                "best_for": fields.get("适合", ""),
                "avoid_when": fields.get("不适合", ""),
                "integration_cost": fields.get("接入成本", ""),
                "alternatives": fields.get("替代方案", ""),
                "score": fields.get("评分", ""),
                "notes": fields.get("备注", ""),
            }
        )

    return {
        "component_count": len(components),
        "components": components,
    }


def write_index(root: Path, output: Path) -> None:
    """写入 catalog/index.json，供后续搜索页面或 CLI 使用。"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_index(root), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    """命令行入口：先校验，校验通过后可生成索引。"""
    parser = argparse.ArgumentParser(description="校验开源组件目录")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="仓库根目录")
    parser.add_argument(
        "--write-index",
        action="store_true",
        help="校验通过后写入 catalog/index.json",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    errors = validate_repository(root)

    if errors:
        print("组件目录校验失败：")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.write_index:
        output = root / "catalog" / "index.json"
        write_index(root, output)
        print(f"组件目录校验通过，已生成 {output}")
    else:
        print("组件目录校验通过。")

    return 0


if __name__ == "__main__":
    sys.exit(main())
