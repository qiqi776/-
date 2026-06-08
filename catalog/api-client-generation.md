# API 客户端与 SDK 生成组件

API 客户端与 SDK 生成组件覆盖从 OpenAPI/Swagger 等接口契约生成类型、请求客户端、SDK、Mock、查询 Hooks 和多语言客户端代码；OpenAPI 文档渲染、在线调试和开发者门户放在 API 文档分类，入口流量治理放在 API 网关分类，服务端框架放在后端分类。

## OpenAPI Generator

- GitHub: https://github.com/OpenAPITools/openapi-generator
- 官网: https://openapi-generator.tech
- 模块: API 客户端生成 / 多语言 SDK / 服务端 Stub
- 技术栈: Java, OpenAPI, Mustache Templates
- 许可证: Apache-2.0
- 适合: 需要从 OpenAPI 规范生成多语言 SDK、客户端、服务端 Stub、文档和模板化代码的团队。
- 不适合: 只需要前端 TypeScript 类型，或项目不想维护生成模板、配置和规范兼容性差异。
- 接入成本: 中
- 替代方案: Orval, Hey API OpenAPI TS, openapi-typescript
- 评分: 4/5
- 备注: 生态覆盖面最广；生产前要锁定生成器版本、模板改动、规范校验、CI 生成流程和生成代码的安全审查。

## Orval

- GitHub: https://github.com/orval-labs/orval
- 官网: https://orval.dev
- 模块: API 客户端生成 / TypeScript / 前端查询 Hooks
- 技术栈: TypeScript, OpenAPI, React Query, SWR, Vue Query
- 许可证: MIT
- 适合: 前端团队需要从 OpenAPI 生成类型安全请求函数、React/Vue/Svelte/Solid Query Hooks、Mock 和 Zod Schema。
- 不适合: 需要生成 Java、Go、Python 等多语言 SDK，或不使用现代前端数据请求生态的项目。
- 接入成本: 中
- 替代方案: Hey API OpenAPI TS, openapi-typescript, OpenAPI Generator
- 评分: 4/5
- 备注: 适合把前后端契约接入前端工程流；上线前要确认生成目录、缓存键、错误模型、Mock 策略和接口变更审查。

## Hey API OpenAPI TS

- GitHub: https://github.com/hey-api/openapi-ts
- 官网: https://heyapi.dev
- 模块: API 客户端生成 / TypeScript SDK / Schema
- 技术栈: TypeScript, OpenAPI, Fetch, Axios, TanStack Query, Zod
- 许可证: MIT
- 适合: TypeScript 项目需要生成生产级 SDK、类型、Schema、TanStack Query Hooks，并通过插件扩展客户端行为。
- 不适合: 需要传统多语言企业 SDK 生成，或团队只想生成纯类型而不需要 SDK、客户端和插件体系。
- 接入成本: 中
- 替代方案: Orval, openapi-typescript, OpenAPI Generator
- 评分: 4/5
- 备注: 插件体系灵活，适合前端和全栈 TypeScript；生产前要确认 Node 版本、插件组合、生成代码边界、认证注入和规范来源可信度。
