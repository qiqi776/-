#!/usr/bin/env python3
"""根据模块列表生成可直接复制到项目仓库的拼装工作表。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


COST_RANK = {"低": 0, "中": 1, "高": 2}
REVIEW_LICENSE_KEYWORDS = ("AGPL", "GPL", "BUSL", "BSL", "SSPL", "ELASTIC", "商业许可证")


def load_components(path: Path) -> list[dict[str, Any]]:
    """读取 catalog/index.json 并返回组件列表。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("components", [])


def parse_modules(raw_modules: str) -> list[str]:
    """解析逗号分隔的模块列表，并去掉空白项。"""
    return [module.strip() for module in raw_modules.split(",") if module.strip()]


def score_value(component: dict[str, Any]) -> int:
    """把 4/5 这类评分转换成整数，无法解析时按 0 分处理。"""
    raw_score = str(component.get("score", "0/5"))
    try:
        return int(raw_score.split("/", 1)[0])
    except ValueError:
        return 0


def component_sort_key(component: dict[str, Any]) -> tuple[int, int, str]:
    """排序规则与组合生成器保持一致：评分高优先，接入成本低优先。"""
    cost = COST_RANK.get(str(component.get("integration_cost", "")), 9)
    return (-score_value(component), cost, str(component.get("name", "")))


def select_for_category(components: list[dict[str, Any]], category: str) -> dict[str, Any]:
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


def component_name(component: dict[str, Any] | None) -> str:
    """返回组件名称；缺失时返回空字符串，方便 Markdown 表格显示。"""
    if component is None:
        return ""
    return str(component.get("name", ""))


def license_needs_review(license_text: str) -> bool:
    """判断许可证文本是否包含需要重点审查的关键词。"""
    normalized = license_text.upper()
    return any(keyword.upper() in normalized for keyword in REVIEW_LICENSE_KEYWORDS)


def risk_note_for_component(component: dict[str, Any]) -> str:
    """为许可证检查表生成简短风险说明。"""
    notes = []
    license_text = str(component.get("license", ""))
    integration_cost = str(component.get("integration_cost", ""))

    if license_needs_review(license_text):
        notes.append("许可证需要重点审查")
    if integration_cost == "高":
        notes.append("接入成本高")

    avoid_when = str(component.get("avoid_when", "")).strip()
    if avoid_when:
        notes.append(f"边界: {avoid_when}")

    return "；".join(notes) if notes else "暂未发现明显目录风险"


def acceptance_for_component(component: dict[str, Any]) -> str:
    """根据许可证和接入成本给出默认人工确认状态。"""
    license_text = str(component.get("license", ""))
    integration_cost = str(component.get("integration_cost", ""))
    if license_needs_review(license_text) or integration_cost == "高":
        return "待确认"
    return "是"


