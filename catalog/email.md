# 邮件与通知组件

邮件与通知组件覆盖邮件发送、事务通知、营销邮件和通知基础设施。

## Postal

- GitHub: https://github.com/postalserver/postal
- 官网: https://postalserver.io
- 模块: 邮件 / 自托管邮件平台
- 技术栈: Ruby, JavaScript
- 许可证: MIT
- 适合: 需要自托管邮件发送平台、事务邮件和邮件投递控制的项目。
- 不适合: 团队不想处理邮件投递信誉、DNS、退信和运维复杂度。
- 接入成本: 高
- 替代方案: Listmonk, Mailpit, 商业邮件服务
- 评分: 3/5
- 备注: 邮件自托管难点不在安装，而在长期投递质量。

## Listmonk

- GitHub: https://github.com/knadh/listmonk
- 官网: https://listmonk.app
- 模块: 邮件 / Newsletter / 营销通知
- 技术栈: Go, PostgreSQL
- 许可证: AGPL-3.0
- 适合: Newsletter、邮件列表、营销活动和批量通知管理。
- 不适合: 团队不能接受 AGPL，或只需要应用内少量事务邮件。
- 接入成本: 中
- 替代方案: Postal, Mautic, 商业邮件营销平台
- 评分: 4/5
- 备注: 适合内容产品和社区产品沉淀用户触达能力。

## Novu

- GitHub: https://github.com/novuhq/novu
- 官网: https://novu.co
- 模块: 通知 / 多渠道通知
- 技术栈: TypeScript, Node.js
- 许可证: MIT（核心）/ 商业许可证（enterprise）
- 适合: 需要统一管理邮件、站内信、短信、推送等多渠道通知的 SaaS 或平台型项目。
- 不适合: 项目只有单一邮件发送需求、通知规则非常简单，或要求整个仓库完全使用单一开源许可证。
- 接入成本: 中
- 替代方案: Knock, Courier, 自研通知服务
- 评分: 4/5
- 备注: Novu 是 open core，核心代码 MIT，enterprise 目录受商业许可证约束。
