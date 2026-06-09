# 状态页与事故沟通组件

状态页与事故沟通组件覆盖公开服务状态、可用性展示、事故记录、维护窗口、订阅通知、历史事件和客户沟通入口；内部指标、日志、链路追踪和告警基础设施放在监控分类，多渠道用户通知放在通知触达分类。

## Upptime

- GitHub: https://github.com/upptime/upptime
- 官网: https://upptime.js.org
- 模块: 状态页 / 可用性监控 / GitHub Pages
- 技术栈: GitHub Actions, GitHub Issues, GitHub Pages, JavaScript, Svelte
- 许可证: MIT
- 适合: 小团队或开源项目想用 GitHub Actions 自动检查端点，并把状态页、事故记录和历史数据托管在 GitHub Pages。
- 不适合: 私有仓库状态页、复杂维护窗口审批、多租户状态页、企业级订阅通知或不能依赖 GitHub Actions 配额的场景。
- 接入成本: 低
- 替代方案: Gatus, Uptime Kuma, Cachet
- 评分: 4/5
- 备注: 适合快速搭建零服务器状态页；生产前要确认公开仓库要求、检查频率、GitHub Actions 限额、Issues 数据保留和自定义域名配置。

## Gatus

- GitHub: https://github.com/TwiN/gatus
- 官网: https://gatus.io
- 模块: 状态页 / 健康检查 / 告警
- 技术栈: Go, Docker, YAML
- 许可证: Apache-2.0
- 适合: 需要自托管端点健康检查、状态页、延迟图表、条件断言、告警通知和轻量事故展示的工程团队。
- 不适合: 只想要静态公告页，或需要完整客户订阅管理、事故复盘流程、审批工作流和品牌化状态门户的产品团队。
- 接入成本: 低
- 替代方案: Upptime, Uptime Kuma, Cachet
- 评分: 4/5
- 备注: 适合把监控探活和状态展示合在一起；上线前要设计检查位置、外部依赖、告警噪音、状态页访问权限和历史数据存储。

## Uptime Kuma

- GitHub: https://github.com/louislam/uptime-kuma
- 官网: https://uptime.kuma.pet
- 模块: 状态页 / 自托管监控 / 多状态页
- 技术栈: Node.js, Vue, SQLite
- 许可证: MIT
- 适合: 团队需要自托管可用性监控、HTTP/TCP/Ping/DNS 检查、通知渠道和多个状态页。
- 不适合: 只想要静态公告页，或需要复杂审批、客户订阅偏好和企业级事故沟通流程。
- 接入成本: 低
- 替代方案: Upptime, Gatus, Cachet
- 评分: 4/5
- 备注: 自托管监控和状态页成熟候选；上线前要确认数据持久化、通知渠道、反向代理、备份和升级方式。
