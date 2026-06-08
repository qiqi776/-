# API 文档与接口契约组件

API 文档与接口契约组件覆盖 OpenAPI 文档渲染、接口调试、前后端契约协作和开发者门户。

## Swagger UI

- GitHub: https://github.com/swagger-api/swagger-ui
- 官网: https://swagger.io/tools/swagger-ui
- 模块: API 文档 / OpenAPI 交互文档
- 技术栈: JavaScript, OpenAPI
- 许可证: Apache-2.0
- 适合: 需要把 OpenAPI 规范渲染成交互式接口文档，并支持在线调试请求的后端项目。
- 不适合: 需要高度品牌化开发者门户，或希望文档体验更接近现代产品文档站的项目。
- 接入成本: 低
- 替代方案: Redoc, Scalar, Stoplight Elements
- 评分: 4/5
- 备注: 是 OpenAPI 生态中最通用的默认选择，适合放在服务启动后的开发和测试环境。

## Redoc

- GitHub: https://github.com/Redocly/redoc
- 官网: https://redocly.com/redoc
- 模块: API 文档 / OpenAPI 阅读文档
- 技术栈: TypeScript, React, OpenAPI
- 许可证: MIT
- 适合: 需要把 OpenAPI 规范渲染成阅读体验较好的静态 API 文档和开发者文档页面。
- 不适合: 主要需求是直接在页面里发起接口调试，或需要复杂协作工作台。
- 接入成本: 低
- 替代方案: Swagger UI, Scalar, Stoplight Elements
- 评分: 4/5
- 备注: 阅读体验比传统 Swagger UI 更清爽，适合公开 API 文档和产品化接口说明。

## Scalar

- GitHub: https://github.com/scalar/scalar
- 官网: https://scalar.com
- 模块: API 文档 / 接口文档与调试
- 技术栈: TypeScript, Vue, OpenAPI
- 许可证: MIT
- 适合: 需要现代化 OpenAPI 文档、接口调试、API 客户端体验和较强前端呈现效果的项目。
- 不适合: 团队只需要最保守、最通用的 OpenAPI 文档渲染器。
- 接入成本: 中
- 替代方案: Swagger UI, Redoc, Bruno
- 评分: 4/5
- 备注: 适合希望文档和调试体验更像产品的团队，生产前要确认部署方式和版本稳定性。
