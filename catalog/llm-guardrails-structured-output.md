# LLM 护栏与结构化输出组件

LLM 护栏与结构化输出组件覆盖输入/输出策略、敏感内容拦截、拒答规则、对话路径控制、结构化响应、JSON/Schema 约束、类型校验和生成后修复。它解决“模型能不能按产品边界和数据格式稳定输出”的问题；LLM/RAG 编排和 Agent 放在 AI 分类，模型托管和网关放在模型服务与推理网关分类，Prompt 版本、评估数据集和红队测试放在 LLM 可观测性与评估分类，人机验证和接口防刷放在反滥用分类，依赖漏洞和代码安全扫描放在安全扫描分类。

## Guardrails AI

- GitHub: https://github.com/guardrails-ai/guardrails
- 官网: https://www.guardrailsai.com
- 模块: LLM 护栏 / 输出校验 / 结构化数据
- 技术栈: Python, Pydantic, Validators, LLM API
- 许可证: Apache-2.0
- 适合: AI 应用需要对模型输入输出做格式校验、内容风险检测、自动重试、结构化数据生成和自定义 Validator。
- 不适合: 只需要模型网关路由，或团队不愿维护校验规则、失败处理和业务级安全策略。
- 接入成本: 中
- 替代方案: NeMo Guardrails, Outlines, 自研 Pydantic 校验
- 评分: 4/5
- 备注: 适合把 LLM 输出变成可验证契约；上线前要确认校验失败时的降级逻辑、延迟、重试成本、敏感字段脱敏和规则维护责任。

## NVIDIA NeMo Guardrails

- GitHub: https://github.com/NVIDIA/NeMo-Guardrails
- 官网: https://docs.nvidia.com/nemo/guardrails
- 模块: LLM 护栏 / 对话策略 / 安全控制
- 技术栈: Python, Colang, YAML, LLM API
- 许可证: Apache-2.0
- 适合: 对话式 AI 应用需要可编程护栏、对话路径控制、安全策略、工具调用约束和企业级聊天边界。
- 不适合: 只需要简单 JSON 输出格式，或团队无法维护独立的对话规则语言和策略测试集。
- 接入成本: 高
- 替代方案: Guardrails AI, LangChain Guardrails, 自研策略层
- 评分: 4/5
- 备注: 适合严肃对话产品和企业助手；接入前要验证策略覆盖率、误拒率、工具调用边界、规则版本管理、测试集和人工升级流程。

## Outlines

- GitHub: https://github.com/dottxt-ai/outlines
- 官网: https://dottxt-ai.github.io/outlines/
- 模块: LLM 结构化输出 / 约束式生成 / 类型约束
- 技术栈: Python, Pydantic, JSON Schema, Transformers, vLLM
- 许可证: Apache-2.0
- 适合: 应用需要在生成阶段约束 JSON、枚举、正则、Pydantic 模型或其他结构化输出，减少后处理解析失败。
- 不适合: 主要问题是内容安全、越狱防护、对话策略或多步骤 Agent 行为治理。
- 接入成本: 中
- 替代方案: Guardrails AI, Instructor, Guidance
- 评分: 4/5
- 备注: 更偏结构化生成引擎，不是完整安全平台；要确认目标模型后端支持、流式输出、schema 复杂度、生成速度和失败回退路径。
