# 数字身份与可验证凭证组件

数字身份与可验证凭证组件覆盖 DID、Verifiable Credentials、凭证发行、持有、验证、钱包、OpenID4VC、DIDComm 和去中心化信任服务；登录、SSO、OAuth 会话和企业 IAM 放在认证分类，角色权限和资源关系放在授权策略分类，电子合同签署证据放在电子签名分类。

## ACA-Py

- GitHub: https://github.com/openwallet-foundation/acapy
- 官网: https://aca-py.org
- 模块: 数字身份 / SSI Agent / 可验证凭证
- 技术栈: Python, AnonCreds, DIDComm, W3C VC
- 许可证: Apache-2.0
- 适合: 需要生产级服务端 SSI Agent、凭证发行方、持有方、验证方、Webhook 控制器和 Trust over IP 生态集成的组织。
- 不适合: 只需要普通用户登录、OAuth SSO，或团队没有 DID、钱包、凭证协议和密钥治理经验的项目。
- 接入成本: 高
- 替代方案: Credo, Veramo, walt.id Identity
- 评分: 4/5
- 备注: 适合严肃的可验证凭证网络和企业信任服务；上线前要确认 LTS 版本、协议互操作、钱包兼容、密钥托管、撤销机制和审计边界。

## Credo

- GitHub: https://github.com/openwallet-foundation/credo-ts
- 官网: https://credo.js.org
- 模块: 数字身份 / TypeScript 框架 / DID 与 VC
- 技术栈: TypeScript, Node.js, React Native, OpenID4VC, DIDComm
- 许可证: Apache-2.0
- 适合: TypeScript 或 React Native 团队构建去中心化身份应用、移动钱包、凭证发行/验证流程和跨平台 Agent。
- 不适合: 希望开箱即用部署完整门户，或只需要传统数据库用户表和密码登录的 Web 应用。
- 接入成本: 高
- 替代方案: ACA-Py, Veramo, walt.id Identity
- 评分: 4/5
- 备注: 框架灵活且协议覆盖广；生产前要验证 DID 方法、凭证格式、移动端安全存储、租户模型和协议版本兼容。

## walt.id Identity

- GitHub: https://github.com/walt-id/waltid-identity
- 官网: https://docs.walt.id
- 模块: 数字身份 / Issuer API / Verifier API / Wallet
- 技术栈: Kotlin, JVM, JavaScript, iOS, Docker
- 许可证: Apache-2.0
- 适合: 需要发行 API、验证 API、钱包 API、白标 Web 钱包、凭证门户和 OpenID4VC/SD-JWT/mdoc 工具链的团队。
- 不适合: 只想嵌入一个轻量登录组件，或无法接受多服务、多应用和凭证标准学习成本的项目。
- 接入成本: 高
- 替代方案: ACA-Py, Credo, Veramo
- 评分: 4/5
- 备注: 组件覆盖发行、验证和钱包，适合快速搭建凭证产品雏形；上线前要确认托管模式、密钥管理、凭证 schema、钱包体验、撤销和合规责任。
