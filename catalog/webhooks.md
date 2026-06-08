# Webhook 与外部事件投递组件

Webhook 与外部事件投递组件覆盖产品事件发布、客户订阅端点、签名校验、重试、失败告警、事件重放、交付日志和开发者集成；内部服务消息解耦放在消息队列分类，用户/团队消息触达放在通知触达分类，入口路由和鉴权放在 API 网关分类。

## Svix

- GitHub: https://github.com/svix/svix-webhooks
- 官网: https://www.svix.com
- 模块: Webhook / 事件投递 / 开发者集成
- 技术栈: Rust, PostgreSQL, Redis, Kafka, 多语言 SDK
- 许可证: MIT
- 适合: SaaS 或平台型产品需要对外提供可靠 Webhook，覆盖消息签名、重试、失败处理、端点管理、事件日志和多语言 SDK。
- 不适合: 只需要向内部 Slack 或运维工具发简单通知，或团队不想维护独立 Webhook 服务。
- 接入成本: 中
- 替代方案: Hookdeck Outpost, Convoy, Hook0
- 评分: 4/5
- 备注: 适合把客户集成能力产品化；生产前要确认事件 schema、幂等键、签名轮换、失败队列、租户隔离和 SDK 版本策略。

## Hookdeck Outpost

- GitHub: https://github.com/hookdeck/outpost
- 官网: https://outpost.hookdeck.com/docs
- 模块: Webhook / 事件目的地 / 出站事件基础设施
- 技术栈: Go, PostgreSQL, Redis, TypeScript, Python
- 许可证: Apache-2.0
- 适合: 事件生产方需要自托管出站 Webhook 和多种事件目的地，支持 HTTP Webhook、EventBridge、SQS、S3、Pub/Sub、RabbitMQ 和 Kafka。
- 不适合: 只需要应用内同步回调，或项目没有多租户、客户端点管理、事件目的地和交付可观测需求。
- 接入成本: 中
- 替代方案: Svix, Convoy, Hook0
- 评分: 4/5
- 备注: 适合把出站事件投递做成平台能力；上线前要确认主题模型、目标类型、重试策略、用户门户、OpenTelemetry 和队列依赖。

## Convoy

- GitHub: https://github.com/frain-dev/convoy
- 官网: https://getconvoy.io
- 模块: Webhook / 网关 / 双向事件
- 技术栈: Go, TypeScript, PostgreSQL
- 许可证: Elastic License 2.0
- 适合: 需要专门 Webhook 网关来接收、持久化、调试、投递和管理大规模事件，并支持重试、限流、滚动密钥和端点订阅的团队。
- 不适合: 团队只接受 OSI 宽松许可证，或只需要一个简单 HTTP 回调而不需要完整 Webhook 网关。
- 接入成本: 中
- 替代方案: Svix, Hookdeck Outpost, Hook0
- 评分: 3/5
- 备注: 功能覆盖成熟但许可证不是常规宽松开源；生产前要重点审查 Elastic License v2.0、商业化限制、静态 IP、密钥轮换和失败告警策略。
