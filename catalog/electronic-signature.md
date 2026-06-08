# 电子签名与合同签署组件

电子签名与合同签署组件覆盖 PDF 合同签署、收件人流程、字段放置、模板复用、邮件邀请、完成证书、审计轨迹和签署状态管理；普通 PDF 预览、Office 解析和文本抽取放在文档处理分类，账单合同生成和发票开具放在账单与发票分类。

## Documenso

- GitHub: https://github.com/documenso/documenso
- 官网: https://documenso.com
- 模块: 电子签名 / 合同签署 / PDF 签署
- 技术栈: TypeScript, React Router, Prisma, PostgreSQL
- 许可证: AGPL-3.0
- 适合: 需要自托管电子签名、PDF 合同签署、签署人流程、模板、团队协作、API 接入和审计轨迹的 SaaS 或内部系统。
- 不适合: 无法接受 AGPL-3.0 许可证义务，或需要特定司法辖区合格电子签名认证、硬件证书和复杂线下身份核验的场景。
- 接入成本: 高
- 替代方案: DocuSeal, OpenSign, LibreSign
- 评分: 4/5
- 备注: 功能覆盖完整但属于关键业务链路；上线前要确认 AGPL 合规、邮件送达、文件存储、签署证据、备份、品牌域名和法律合规边界。

## DocuSeal

- GitHub: https://github.com/docusealco/docuseal
- 官网: https://www.docuseal.com
- 模块: 电子签名 / 表单填署 / 文档签署
- 技术栈: Ruby on Rails, Vue, Tailwind CSS, PostgreSQL
- 许可证: AGPL-3.0
- 适合: 需要较快部署自托管签署门户、PDF 表单填署、签名字段、模板、API 和签署完成记录的团队。
- 不适合: 团队不想维护 Rails 应用，或闭源商业项目不能承担 AGPL-3.0 网络服务源码义务。
- 接入成本: 中
- 替代方案: Documenso, OpenSign, LibreSign
- 评分: 4/5
- 备注: 单体 Rails 部署相对直接；生产前要确认数据库、对象存储、邮件、签署审计、租户隔离、备份恢复和许可证边界。

## OpenSign

- GitHub: https://github.com/OpenSignLabs/OpenSign
- 官网: https://www.opensignlabs.com
- 模块: 电子签名 / DocuSign 替代 / PDF 签署
- 技术栈: JavaScript, React, Node.js, Parse Server, MongoDB
- 许可证: AGPL-3.0
- 适合: 需要开源 DocuSign 替代、多人签署、模板、签署链接、OTP 验证、API、审计轨迹和 Docker 自托管的产品。
- 不适合: 不想维护 Node.js、Parse Server 和 MongoDB 组合，或要求许可证更宽松、代码结构更简单的项目。
- 接入成本: 中
- 替代方案: Documenso, DocuSeal, LibreSign
- 评分: 4/5
- 备注: 功能面广且偏完整产品；部署前要确认 MongoDB 持久化、邮件配置、文件存储、API 权限、证书生成、升级路径和 AGPL 合规。
