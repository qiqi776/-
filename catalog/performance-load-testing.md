# 性能与负载测试组件

性能与负载测试组件覆盖接口压测、浏览器或用户行为负载、容量基线、吞吐与延迟阈值、压力场景、分布式执行、结果分析和发布前性能门禁。它解决“系统在目标并发、流量和数据规模下是否能稳定运行”的问题；单元测试、端到端测试和自动化回归放在测试与质量分类，线上指标、告警和链路追踪放在监控分类，页面可访问性和 Lighthouse 综合审计放在无障碍与可访问性测试分类。

## k6

- GitHub: https://github.com/grafana/k6
- 官网: https://k6.io
- 模块: 性能测试 / API 压测 / JavaScript 场景
- 技术栈: Go, JavaScript, HTTP, WebSocket, Grafana
- 许可证: AGPL-3.0
- 适合: 团队需要用代码定义 API、WebSocket、浏览器或混合场景压测，并把阈值、趋势和发布门禁纳入 CI/CD。
- 不适合: 团队不能接受 AGPL 许可证义务，或需要完全图形化录制、复杂企业插件和老式 JMeter 生态兼容。
- 接入成本: 中
- 替代方案: Locust, Apache JMeter, Gatling
- 评分: 4/5
- 备注: 适合把性能测试脚本版本化；生产前要确认执行节点、阈值、结果存储、Grafana 集成、浏览器模式成本和许可证边界。

## Locust

- GitHub: https://github.com/locustio/locust
- 官网: https://locust.io
- 模块: 性能测试 / 用户行为建模 / 分布式压测
- 技术栈: Python, gevent, HTTP, Web UI
- 许可证: MIT
- 适合: Python 团队需要用代码描述用户行为、等待时间、任务权重和分布式压测，并快速观察实时吞吐与延迟。
- 不适合: 需要浏览器级真实用户渲染，或团队希望完全无代码录制和企业级测试计划管理。
- 接入成本: 低
- 替代方案: k6, Apache JMeter, Gatling
- 评分: 4/5
- 备注: 接入成本低，适合从核心 API 和业务流程开始做容量基线；要设计测试数据、用户凭据、分布式 worker、限流边界和报告归档。

## Apache JMeter

- GitHub: https://github.com/apache/jmeter
- 官网: https://jmeter.apache.org
- 模块: 性能测试 / 协议压测 / 测试计划
- 技术栈: Java, JVM, HTTP, JDBC, JMS
- 许可证: Apache-2.0
- 适合: 企业团队需要成熟 GUI、丰富协议插件、JDBC/JMS/LDAP 等老系统压测和可共享测试计划。
- 不适合: 希望用现代代码化脚本维护轻量压测，或团队无法接受 JVM、测试计划文件和插件兼容成本。
- 接入成本: 中
- 替代方案: k6, Locust, Gatling
- 评分: 4/5
- 备注: 生态成熟但测试计划容易膨胀；落地前要确认无头运行、插件版本、分布式执行、测试数据隔离、结果文件大小和 CI 门禁方式。
