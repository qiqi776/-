# 认证组件

认证组件覆盖登录、身份、OAuth、用户管理和访问控制。

## Supabase Auth

- GitHub: https://github.com/supabase/supabase
- 官网: https://supabase.com/auth
- 模块: 认证 / 数据库 / 后端
- 技术栈: TypeScript, Go, PostgreSQL
- 许可证: Apache-2.0
- 适合: 快速开发产品，并希望认证、Postgres、存储和 API 能在同一平台中协作。
- 不适合: 需要复杂企业 IAM、深度自定义身份流程，或希望尽量减少平台绑定。
- 接入成本: 中
- 替代方案: Auth.js, Keycloak, Ory
- 评分: 4/5
- 备注: 当认证和 Postgres 可以一起选择时很有价值。

## Auth.js

- GitHub: https://github.com/nextauthjs/next-auth
- 官网: https://authjs.dev
- 模块: 认证 / Web
- 技术栈: TypeScript, JavaScript
- 许可证: ISC
- 适合: 需要 OAuth、邮箱登录和框架友好会话处理的 Web 应用。
- 不适合: 需要独立身份提供商或集中式企业 IAM 的项目。
- 接入成本: 低
- 替代方案: Supabase Auth, Lucia, Ory
- 评分: 4/5
- 备注: 很适合 Next.js 及相近 Web 技术栈。

## Keycloak

- GitHub: https://github.com/keycloak/keycloak
- 官网: https://www.keycloak.org
- 模块: 认证 / IAM
- 技术栈: Java
- 许可证: Apache-2.0
- 适合: 企业身份、SSO、Realm、OAuth2、OpenID Connect、SAML 和集中式访问控制。
- 不适合: 只需要轻量登录且不想承担运维复杂度的项目。
- 接入成本: 高
- 替代方案: Ory, Zitadel, Authentik
- 评分: 4/5
- 备注: 能力强，但比应用级认证库更重。

