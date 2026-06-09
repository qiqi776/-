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

# 常用中文项目类型别名，方便命令行直接按业务语境选择项目蓝图。
PRESET_ALIASES = {
    "SaaS 起步项目": "saas-starter",
    "SaaS起步项目": "saas-starter",
    "SaaS": "saas-starter",
    "订阅型产品": "saas-starter",
    "AI RAG 应用": "ai-rag-app",
    "AI RAG应用": "ai-rag-app",
    "RAG 应用": "ai-rag-app",
    "RAG应用": "ai-rag-app",
    "AI 应用": "ai-rag-app",
    "AI应用": "ai-rag-app",
    "内部管理后台": "internal-admin",
    "内部后台": "internal-admin",
    "管理后台": "internal-admin",
    "运营后台": "internal-admin",
}

MODULE_ALIASES = {
    "前端": "frontend",
    "后端": "backend",
    "认证": "auth",
    "登录": "auth",
    "数据库": "database",
    "支付": "payment",
    "账单": "billing-invoicing",
    "发票": "billing-invoicing",
    "部署": "deployment",
    "监控": "observability",
    "可观测性": "observability",
    "内部工具": "internal-tools",
    "管理后台": "internal-tools",
    "AI": "ai",
    "模型服务": "model-serving-inference",
    "向量数据库": "vector-database",
    "LLM护栏": "llm-guardrails-structured-output",
    "LLM 护栏": "llm-guardrails-structured-output",
    "LLM评估": "llm-observability-evaluation",
    "LLM 评估": "llm-observability-evaluation",
}


def normalize_preset_name(preset: str | None) -> str | None:
    """把中文项目类型或英文预设 slug 统一成内置预设键名。"""
    if preset is None:
        return None
    stripped = preset.strip()
    return PRESET_ALIASES.get(stripped, stripped)


def preset_exists(preset: str | None) -> bool:
    """判断预设名或中文别名是否能对应到内置项目蓝图。"""
    normalized_preset = normalize_preset_name(preset)
    return bool(normalized_preset and normalized_preset in STACK_PRESETS)


def normalize_module_name(module: str) -> str:
    """把常用中文模块名转换成 catalog 分类 slug；未知项保持原样。"""
    stripped = module.strip()
    return MODULE_ALIASES.get(stripped, stripped)


def parse_modules(raw_modules: str) -> list[str]:
    """解析逗号分隔模块列表，同时支持常用中文模块名别名。"""
    return [normalize_module_name(module) for module in raw_modules.split(",") if module.strip()]


def resolve_modules(raw_modules: str, preset: str | None) -> list[str]:
    """根据显式模块或内置项目预设得到最终模块列表。"""
    modules = parse_modules(raw_modules)
    if modules:
        return modules
    normalized_preset = normalize_preset_name(preset)
    if not normalized_preset:
        return []
    return list(STACK_PRESETS.get(normalized_preset, []))


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
        lines.append(f"  - 可用写法: {preset_name} / {details['name']}")
        lines.append(f"  - 适合: {details['best_for']}")
        lines.append(f"  - 模块: {modules}")
    return "\n".join(lines)
