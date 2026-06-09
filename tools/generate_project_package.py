#!/usr/bin/env python3
"""一次性生成项目拼装包，包含选型 JSON、组件清单、风险报告、实施计划、架构图、执行清单、Issue 草案、标签配置、导入命令、Issue 模板、配置样例和项目 README 草案。"""

from __future__ import annotations

import argparse
import json
import re
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
EDGE_TARGETS = {
    "frontend": ["backend", "auth", "analytics"],
    "internal-tools": ["backend", "auth"],
    "backend": [
        "auth",
        "database",
        "payment",
        "billing-invoicing",
        "feature-flags",
        "ai",
        "model-serving-inference",
        "vector-database",
        "deployment",
        "observability",
    ],
    "ai": ["model-serving-inference", "vector-database", "llm-guardrails-structured-output"],
    "model-serving-inference": ["llm-observability-evaluation"],
    "deployment": ["observability"],
}


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


def architecture_node_label(decision: dict | None) -> str:
    """生成架构图节点名称，优先展示能力中文名和已选主组件。"""
    if decision is None:
        return ""
    primary = decision["primary"]
    primary_name = component_name(primary)
    if primary_name:
        return f"{capability_label(decision)} / {primary_name}"
    return f"{capability_label(decision)} / 待选组件"


def architecture_edges(decisions: list[dict]) -> list[tuple[str, str, str]]:
    """根据常见项目数据流生成组件连接，帮助用户理解各模块如何拼装。"""
    decisions_by_category = {str(decision["category"]): decision for decision in decisions}
    edges: list[tuple[str, str, str]] = []

    def add_edge(source_label: str, target_decision: dict | None, purpose: str) -> None:
        """只在目标模块存在时添加连接，避免架构图出现无效节点。"""
        target_label = architecture_node_label(target_decision)
        if target_label:
            edges.append((source_label, target_label, purpose))

    entry_candidates = [category for category in ("frontend", "internal-tools") if category in decisions_by_category]
    backend_decision = decisions_by_category.get("backend")
    if backend_decision:
        if entry_candidates:
            for category in entry_candidates:
                add_edge("前端/客户端", backend_decision, "用户请求进入后端 API")
        else:
            add_edge("前端/客户端", backend_decision, "外部客户端调用后端 API")

    for source_category, target_categories in EDGE_TARGETS.items():
        source_decision = decisions_by_category.get(source_category)
        if not source_decision:
            continue
        source_label = architecture_node_label(source_decision)
        for target_category in target_categories:
            target_decision = decisions_by_category.get(target_category)
            if not target_decision:
                continue
            target_label = architecture_node_label(target_decision)
            if source_label == target_label:
                continue
            purpose = "模块间集成依赖"
            if source_category == "backend":
                purpose = "后端调用该能力完成业务闭环"
            elif source_category == "frontend":
                purpose = "前端直接接入该能力"
            elif source_category == "deployment":
                purpose = "部署后接入监控与告警"
            edges.append((source_label, target_label, purpose))

    unique_edges = []
    seen = set()
    for edge in edges:
        key = (edge[0], edge[1])
        if key in seen:
            continue
        seen.add(key)
        unique_edges.append(edge)
    return unique_edges


def mermaid_node_id(index: int) -> str:
    """生成 Mermaid 可用的稳定节点 ID，避免中文和符号影响渲染。"""
    return f"n{index}"


