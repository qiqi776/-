# 通知触达组件

通知触达组件覆盖多渠道通知、站内信、短信、移动推送、Webhook、团队告警和自托管消息推送服务。

## Novu

- GitHub: https://github.com/novuhq/novu
- 官网: https://novu.co
- 模块: 通知 / 多渠道通知 / 工作流
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: 需要统一管理邮件、站内信、短信、推送、Webhook 和通知模板的 SaaS 或平台型项目。
- 不适合: 项目只有单一邮件发送需求，或通知规则非常简单，不需要独立通知中心。
- 接入成本: 中
- 替代方案: Knock, Courier, 自研通知服务
- 评分: 4/5
- 备注: 适合把通知模板、用户偏好和触达渠道集中治理；生产前要确认企业功能边界、渠道供应商、退订策略和审计日志。

## ntfy

- GitHub: https://github.com/binwiederhier/ntfy
- 官网: https://ntfy.sh
- 模块: 通知 / Push / Webhook
- 技术栈: Go, Android, Web Push
- 许可证: Apache-2.0
- 适合: 需要轻量自托管 Push、Webhook 到手机/浏览器推送、运维告警和简单主题订阅的团队。
- 不适合: 需要复杂用户画像、模板编排、多渠道偏好中心或企业级通知运营后台的项目。
- 接入成本: 低
- 替代方案: Gotify, Novu, Pushover
- 评分: 4/5
- 备注: 部署和接入都很轻；要设计主题权限、访问 token、消息保留时间和移动端通知可靠性。

## Gotify

- GitHub: https://github.com/gotify/server
- 官网: https://gotify.net
- 模块: 通知 / 自托管推送 / 告警
- 技术栈: Go, WebSocket
- 许可证: MIT
- 适合: 需要自托管简单应用通知、服务器告警、Webhook 推送和内部工具消息触达的团队。
- 不适合: 面向大量终端用户的营销通知，或需要短信、邮件、移动 Push 多渠道编排的产品。
- 接入成本: 低
- 替代方案: ntfy, Novu, Apprise
- 评分: 4/5
- 备注: 适合内部告警和工具通知；生产前要确认用户权限、客户端覆盖、消息保留和外部暴露安全边界。
