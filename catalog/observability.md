# 监控组件

监控组件覆盖指标、仪表盘、链路追踪、日志和错误跟踪。

## Prometheus

- GitHub: https://github.com/prometheus/prometheus
- 官网: https://prometheus.io
- 模块: 监控 / 指标
- 技术栈: Go
- 许可证: Apache-2.0
- 适合: 指标采集、告警基础、服务监控和云原生基础设施。
- 不适合: 项目只需要简单托管可用性监控。
- 接入成本: 中
- 替代方案: VictoriaMetrics, InfluxDB, 托管监控平台
- 评分: 5/5
- 备注: 自托管和云原生指标监控的强默认选择。

## Grafana

- GitHub: https://github.com/grafana/grafana
- 官网: https://grafana.com
- 模块: 监控 / 仪表盘
- 技术栈: TypeScript, Go
- 许可证: AGPL-3.0
- 适合: 仪表盘、指标和日志可视化，以及构建共享运维视图。
- 不适合: 团队不能接受 AGPL 义务，或只需要一个简单状态页。
- 接入成本: 中
- 替代方案: Kibana, Metabase, 托管仪表盘
- 评分: 4/5
- 备注: 如果要嵌入或重新分发，许可证需要重点审查。

## OpenTelemetry Collector

- GitHub: https://github.com/open-telemetry/opentelemetry-collector
- 官网: https://opentelemetry.io
- 模块: 监控 / 遥测管线
- 技术栈: Go
- 许可证: Apache-2.0
- 适合: 在多服务中采集、处理和导出 traces、metrics、logs。
- 不适合: 项目只有一个小服务，也没有分布式追踪需求。
- 接入成本: 高
- 替代方案: 厂商 Agent, Fluent Bit, Vector
- 评分: 4/5
- 备注: 当可观测性架构跨多个服务或工具时再引入更合理。

