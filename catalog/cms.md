# 内容管理组件

内容管理组件覆盖 Headless CMS、内容编辑、文档站和营销内容后台。

## Strapi

- GitHub: https://github.com/strapi/strapi
- 官网: https://strapi.io
- 模块: 内容管理 / Headless CMS
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: 需要快速搭建内容模型、管理后台、API 和多角色内容编辑流程的产品。
- 不适合: 只需要静态 Markdown 内容，或团队不想维护独立 CMS 服务的项目。
- 接入成本: 中
- 替代方案: Payload CMS, Directus, Keystone
- 评分: 4/5
- 备注: 生态成熟，适合内容模型变化较多的应用。

## Payload CMS

- GitHub: https://github.com/payloadcms/payload
- 官网: https://payloadcms.com
- 模块: 内容管理 / TypeScript CMS
- 技术栈: TypeScript, Node.js, React
- 许可证: MIT
- 适合: TypeScript 项目、需要代码定义内容模型、可定制 Admin 和与应用后端深度集成的场景。
- 不适合: 团队希望完全低代码配置 CMS，或不想把 CMS 作为应用代码的一部分维护。
- 接入成本: 中
- 替代方案: Strapi, Keystone, TinaCMS
- 评分: 4/5
- 备注: 对现代 TypeScript 团队友好，适合把 CMS 当作应用模块而不是外部平台。

## TinaCMS

- GitHub: https://github.com/tinacms/tinacms
- 官网: https://tina.io
- 模块: 内容管理 / Git-backed CMS
- 技术栈: TypeScript, React, GraphQL
- 许可证: Apache-2.0
- 适合: Markdown/MDX 内容、文档站、营销站和希望内容变更能进入 Git 工作流的项目。
- 不适合: 复杂多角色内容平台、非 Git 内容源，或需要传统数据库 CMS 的项目。
- 接入成本: 中
- 替代方案: Decap CMS, Payload CMS, Strapi
- 评分: 4/5
- 备注: 很适合内容和代码一起版本化的站点。