def format_architecture_map(decisions: list[dict]) -> str:
    """生成组件架构图和连接说明，帮助新项目按模块落地集成关系。"""
    edges = architecture_edges(decisions)
    labels = []
    for source, target, _purpose in edges:
        labels.extend([source, target])
    if not labels:
        labels = [architecture_node_label(decision) for decision in decisions if architecture_node_label(decision)]

    unique_labels = []
    for label in labels:
        if label not in unique_labels:
            unique_labels.append(label)
    node_ids = {label: mermaid_node_id(index) for index, label in enumerate(unique_labels, start=1)}

    lines = [
        "# 组件架构图",
        "",
        "这份图根据已选模块生成，用来说明新项目里各组件的默认连接方向。真实项目可以按业务边界删减或调整。",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    for label in unique_labels:
        lines.append(f'  {node_ids[label]}["{label}"]')
    for source, target, _purpose in edges:
        lines.append(f"  {node_ids[source]} --> {node_ids[target]}")
    lines.extend(
        [
            "```",
            "",
            "## 连接清单",
            "",
        ]
    )
    if edges:
        for source, target, _purpose in edges:
            lines.append(f"- {source} --> {target}")
    else:
        lines.append("- 当前模块之间没有生成默认连接，请按项目业务手动补充。")

    lines.extend(
        [
            "",
            "## 连接说明",
            "",
            "| 来源 | 目标 | 说明 |",
            "| --- | --- | --- |",
        ]
    )
    if edges:
        for source, target, purpose in edges:
            lines.append(f"| {source} | {target} | {purpose} |")
    else:
        lines.append("| 待补充 | 待补充 | 当前模块组合缺少可推断的默认连接。 |")
    return "\n".join(lines)


def format_assembly_checklist(decisions: list[dict]) -> str:
    """生成可复制到项目看板或 Issue 的拼装执行清单。"""
    lines = [
        "# 项目拼装执行清单",
        "",
        "按实施风险排序，把每个组件拆成可分配、可验收的落地任务。",
        "",
    ]
    for index, decision in enumerate(sorted(decisions, key=integration_priority_key), start=1):
        primary = decision["primary"]
        component_label = f"{capability_label(decision)} / {component_name(primary) or '待选组件'}"
        lines.extend(
            [
                f"## {index}. {component_label}",
                "",
                f"- [ ] 负责人:",
                "- [ ] 状态: 未开始 / 进行中 / 已验证 / 暂缓",
                f"- [ ] 风险确认: {integration_risk_reason(decision)}",
                f"- [ ] {first_integration_action(primary)}",
                "- [ ] 跑通最小样例并记录命令、配置和截图或日志",
                "- [ ] 写下失败回退方案和替代组件触发条件",
                "- [ ] 更新项目 README、环境变量示例和组件清单",
                "",
            ]
        )
    lines.extend(
        [
            "## 完成判定",
            "",
            "- [ ] 所有必须模块至少跑通最小样例。",
            "- [ ] 高风险许可证、托管方式和数据边界已经有人签字确认。",
            "- [ ] `component-manifest.md`、`risk-check.md` 和项目 README 已同步。",
        ]
    )
    return "\n".join(lines)


def issue_risk_label(decision: dict) -> str:
    """按组件风险生成 GitHub Issue 标签，方便在看板里优先处理高风险集成。"""
    primary = decision["primary"]
    if not primary:
        return "risk-high"

    license_text = str(primary.get("license", ""))
    integration_cost = str(primary.get("integration_cost", ""))
    if license_needs_review(license_text) or integration_cost == "高":
        return "risk-high"
    if integration_cost == "中":
        return "risk-medium"
    return "risk-low"


def format_issue_labels(decision: dict) -> str:
    """生成可复制到 GitHub Issue 的标签列表，保留组件分类和风险等级。"""
    labels = ["component", "integration", str(decision["category"]), issue_risk_label(decision)]
    return ", ".join(f"`{label}`" for label in labels)


def format_github_issues(decisions: list[dict]) -> str:
    """生成 GitHub Issue 草案，把每个组件接入拆成可复制的跟踪任务。"""
    lines = [
        "# GitHub Issue 草案",
        "",
        "把下面每个区块复制成目标项目仓库中的一个 GitHub Issue，用于跟踪组件接入。Issue 已按风险优先级排序。",
        "",
    ]
    for index, decision in enumerate(sorted(decisions, key=integration_priority_key), start=1):
        primary = decision["primary"]
        component_label = f"{capability_label(decision)} / {component_name(primary) or '待选组件'}"
        lines.extend(
            [
                f"## Issue {index}: 接入 {component_label}",
                "",
                f"标题: 接入 {component_label}",
                f"标签: {format_issue_labels(decision)}",
                "负责人:",
                "里程碑:",
                "",
                "### 背景",
                "",
                f"- 能力: {capability_label(decision)}",
                f"- 主组件: {component_name(primary) or '待选组件'}",
                f"- 备选组件: {component_name(decision['fallback']) or '待补充'}",
                f"- 风险原因: {integration_risk_reason(decision)}",
                f"- 首个动作: {first_integration_action(primary)}",
                "",
                "### 执行清单",
                "",
                f"- [ ] {first_integration_action(primary)}",
                "- [ ] 跑通最小样例并记录命令、配置、截图或日志",
                "- [ ] 确认环境变量、部署地址、数据边界和回退方案",
                "- [ ] 更新 `component-manifest.md`、`risk-check.md` 和 `PROJECT-README.md`",
                "",
                "### 验收标准",
                "",
                "- [ ] 最小样例可重复运行",
                "- [ ] 关键配置已记录到 `.env.example` 或部署平台说明",
                "- [ ] 替代组件触发条件已写入组件清单",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def github_label_payload(name: str, color: str, description: str) -> dict[str, str]:
    """生成 GitHub Label 配置项，字段名对齐 GitHub API 和常见 label 同步工具。"""
    return {
        "name": name,
        "color": color,
        "description": description,
    }


def build_github_labels(decisions: list[dict]) -> list[dict[str, str]]:
    """生成目标项目所需的 GitHub Labels 列表，供 JSON 配置和导入命令共用。"""
    labels = [
        github_label_payload("component", "5319e7", "组件接入或替换相关任务。"),
        github_label_payload("integration", "0e8a16", "需要跑通组件最小集成的任务。"),
        github_label_payload("risk-high", "d73a4a", "高风险集成，优先确认许可证、托管方式或接入成本。"),
        github_label_payload("risk-medium", "fbca04", "中等风险集成，需要在开发前明确边界。"),
        github_label_payload("risk-low", "0e8a16", "低风险集成，按常规最小样例验证。"),
    ]
    existing_names = {label["name"] for label in labels}

    for decision in decisions:
        category = str(decision["category"])
        if category in existing_names:
            continue
        labels.append(
            github_label_payload(
                category,
                "1d76db",
                f"{capability_label(decision)} 模块相关的组件接入任务。",
            )
        )
        existing_names.add(category)

    return labels


def format_github_labels(decisions: list[dict]) -> str:
    """生成目标项目可导入的 GitHub Labels 配置，匹配 Issue 草案里的标签。"""
    labels = build_github_labels(decisions)
    return json.dumps(labels, ensure_ascii=False, indent=2)


def shell_double_quote(text: str) -> str:
    """转义命令参数中的双引号，避免生成的 gh 命令被标题或说明截断。"""
    return str(text).replace('"', '\\"')


def issue_label_csv(decision: dict) -> str:
    """生成 gh issue create 可直接使用的逗号分隔标签值。"""
    return ",".join(["component", "integration", str(decision["category"]), issue_risk_label(decision)])


def issue_body_text(decision: dict) -> str:
    """生成 GitHub Issue 命令中的简短正文，保留首个动作和验收重点。"""
    primary = decision["primary"]
    return (
        f"能力: {capability_label(decision)}\\n"
        f"主组件: {component_name(primary) or '待选组件'}\\n"
        f"备选组件: {component_name(decision['fallback']) or '待补充'}\\n"
        f"风险原因: {integration_risk_reason(decision)}\\n"
        f"首个动作: {first_integration_action(primary)}\\n\\n"
        "执行清单:\\n"
        f"- [ ] {first_integration_action(primary)}\\n"
        "- [ ] 跑通最小样例并记录命令、配置、截图或日志\\n"
        "- [ ] 确认环境变量、部署地址、数据边界和回退方案\\n"
        "- [ ] 更新 component-manifest.md、risk-check.md 和 PROJECT-README.md"
    )


def format_github_import_commands(decisions: list[dict]) -> str:
    """生成可复制执行的 GitHub CLI 命令清单，但不直接访问或修改 GitHub。"""
    lines = [
        "# GitHub 导入命令清单",
        "",
        "下面命令用于在目标项目仓库中创建组件接入标签和 Issue。请先安装并登录 GitHub CLI，然后在目标仓库根目录按需复制执行。",
        "",
        "## 创建标签",
        "",
        "```powershell",
    ]
    for label in build_github_labels(decisions):
        lines.append(
            'gh label create "{name}" --color "{color}" --description "{description}"'.format(
                name=shell_double_quote(label["name"]),
                color=shell_double_quote(label["color"]),
                description=shell_double_quote(label["description"]),
            )
        )

    lines.extend(
        [
            "```",
            "",
            "## 创建组件接入 Issue",
            "",
            "```powershell",
        ]
    )
    for decision in sorted(decisions, key=integration_priority_key):
        primary = decision["primary"]
        title = f"接入 {capability_label(decision)} / {component_name(primary) or '待选组件'}"
        lines.append(
            'gh issue create --title "{title}" --label "{labels}" --body "{body}"'.format(
                title=shell_double_quote(title),
                labels=shell_double_quote(issue_label_csv(decision)),
                body=shell_double_quote(issue_body_text(decision)),
            )
        )
    lines.append("```")
    return "\n".join(lines)


def format_github_issue_template() -> str:
    """生成目标项目可放入 .github/ISSUE_TEMPLATE 的组件接入表单模板。"""
    lines = [
        "name: 组件接入任务",
        'description: 用于跟踪一个开源组件从选型到最小集成验证的过程。',
        'title: "接入 [能力] / [组件]"',
        "labels: [component, integration]",
        "body:",
        "  - type: input",
        "    id: capability",
        "    attributes:",
        "      label: 组件能力",
        "      description: 例如 后端 / API、认证 / IAM、数据库 / 关系型数据库。",
        "      placeholder: 后端 / API",
        "    validations:",
        "      required: true",
        "  - type: input",
        "    id: primary_component",
        "    attributes:",
        "      label: 主组件",
        "      description: 当前计划接入的开源组件名称。",
        "      placeholder: FastAPI",
        "    validations:",
        "      required: true",
        "  - type: input",
        "    id: fallback_component",
        "    attributes:",
        "      label: 备选组件",
        "      description: 主组件不适合时的替代方案。",
        "      placeholder: NestJS",
        "  - type: dropdown",
        "    id: risk_level",
        "    attributes:",
        "      label: 风险等级",
        "      description: 根据许可证、接入成本、托管方式和数据边界选择。",
        "      options:",
        "        - risk-high",
        "        - risk-medium",
        "        - risk-low",
        "    validations:",
        "      required: true",
        "  - type: textarea",
        "    id: first_action",
        "    attributes:",
        "      label: 首个动作",
        "      description: 写下最小集成验证的第一步。",
        "      placeholder: 先确认许可证和部署方式，再跑通最小样例",
        "    validations:",
        "      required: true",
        "  - type: textarea",
        "    id: acceptance",
        "    attributes:",
        "      label: 验收标准",
        "      description: 说明这个组件接入任务怎样算完成。",
        "      value: |",
        "        - [ ] 最小样例可重复运行",
        "        - [ ] 关键配置已记录到 .env.example 或部署平台说明",
        "        - [ ] 替代组件触发条件已写入组件清单",
        "    validations:",
        "      required: true",
    ]
    return "\n".join(lines)


def format_github_pr_template() -> str:
    """生成目标项目可放入 .github 的组件接入 Pull Request 模板。"""
    lines = [
        "# 组件接入 Pull Request 模板",
        "",
        "## 关联组件 Issue",
        "",
        "- 关联 Issue:",
        "- 能力:",
        "- 主组件:",
        "- 备选组件:",
        "",
        "## 变更范围",
        "",
        "- [ ] 新增或替换开源组件",
        "- [ ] 更新配置、环境变量或部署说明",
        "- [ ] 更新组件清单、风险检查或项目 README",
        "",
        "## 最小样例验证",
        "",
        "- [ ] 已跑通最小样例，并记录可重复执行的命令",
        "- 验证命令:",
        "- 关键日志、截图或输出:",
        "",
        "## 同步检查",
        "",
        "- [ ] 更新 `component-manifest.md`",
        "- [ ] 更新 `risk-check.md`",
        "- [ ] 更新 `.env.example` 或部署平台变量说明",
        "- [ ] 更新 `PROJECT-README.md`",
        "",
        "## 风险与回退",
        "",
        "- 风险等级:",
        "- 回退方案:",
        "- 切换到备选组件的触发条件:",
    ]
    return "\n".join(lines)


def env_key_part(raw_text: str, fallback: str) -> str:
    """把模块名或组件名转换成适合环境变量使用的英文大写片段。"""
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", raw_text).strip("_").upper()
    return normalized or fallback.upper()


def env_prefix(decision: dict) -> str:
    """生成单个组件的环境变量前缀，优先使用分类名和组件名。"""
    primary = decision["primary"]
    category_part = env_key_part(str(decision["category"]), "MODULE")
    component_part = env_key_part(component_name(primary), "COMPONENT")
    return f"{category_part}_{component_part}"


def format_env_example(decisions: list[dict], project_name: str) -> str:
    """生成新项目可复制的环境变量样例，提醒用户只填占位不提交真实密钥。"""
    title = project_name or "未命名项目"
    lines = [
        f"# {title} 环境变量样例",
        "# 不要在这个文件里填写真实密钥；复制为 .env.local 或部署平台变量后再填真实值。",
        "# 每个变量按已选主组件生成，真实项目可按框架约定删减或改名。",
        "",
    ]
    for decision in sorted(decisions, key=integration_priority_key):
        primary = decision["primary"]
        prefix = env_prefix(decision)
        lines.extend(
            [
                f"# {capability_label(decision)} / {component_name(primary) or '待选组件'}",
                f"# 风险: {integration_risk_reason(decision)}",
                f"{prefix}_ENABLED=false",
                f"{prefix}_URL=",
                f"{prefix}_API_KEY=",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def format_project_readme(decisions: list[dict], project_name: str) -> str:
    """生成可放进目标项目仓库的 README 草案，集中记录组件拼装决策。"""
    title = project_name or "未命名项目"
    lines = [
        f"# {title}",
        "",
        "这个 README 由开源组件库生成，作为项目技术栈和组件拼装记录的第一版草案。",
        "",
        "## 技术栈总览",
        "",
        "| 能力 | 主组件 | 备选组件 | 选择理由 | 主要风险 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for decision in decisions:
        lines.append(
            "| {capability} | {primary} | {fallback} | {reason} | {risk} |".format(
                capability=capability_label(decision),
                primary=component_name(decision["primary"]) or "待选组件",
                fallback=component_name(decision["fallback"]),
                reason=decision["reason"],
                risk=decision["risk"],
            )
        )

    lines.extend(
        [
            "",
            "## 优先集成顺序",
            "",
        ]
    )
    for index, decision in enumerate(sorted(decisions, key=integration_priority_key), start=1):
        primary = decision["primary"]
        lines.append(f"{index}. {capability_label(decision)} / {component_name(primary) or '待选组件'}")

    lines.extend(
        [
            "",
            "## 配置与环境变量",
            "",
            "从 `.env.example` 复制一份本地或部署环境变量文件，再填入真实地址和密钥。不要把真实密钥提交到仓库。",
            "",
            "## 组件追踪文件",
            "",
            "- [component-manifest.md](component-manifest.md): 记录每个能力的主组件、链接、首个动作和待确认事项。",
            "- [risk-check.md](risk-check.md): 记录许可证、接入成本和缺失组件风险。",
            "- [integration-plan.md](integration-plan.md): 记录先验证哪些关键集成。",
            "- [architecture-map.md](architecture-map.md): 记录组件连接方向。",
            "- [assembly-checklist.md](assembly-checklist.md): 记录可拆到看板或 Issue 的执行任务。",
            "",
            "## 维护规则",
            "",
            "1. 替换组件时同步更新组件清单、风险检查和环境变量样例。",
            "2. 高风险许可证、托管方式和数据边界必须先确认再进入生产。",
            "3. 每次新增模块都先跑通最小样例，再扩展完整功能。",
        ]
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
        "- `architecture-map.md`: 根据已选模块生成的组件连接图，用于理解各组件如何拼装。",
        "- `assembly-checklist.md`: 可复制到项目看板或 GitHub Issue 的拼装执行清单。",
        "- `github-issues.md`: 可复制到 GitHub Issues 的组件接入任务草案。",
        "- `github-labels.json`: 与 Issue 草案匹配的 GitHub Labels 配置。",
        "- `github-import-commands.md`: 可复制执行的 GitHub CLI 标签和 Issue 创建命令。",
        "- `github-issue-template.yml`: 可放入 `.github/ISSUE_TEMPLATE/` 的组件接入表单模板。",
        "- `github-pr-template.md`: 可放入 `.github/pull_request_template.md` 的组件接入 PR 模板。",
        "- `.env.example`: 按已选组件生成的环境变量样例，提醒不要提交真实密钥。",
        "- `PROJECT-README.md`: 可放入目标项目仓库的 README 草案，用于记录技术栈和维护规则。",
        "",
        "## 使用建议",
        "",
        "1. 先阅读 `risk-check.md`，处理高风险许可证和高接入成本组件。",
        "2. 查看 `architecture-map.md`，确认组件之间的连接方向是否符合项目边界。",
        "3. 按 `integration-plan.md` 的顺序跑通最小集成，先验证最可能影响项目落地的模块。",
        "4. 把 `assembly-checklist.md` 拆到项目看板或 Issue，逐项分配负责人和验收结果。",
        "5. 把 `github-issues.md` 中的区块复制成 GitHub Issues，按风险标签推进接入。",
        "6. 按 `github-labels.json` 在目标仓库建立标签，让组件任务能按分类和风险筛选。",
        "7. 需要批量创建时，参考 `github-import-commands.md` 在目标仓库执行 GitHub CLI 命令。",
        "8. 把 `github-issue-template.yml` 复制到目标仓库 `.github/ISSUE_TEMPLATE/component-integration.yml`，统一后续组件接入表单。",
        "9. 把 `github-pr-template.md` 复制到目标仓库 `.github/pull_request_template.md`，统一组件接入 PR 检查项。",
        "10. 复制 `.env.example` 到新项目，按实际组件填写部署地址和密钥变量。",
        "11. 参考 `PROJECT-README.md` 初始化目标项目 README，保留技术栈取舍记录。",
        "12. 把 `component-manifest.md` 放进新项目仓库，作为后续集成和替换组件的追踪清单。",
        "13. 保留 `stack-plan.json`，让模板、脚手架或其他自动化工具继续消费。",
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
        "architecture-map.md": format_architecture_map(decisions) + "\n",
        "assembly-checklist.md": format_assembly_checklist(decisions) + "\n",
        "github-issues.md": format_github_issues(decisions) + "\n",
        "github-labels.json": format_github_labels(decisions) + "\n",
        "github-import-commands.md": format_github_import_commands(decisions) + "\n",
        "github-issue-template.yml": format_github_issue_template() + "\n",
        "github-pr-template.md": format_github_pr_template() + "\n",
        ".env.example": format_env_example(decisions, project_name) + "\n",
        "PROJECT-README.md": format_project_readme(decisions, project_name) + "\n",
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
