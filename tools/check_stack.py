#!/usr/bin/env python3
"""检查一组候选组件在拼装成项目技术栈前的明显风险。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


# 这些许可证不一定不能用，但在分发、嵌入或商业化前必须重点审查义务。
REVIEW_LICENSE_KEYWORDS = ("AGPL", "GPL", "BUSL", "BSL", "SSPL", "ELASTIC", "商业许可证")


def load_components(path: Path) -> list[dict[str, Any]]:
    """读取 catalog/index.json 并返回组件列表。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("components", [])


def parse_component_names(raw_components: str) -> list[str]:
    """解析逗号分隔的组件名，并去掉空白项。"""
    return [component.strip() for component in raw_components.split(",") if component.strip()]


def component_names_from_stack_plan(path: Path) -> list[str]:
    """从技术栈 JSON 清单中提取已选主组件名称，供风险检查继续使用。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    names = []
    for module in data.get("modules", []):
        primary = module.get("primary")
        if not primary:
            continue
        name = str(primary.get("name", "")).strip()
        if name:
            names.append(name)
    return names


def index_components_by_name(components: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """按小写组件名建立索引，方便命令行输入做大小写不敏感匹配。"""
    return {str(component.get("name", "")).lower(): component for component in components}


def license_needs_review(license_text: str) -> bool:
    """判断许可证文本是否包含需要重点审查的关键词。"""
    normalized = license_text.upper()
    return any(keyword.upper() in normalized for keyword in REVIEW_LICENSE_KEYWORDS)


def analyze_component(component: dict[str, Any]) -> tuple[str, str]:
    """根据目录条目生成风险等级和风险提示。"""
    risk_notes = []
    license_text = str(component.get("license", ""))
    integration_cost = str(component.get("integration_cost", ""))

    if license_needs_review(license_text):
        risk_notes.append("许可证需要重点审查")
    if integration_cost == "高":
        risk_notes.append("接入成本高")

    avoid_when = str(component.get("avoid_when", "")).strip()
    if risk_notes and avoid_when:
        risk_notes.append(f"边界: {avoid_when}")

    if not risk_notes:
        return "低", "暂未发现明显目录风险"
    if license_needs_review(license_text) or integration_cost == "高":
        return "高", "；".join(risk_notes)
    return "中", "；".join(risk_notes)


def build_component_checks(
    components: list[dict[str, Any]],
    component_names: list[str],
) -> list[dict[str, Any]]:
    """按用户输入的组件名生成风险检查结果。"""
    by_name = index_components_by_name(components)
    checks = []

    for name in component_names:
        component = by_name.get(name.lower())
        if component is None:
            checks.append(
                {
                    "component": name,
                    "category": "",
                    "license": "",
                    "integration_cost": "",
                    "risk_level": "高",
                    "risk_notes": "目录中未找到该组件，需要先补录或确认名称。",
                }
            )
            continue

        risk_level, risk_notes = analyze_component(component)
        checks.append(
            {
                "component": component.get("name", name),
                "category": component.get("category", ""),
                "license": component.get("license", ""),
                "integration_cost": component.get("integration_cost", ""),
                "risk_level": risk_level,
                "risk_notes": risk_notes,
            }
        )

    return checks


def format_risk_table(checks: list[dict[str, Any]]) -> str:
    """把风险检查结果格式化成 Markdown 表格。"""
    lines = [
        "# 技术栈风险检查",
        "",
        "| 组件 | 分类 | 许可证 | 接入成本 | 风险等级 | 风险提示 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for check in checks:
        lines.append(
            "| {component} | {category} | {license} | {integration_cost} | {risk_level} | {risk_notes} |".format(
                component=check["component"],
                category=check["category"],
                license=check["license"],
                integration_cost=check["integration_cost"],
                risk_level=check["risk_level"],
                risk_notes=check["risk_notes"],
            )
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """命令行入口：读取索引并输出候选技术栈风险表。"""
    parser = argparse.ArgumentParser(description="检查候选技术栈组件风险")
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("catalog/index.json"),
        help="组件索引 JSON 文件路径",
    )
    parser.add_argument(
        "--components",
        default="",
        help="逗号分隔的组件名，例如 FastAPI,PostgreSQL,Grafana",
    )
    parser.add_argument(
        "--stack-plan",
        type=Path,
        help="assemble_stack.py --format json 生成的技术栈清单，默认检查其中的主组件。",
    )
    args = parser.parse_args(argv)

    components = load_components(args.index)
    component_names = parse_component_names(args.components)
    if args.stack_plan:
        component_names.extend(component_names_from_stack_plan(args.stack_plan))
    if not component_names:
        parser.error("必须提供 --components 或 --stack-plan。")
    checks = build_component_checks(components, component_names)
    print(format_risk_table(checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
