# 通信渠道与短信语音组件

通信渠道与短信语音组件覆盖短信网关、批量短信、可编程语音、SIP/电话网络接入和 CPaaS 基础设施；通知模板、用户偏好和多渠道编排放在通知触达分类，邮件投递放在邮件组件分类，WebRTC 会议和实时媒体房间放在音视频通话分类。

## Fonoster

- GitHub: https://github.com/fonoster/fonoster
- 官网: https://fonoster.com
- 模块: 通信渠道 / 可编程语音 / CPaaS
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: 需要自托管类 Twilio 通信能力、可编程语音应用、PBX 功能、号码和电话网络接入的产品或平台团队。
- 不适合: 只需要简单短信验证码，或团队没有电话网络、SIP、号码资源和语音链路运维经验的项目。
- 接入成本: 高
- 替代方案: jambonz, Routr, 商业 CPaaS 服务
- 评分: 4/5
- 备注: 适合把通信能力做成平台底座；生产前要确认运营商接入、号码资源、录音存储、语音合成、费用控制和通信合规边界。

## jambonz

- GitHub: https://github.com/jambonz/jambonz-feature-server
- 官网: https://jambonz.org
- 模块: 通信渠道 / 可编程语音 / 自托管 CPaaS
- 技术栈: JavaScript, Node.js, FreeSWITCH, MySQL, Redis
- 许可证: MIT
- 适合: 需要自托管语音应用平台、呼叫流程控制、SIP/FreeSWITCH 集成、语音机器人和企业通信自动化的团队。
- 不适合: 小型 Web 应用只需要托管短信、邮件或站内通知，或团队不想维护 SBC、媒体服务器、数据库和缓存组件。
- 接入成本: 高
- 替代方案: Fonoster, Routr, Asterisk
- 评分: 4/5
- 备注: 平台组件较多但边界清楚；上线前要验证部署拓扑、呼叫质量、语音识别/合成供应商、号码路由、监控和故障转移。

## playSMS

- GitHub: https://github.com/playsms/playsms
- 官网: https://www.playsms.org
- 模块: 通信渠道 / 短信网关 / 批量短信
- 技术栈: PHP, MySQL, SMS Gateway
- 许可证: GPL-3.0
- 适合: 需要自托管短信管理后台、批量短信、短信收发、SMSC 路由、短信到邮箱和多网关适配的组织。
- 不适合: 不能接受 GPL 许可证约束，或需要现代 SaaS 多租户通知编排、复杂用户偏好中心和托管送达率优化的项目。
- 接入成本: 中
- 替代方案: Kannel, Jasmin, Fonoster
- 评分: 3/5
- 备注: 适合短信网关管理和传统短信业务；接入前要确认短信供应商、国家地区规则、退订机制、黑名单、送达回执和安全边界。