def selected_components(decisions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """提取主组件并去重，用于生成许可证检查表。"""
    result = []
    seen = set()
    for decision in decisions:
        primary = decision["primary"]
        if primary is None:
            continue
        name = component_name(primary)
        if name in seen:
            continue
        seen.add(name)
        result.append(primary)
    return result


def format_capability_map(decisions: list[dict[str, Any]]) -> str:
    """生成已填好主组件和风险的能力地图表。"""
    lines = [
        "## 能力地图",
        "",
        "| 能力 | 是否需要 | 主组件 | 备选组件 | 选择理由 | 主要风险 | 验证方式 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for decision in decisions:
        lines.append(
            "| {category} | 是 | {primary} | {fallback} | {reason} | {risk} | 先做最小集成验证 |".format(
                category=decision["category"],
                primary=component_name(decision["primary"]),
                fallback=component_name(decision["fallback"]),
                reason=decision["reason"],
                risk=decision["risk"],
            )
        )
    return "\n".join(lines)


def format_license_table(components: list[dict[str, Any]]) -> str:
    """生成主组件许可证检查表。"""
    lines = [
        "## 许可证检查",
        "",
        "| 组件 | 许可证 | 是否可接受 | 需要确认的问题 |",
        "| --- | --- | --- | --- |",
    ]
    if not components:
        lines.append("|  |  | 待确认 | 需要先选择主组件。 |")
        return "\n".join(lines)

    for component in components:
        lines.append(
            "| {name} | {license} | {acceptance} | {risk_notes} |".format(
                name=component_name(component),
                license=component.get("license", ""),
                acceptance=acceptance_for_component(component),
                risk_notes=risk_note_for_component(component),
            )
        )
    return "\n".join(lines)


def format_validation_table(decisions: list[dict[str, Any]]) -> str:
    """生成优先验证的集成表，默认按输入模块顺序排序。"""
    lines = [
        "## 优先验证的集成",
        "",
        "先验证最容易影响项目成败的模块，而不是先做最容易展示的页面。",
        "",
        "| 优先级 | 集成项 | 为什么风险高 | 最小验证方式 | 通过标准 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for index, decision in enumerate(decisions, start=1):
        primary_name = component_name(decision["primary"]) or "待选组件"
        lines.append(
            "| {index} | {category} / {primary} | {risk} | 跑通最小配置、认证、数据读写或部署路径 | 能稳定复现并记录失败回退方案 |".format(
                index=index,
                category=decision["category"],
                primary=primary_name,
                risk=decision["risk"],
            )
        )
    return "\n".join(lines)


def format_final_decision(decisions: list[dict[str, Any]]) -> str:
    """生成最终技术栈决策草案，后续可人工精简后放进项目 README。"""
    lines = [
        "## 最终技术栈决策",
        "",
        "```md",
        "# 技术栈决策",
        "",
    ]
    for decision in decisions:
        lines.append(f"- {decision['category']}: {component_name(decision['primary'])}")
    lines.extend(
        [
            "",
            "## 关键取舍",
            "",
            "1. 先确认许可证、数据边界和托管方式。",
            "2. 先验证风险最高的集成，再扩展完整功能。",
            "3. 组件替换必须同步更新能力地图和风险检查。",
            "```",
        ]
    )
    return "\n".join(lines)


def build_worksheet(
    components: list[dict[str, Any]],
    categories: list[str],
    project_name: str,
) -> str:
    """生成完整项目拼装工作表。"""
    decisions = [select_for_category(components, category) for category in categories]
    primary_components = selected_components(decisions)
    sections = [
        "# 项目拼装工作表",
        "",
        "这份工作表由组件目录生成，适合作为新项目技术栈选型的第一版草案。",
        "",
        "## 项目概况",
        "",
        f"- 项目名称: {project_name}",
        "- 项目类型:",
        "- 目标用户:",
        "- 首个可交付版本:",
        "- 必须自托管: 是 / 否",
        "- 主要语言偏好:",
        "- 许可证限制:",
        "",
        format_capability_map(decisions),
        "",
        format_license_table(primary_components),
        "",
        "## 数据与身份边界",
        "",
        "- 用户身份由哪个组件管理:",
        "- 业务主数据库:",
        "- 文件和媒体存储位置:",
        "- 日志、指标和追踪数据位置:",
        "- 是否需要数据迁移预案:",
        "",
        format_validation_table(decisions),
        "",
        format_final_decision(decisions),
    ]
    return "\n".join(sections) + "\n"


def main(argv: list[str] | None = None) -> int:
    """命令行入口：读取索引并写出项目拼装工作表。"""
    parser = argparse.ArgumentParser(description="生成项目拼装工作表")
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("catalog/index.json"),
        help="组件索引 JSON 文件路径",
    )
    parser.add_argument(
        "--modules",
        required=True,
        help="逗号分隔的模块分类，例如 frontend,backend,auth,database",
    )
    parser.add_argument("--project-name", default="", help="项目名称，会写入工作表项目概况")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("stack-selection.md"),
        help="输出工作表路径",
    )
    args = parser.parse_args(argv)

    components = load_components(args.index)
    worksheet = build_worksheet(components, parse_modules(args.modules), args.project_name)
    args.output.write_text(worksheet, encoding="utf-8")
    print(f"已生成项目拼装工作表: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
