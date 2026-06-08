# 邮件组件

邮件组件覆盖邮件发送、事务邮件、邮件列表、Newsletter、营销邮件、邮件投递基础设施和本地邮件测试捕获；多渠道通知、Push 和 Webhook 统一放在通知触达分类。

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

## Mailpit

- GitHub: https://github.com/axllent/mailpit
- 官网: https://mailpit.axllent.org
- 模块: 邮件 / 本地邮件测试 / SMTP 捕获
- 技术栈: Go, Vue
- 许可证: MIT
- 适合: 开发、测试和 CI 环境中捕获应用发送的邮件，并通过 Web UI、API 检查邮件内容。
- 不适合: 需要生产级邮件投递、邮件列表运营或真实用户营销触达的场景。
- 接入成本: 低
- 替代方案: MailHog, Mailtrap, Postal
- 评分: 3/5
- 备注: 适合作为项目组件栈里的邮件沙箱，降低事务邮件联调和自动化测试成本。
