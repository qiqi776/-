"""集中维护项目拼装预设，供快速决策表和完整工作表共同使用。"""

from __future__ import annotations


# 每个预设是一组 catalog/index.json 中的英文分类名，用来描述常见项目的基础能力地图。
STACK_PRESETS = {
    "saas-starter": [
        "frontend",
        "backend",
        "auth",
        "database",
        "payment",
        "billing-invoicing",
        "analytics",
        "feature-flags",
        "deployment",
        "observability",
    ],
    "ai-rag-app": [
        "frontend",
        "backend",
        "model-serving-inference",
        "ai",
        "vector-database",
        "llm-guardrails-structured-output",
        "llm-observability-evaluation",
        "auth",
        "database",
        "deployment",
        "observability",
    ],
    "internal-admin": [
        "frontend",
        "internal-tools",
        "backend",
        "auth",
        "database",
        "deployment",
        "observability",
    ],
}


def format_presets() -> str:
    """生成命令行可读的项目预设清单，方便用户先查看再生成拼装草案。"""
    lines = [
        "可用项目预设:",
        "",
    ]
    for preset_name in sorted(STACK_PRESETS):
        modules = ", ".join(STACK_PRESETS[preset_name])
        lines.append(f"- {preset_name}: {modules}")
    return "\n".join(lines)
