# LLM 可观测性与评估组件

LLM 可观测性与评估组件覆盖提示词版本、模型调用追踪、Token 与成本分析、数据集、离线评估、在线反馈、RAG 质量评估和红队测试。它解决“AI 应用效果是否稳定、哪里出错、上线前后如何评估”的问题；LLM/RAG 编排和 Agent 放在 AI 分类，输入输出策略、拒答规则和结构化响应放在 LLM 护栏与结构化输出分类，模型托管、推理服务和模型网关放在模型服务与推理网关分类，通用指标和链路追踪放在监控分类，普通单元测试和端到端测试放在测试与质量分类。

## Langfuse

- GitHub: https://github.com/langfuse/langfuse
- 官网: https://langfuse.com
- 模块: LLM 可观测性 / Prompt 管理 / 评估
- 技术栈: TypeScript, Next.js, PostgreSQL, ClickHouse, Redis
- 许可证: MIT（ee 目录另行许可）
- 适合: 生产级 LLM 应用需要记录模型调用、检索步骤、Agent 动作、提示词版本、用户反馈、数据集和自动/人工评估。
- 不适合: 只做少量提示词对比，或团队不想维护 ClickHouse、PostgreSQL、队列、权限和遥测采集平台。
- 接入成本: 中
- 替代方案: Phoenix, promptfoo, Helicone
- 评分: 5/5
- 备注: 主体代码按 MIT 使用，企业目录有单独许可边界；接入前要确认提示词和用户数据脱敏、采样率、保留周期、租户隔离、成本口径和告警责任。

## Phoenix

- GitHub: https://github.com/Arize-ai/phoenix
- 官网: https://phoenix.arize.com
- 模块: LLM 可观测性 / RAG 评估 / 实验
- 技术栈: Python, TypeScript, OpenTelemetry, OpenInference
- 许可证: Elastic-2.0
- 适合: 团队需要追踪 LLM/RAG 调用、构建评估数据集、比较提示词/模型/检索变化，并分析回答质量、检索相关性和实验结果。
- 不适合: 计划把该软件作为托管或管理服务对第三方提供，或团队只需要一个轻量 CLI 做提示词回归测试。
- 接入成本: 中
- 替代方案: Langfuse, promptfoo, OpenTelemetry + 自研评估管线
- 评分: 4/5
- 备注: Elastic-2.0 对托管服务、许可证功能和再分发有明确限制；商业产品集成前要单独审查许可证、数据保留、追踪字段脱敏和评估指标可信度。

## promptfoo

- GitHub: https://github.com/promptfoo/promptfoo
- 官网: https://www.promptfoo.dev
- 模块: LLM 评估 / Prompt 测试 / 红队
- 技术栈: TypeScript, Node.js, CLI, YAML
- 许可证: MIT
- 适合: 在本地或 CI 中比较提示词、模型和供应商输出，做回归评估、越狱/注入/敏感输出红队扫描和上线前质量门禁。
- 不适合: 需要长期保存生产链路追踪、用户反馈、Prompt 版本协作和运营仪表盘的 LLMOps 平台。
- 接入成本: 低
- 替代方案: Langfuse, Phoenix, Ragas
- 评分: 4/5
- 备注: 很适合做发布前评估门禁；要准备稳定的测试集、断言规则、人工复核样本和失败阈值，不能只依赖 LLM-as-a-judge 结论。
