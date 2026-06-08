# 日志管理与分析组件

日志管理与分析组件覆盖应用日志、基础设施日志、采集代理、解析转换、日志聚合、查询、保留策略、告警联动和成本治理。它解决“运行时日志如何被收集、清洗、存储、检索和用于排障”的问题；指标、仪表盘、链路追踪和通用遥测架构放在监控分类，应用异常、崩溃报告和会话回放放在错误跟踪分类，站内全文搜索放在搜索分类。

## Grafana Loki

- GitHub: https://github.com/grafana/loki
- 官网: https://grafana.com/oss/loki/
- 模块: 日志管理 / 日志聚合 / 标签查询
- 技术栈: Go, Prometheus, Grafana, Object Storage
- 许可证: AGPL-3.0
- 适合: 已经使用 Prometheus/Grafana，希望用标签索引和对象存储低成本管理 Kubernetes、服务和基础设施日志的团队。
- 不适合: 需要全文倒排索引、复杂日志分析 DSL、长期安全审计检索，或团队不能接受 AGPL 许可证义务的项目。
- 接入成本: 中
- 替代方案: OpenSearch, Elasticsearch, ClickHouse, VictoriaLogs
- 评分: 4/5
- 备注: 成本模型依赖标签设计和对象存储；生产前要确认多租户、日志保留、查询限制、告警规则、Grafana 集成和许可证边界。

## Fluent Bit

- GitHub: https://github.com/fluent/fluent-bit
- 官网: https://fluentbit.io
- 模块: 日志管理 / 采集代理 / 边缘转发
- 技术栈: C, Lua, Kubernetes, OpenTelemetry
- 许可证: Apache-2.0
- 适合: 需要轻量日志采集、容器日志 tail、边缘节点转发、多输出插件和低资源占用 agent 的项目。
- 不适合: 需要复杂事件路由、强类型转换、全链路可观测性数据处理，或希望用一个管道统一 metrics/traces/logs 的团队。
- 接入成本: 低
- 替代方案: Vector, Fluentd, OpenTelemetry Collector
- 评分: 4/5
- 备注: 适合先解决日志采集与转发；上线前要确认 buffer、背压、日志丢弃策略、Kubernetes metadata、输出端重试和配置热更新方式。

## Vector

- GitHub: https://github.com/vectordotdev/vector
- 官网: https://vector.dev
- 模块: 日志管理 / 可观测性管道 / 数据转换
- 技术栈: Rust, VRL, OpenTelemetry, Kafka, HTTP
- 许可证: MPL-2.0
- 适合: 平台团队需要统一采集、转换、采样和路由 logs、metrics、traces，并用声明式管道接入多个后端。
- 不适合: 只需要最简单容器日志 tail，或团队不想维护管道 DSL、状态缓存和多目的地故障处理。
- 接入成本: 中
- 替代方案: Fluent Bit, Fluentd, OpenTelemetry Collector
- 评分: 4/5
- 备注: 适合把日志管道平台化；落地前要设计拓扑、VRL 转换测试、端到端延迟、磁盘缓冲、schema 版本和目标端失败降级。
