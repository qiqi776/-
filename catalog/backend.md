# 后端组件

后端组件覆盖 API 框架、服务框架和服务端应用基础。

## FastAPI

- GitHub: https://github.com/fastapi/fastapi
- 官网: https://fastapi.tiangolo.com
- 模块: 后端 / API
- 技术栈: Python, Starlette, Pydantic
- 许可证: MIT
- 适合: Python API、AI 相关服务、内部工具，以及需要类型化请求模型的快速服务开发。
- 不适合: 团队需要内置管理后台、ORM 和完整全栈约定的框架。
- 接入成本: 低
- 替代方案: Django REST Framework, Flask, Litestar
- 评分: 5/5
- 备注: 和 AI、数据处理、自动化项目组合时很顺手。

## NestJS

- GitHub: https://github.com/nestjs/nest
- 官网: https://nestjs.com
- 模块: 后端 / API / 服务框架
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: 结构化 TypeScript 后端、模块化服务、较大团队，以及受益于依赖注入的项目。
- 不适合: 服务必须保持极小、极轻，或团队不想接受框架约束。
- 接入成本: 中
- 替代方案: Express, Fastify, AdonisJS
- 评分: 4/5
- 备注: 当架构一致性重要时，它比裸 Express 更稳。

## Django

- GitHub: https://github.com/django/django
- 官网: https://www.djangoproject.com
- 模块: 后端 / 全栈 Web
- 技术栈: Python
- 许可证: BSD-3-Clause
- 适合: 后台驱动的 Web 应用、内容系统、CRUD 密集型产品，以及需要内置 ORM 和 Admin 的项目。
- 不适合: 只需要一个小 API 服务，或明确偏好 async-first 架构。
- 接入成本: 中
- 替代方案: FastAPI, Rails, Laravel
- 评分: 4/5
- 备注: 更适合作为应用基础，而不是小模块。

