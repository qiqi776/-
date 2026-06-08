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
- 替代方案: Highlight, Errbit, Sentry
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
- 替代方案: Exceptionless, OpenReplay, Sentry
- 评分: 4/5
- 备注: 适合前端体验和全栈排障联动；上线前要重点核对子目录许可证、采样率、隐私遮罩、会话数据保留、ClickHouse 成本和 SDK 注入范围。

## Errbit

- GitHub: https://github.com/errbit/errbit
- 官网: https://errbit.com
- 模块: 错误跟踪 / Airbrake 兼容 / Ruby
- 技术栈: Ruby, Rails, MongoDB
- 许可证: MIT
- 适合: Ruby/Rails 或 Airbrake 协议生态项目需要轻量自托管错误收集、异常列表、通知和基础错误管理。
- 不适合: 需要现代前端会话回放、复杂性能追踪、多语言深度 SDK、日志聚合和大规模多租户错误平台的场景。
- 接入成本: 中
- 替代方案: Exceptionless, Sentry, GlitchTip
- 评分: 3/5
- 备注: 简单直接、许可证宽松；选型时要复核维护活跃度、MongoDB 运维、通知插件、协议兼容和长期升级路径。
