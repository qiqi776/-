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

STACK_PRESET_DETAILS = {
    "saas-starter": {
        "name": "SaaS 起步项目",
        "best_for": "适合需要账号、计费、数据分析、功能开关和可观测性的订阅型产品。",
    },
    "ai-rag-app": {
        "name": "AI RAG 应用",
        "best_for": "适合需要模型接入、检索增强、向量数据库、LLM 护栏和评估闭环的 AI 产品。",
    },
    "internal-admin": {
        "name": "内部管理后台",
        "best_for": "适合需要管理 UI、内部工具、身份、数据库、部署和监控的运营或管理系统。",
    },
}


def format_presets() -> str:
    """生成命令行可读的项目预设清单，方便用户先查看再生成拼装草案。"""
    lines = [
        "可用项目预设:",
        "",
    ]
    for preset_name in sorted(STACK_PRESETS):
        details = STACK_PRESET_DETAILS[preset_name]
        modules = ", ".join(STACK_PRESETS[preset_name])
        lines.append(f"- {preset_name}（{details['name']}）")
        lines.append(f"  - 适合: {details['best_for']}")
        lines.append(f"  - 模块: {modules}")
    return "\n".join(lines)
