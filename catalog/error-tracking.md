# 错误跟踪与异常上报组件

错误跟踪与异常上报组件覆盖应用异常收集、崩溃报告、堆栈聚合、前端错误、发布版本关联、告警通知和会话回放辅助排障；指标、日志、链路追踪和仪表盘放在监控分类，公开事故沟通放在状态页分类，代码质量测试放在测试与质量分类。Sentry 主服务等采用 FSL/商业限制的项目要单独审查许可证，不能只按 SDK 的 MIT 许可证判断整个平台。

## Exceptionless

- GitHub: https://github.com/exceptionless/Exceptionless
- 官网: https://exceptionless.com
- 模块: 错误跟踪 / 异常上报 / 日志
- 技术栈: C#, .NET, Svelte, JavaScript, Elasticsearch, Redis
- 许可证: Apache-2.0
- 适合: 需要自托管实时错误报告、异常聚合、事件日志、项目分组、告警和多语言客户端接入的团队。
- 不适合: 团队不想维护 .NET、Elasticsearch/OpenSearch、Redis 等服务，或主要需求是完整 APM 与分布式追踪平台。
- 接入成本: 高
- 替代方案: Highlight, SigNoz, OpenReplay
- 评分: 4/5
- 备注: 平台能力完整且许可证清楚；生产前要确认存储规模、索引保留、事件脱敏、告警噪音、版本标记和客户端 SDK 覆盖范围。

## Highlight

- GitHub: https://github.com/highlight/highlight
- 官网: https://highlight.io
- 模块: 错误跟踪 / 会话回放 / 全栈监控
- 技术栈: TypeScript, Go, React, ClickHouse, OpenTelemetry
- 许可证: Apache-2.0 / Other
- 适合: Web 产品需要把前端异常、会话回放、日志、追踪和用户行为上下文放在一起排查线上问题。
- 不适合: 团队只需要轻量异常收集，或不能接受仓库中企业目录、子目录许可证和托管服务边界需要单独核对。
- 接入成本: 高
- 替代方案: Exceptionless, SigNoz, OpenReplay
- 评分: 4/5
- 备注: 适合前端体验和全栈排障联动；上线前要重点核对子目录许可证、采样率、隐私遮罩、会话数据保留、ClickHouse 成本和 SDK 注入范围。

## SigNoz

- GitHub: https://github.com/SigNoz/signoz
- 官网: https://signoz.io
- 模块: 错误跟踪 / APM / OpenTelemetry
- 技术栈: Go, TypeScript, ClickHouse, OpenTelemetry
- 许可证: MIT Expat（核心；ee/cmd/enterprise 另行许可）
- 适合: 团队希望把异常监控、日志、指标、链路追踪和告警统一在 OpenTelemetry 原生平台中排查线上问题。
- 不适合: 只需要极轻量 Airbrake 兼容错误列表，或不想维护 ClickHouse 和完整观测平台的项目。
- 接入成本: 高
- 替代方案: Exceptionless, Highlight, OpenReplay
- 评分: 4/5
- 备注: 异常监控能力成熟且生态活跃；生产前要确认企业目录许可边界、采样率、ClickHouse 容量、数据保留和告警策略。
