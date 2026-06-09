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
REVIEW_LICENSE_KEYWORDS = ("AGPL", "GPL", "BUSL", "BSL", "SSPL", "ELASTIC", "商业许可证")
MIN_MATURE_SCORE = 4
NON_OPEN_LICENSE_KEYWORDS = ("商业许可证", "SOURCE-AVAILABLE", "BUSL", "BSL", "SSPL", "ELASTIC")


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


def is_open_source_candidate(component: dict[str, Any]) -> bool:
    """判断组件是否具备开源候选的基础条件：有 GitHub 且许可证没有明显商业或非标准开放限制。"""
    return has_github_repo(component) and has_clear_open_source_license(component)


def component_sort_key(component: dict[str, Any]) -> tuple[int, int, int, str]:
    """排序规则：成熟开源优先，再按评分高、接入成本低和名称稳定排序。"""
    cost = COST_RANK.get(str(component.get("integration_cost", "")), 9)
    maturity_rank = 0 if is_mature_open_source(component) else 1
    return (maturity_rank, -score_value(component), cost, str(component.get("name", "")))


def select_for_category(
    components: list[dict[str, Any]],
    category: str,
    mature_only: bool = False,
) -> dict[str, Any]:
    """为单个模块选择主组件和备选组件。"""
    candidates = [component for component in components if component.get("category") == category]
    candidates = [component for component in candidates if is_open_source_candidate(component)]
    if mature_only:
        candidates = [component for component in candidates if is_mature_open_source(component)]
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
    mature_only: bool = False,
) -> list[dict[str, Any]]:
    """为多个模块生成技术栈决策草案。"""
    return [select_for_category(components, category, mature_only=mature_only) for category in categories]


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


def component_field(component: dict[str, Any] | None, field_name: str) -> str:
    """读取组件字段；缺失组件或字段为空时返回空字符串，便于表格稳定输出。"""
    if component is None:
        return ""
    return str(component.get(field_name, "")).strip()


def capability_label(decision: dict[str, Any]) -> str:
    """优先使用目录里的中文模块名；缺失时回退到英文分类名。"""
    primary = decision["primary"]
    if primary is None:
        return str(decision["category"])
    module = component_field(primary, "module")
    return module or str(decision["category"])


def license_needs_review(license_text: str) -> bool:
    """判断许可证文本是否包含需要人工重点审查的关键词。"""
    normalized = license_text.upper()
    return any(keyword.upper() in normalized for keyword in REVIEW_LICENSE_KEYWORDS)


def first_integration_action(component: dict[str, Any] | None) -> str:
    """根据许可证和接入成本给出项目接入时的第一个动作。"""
    if component is None:
        return "先补齐该模块候选组件"
    license_text = component_field(component, "license")
    integration_cost = component_field(component, "integration_cost")
    if license_needs_review(license_text) or integration_cost in {"中", "高"}:
        return "先确认许可证和部署方式，再跑通最小样例"
    return "先阅读快速开始并跑通最小样例"


def manifest_review_note(decision: dict[str, Any]) -> str:
    """生成项目组件清单中的待确认事项，提醒真实拼装前先处理边界风险。"""
    primary = decision["primary"]
    if primary is None:
        return "目录中暂未收录该模块组件。"

    notes = []
    license_text = component_field(primary, "license")
    integration_cost = component_field(primary, "integration_cost")
    avoid_when = component_field(primary, "avoid_when")

    if license_needs_review(license_text):
        notes.append("许可证需要重点审查")
    if integration_cost == "高":
        notes.append("接入成本高")
    if avoid_when:
        notes.append(avoid_when)
    elif notes:
        notes.append(str(decision["reason"]))

    return "；".join(notes) if notes else "按项目数据边界人工确认"


def component_summary(component: dict[str, Any] | None) -> dict[str, str] | None:
    """把组件压缩成技术栈清单需要的稳定字段，避免泄露多余目录细节。"""
    if component is None:
        return None
    return {
        "name": str(component.get("name", "")),
        "github": str(component.get("github", "")),
        "website": str(component.get("website", "")),
        "license": str(component.get("license", "")),
        "integration_cost": str(component.get("integration_cost", "")),
        "score": str(component.get("score", "")),
    }


def stack_decisions_payload(decisions: list[dict[str, Any]]) -> dict[str, Any]:
    """生成机器可读技术栈清单，供脚手架、模板或后续自动化读取。"""
    return {
        "module_count": len(decisions),
        "modules": [
            {
                "category": decision["category"],
                "primary": component_summary(decision["primary"]),
                "fallback": component_summary(decision["fallback"]),
                "reason": decision["reason"],
                "risk": decision["risk"],
            }
            for decision in decisions
        ],
    }


def format_stack_json(decisions: list[dict[str, Any]]) -> str:
    """把技术栈决策草案格式化成稳定 JSON，方便其他工具继续处理。"""
    return json.dumps(stack_decisions_payload(decisions), ensure_ascii=False, indent=2)


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


def format_component_manifest(decisions: list[dict[str, Any]]) -> str:
    """把技术栈决策渲染成可放进新项目仓库的组件清单。"""
    lines = [
        "# 项目组件清单",
        "",
        "这份清单由组件目录生成，适合放进新项目仓库追踪每个能力使用的开源组件。",
        "",
        "| 能力 | 主组件 | GitHub | 官网 | 许可证 | 接入成本 | 备选组件 | 首个动作 | 待确认事项 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for decision in decisions:
        primary = decision["primary"]
        lines.append(
            "| {capability} | {primary} | {github} | {website} | {license} | {cost} | {fallback} | {action} | {review_note} |".format(
                capability=capability_label(decision),
                primary=component_name(primary) or "待选组件",
                github=component_field(primary, "github"),
                website=component_field(primary, "website"),
                license=component_field(primary, "license"),
                cost=component_field(primary, "integration_cost"),
                fallback=component_name(decision["fallback"]),
                action=first_integration_action(primary),
                review_note=manifest_review_note(decision),
            )
        )
    return "\n".join(lines)


def render_stack_decisions(decisions: list[dict[str, Any]], output_format: str) -> str:
    """按用户选择的格式渲染技术栈清单。"""
    if output_format == "json":
        return format_stack_json(decisions)
    if output_format == "manifest":
        return format_component_manifest(decisions)
    return format_stack_table(decisions)


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
    parser.add_argument(
        "--format",
        choices=("markdown", "json", "manifest"),
        default="markdown",
        help="输出格式：markdown 适合人工阅读，json 适合自动化处理，manifest 适合放进新项目仓库追踪组件。",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="把技术栈清单写入指定文件；不提供时输出到终端。",
    )
    parser.add_argument(
        "--mature-only",
        action="store_true",
        help="只从有 GitHub、许可证清楚且评分不低于 4/5 的成熟开源候选中选择组件。",
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
    decisions = build_stack_decisions(components, modules, mature_only=args.mature_only)
    output_text = render_stack_decisions(decisions, args.format)
    if args.output:
        args.output.write_text(output_text + "\n", encoding="utf-8")
        print(f"已生成技术栈清单: {args.output}")
    else:
        print(output_text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
