# 开源组件库

这个仓库用于整理 GitHub 上可复用的开源模块。目标不是把所有源码搬进来，而是把“开发一个项目时需要哪些组件、每类组件有哪些可靠选择、怎么组合它们”整理成可维护的索引。

## 这个仓库解决什么问题

做新项目时，真正难的通常不是“选哪个框架”，而是这些模块能不能拼起来：

- 登录与权限
- 前端界面
- 后端 API
- 数据库与 ORM
- AI / RAG / Agent
- 支付与订阅
- 部署与托管
- 监控与可观测性

本仓库把这些选择拆成明确的模块，并记录每个组件适合什么、不适合什么、接入成本和替代方案。

## 目录

| 分类 | 文件 | 用途 |
| --- | --- | --- |
| 前端 | [catalog/frontend.md](catalog/frontend.md) | UI 系统、管理后台、组件库、前端框架 |
| 后端 | [catalog/backend.md](catalog/backend.md) | API 框架、服务框架、后端基础设施 |
| 认证 | [catalog/auth.md](catalog/auth.md) | 登录、身份、OAuth、用户管理、权限控制 |
| 数据库 | [catalog/database.md](catalog/database.md) | 数据库、ORM、后端即服务、向量存储 |
| AI | [catalog/ai.md](catalog/ai.md) | LLM 应用、RAG、Agent、工作流、模型接入工具 |
| 支付 | [catalog/payment.md](catalog/payment.md) | 支付 SDK、电商引擎、结账、订阅 |
| 部署 | [catalog/deployment.md](catalog/deployment.md) | 自托管、PaaS、应用部署、基础设施胶水 |
| 监控 | [catalog/observability.md](catalog/observability.md) | 指标、仪表盘、链路追踪、日志、错误跟踪 |

## 项目组合蓝图

这些蓝图可以作为新项目选型的起点：

- [SaaS 起步项目](stacks/saas-starter.md)：认证、前端、后端、数据库、支付、部署、监控。
- [AI RAG 应用](stacks/ai-rag-app.md)：前端、API、LLM 编排、向量数据库、部署、监控。
- [内部管理后台](stacks/internal-admin.md)：管理 UI、后端、身份、数据库、部署。

## 组件条目格式

新增组件时使用下面的格式。字段名保持统一，便于后续脚本校验和生成机器可读索引。

```md
## 组件名称

- GitHub: https://github.com/org/repo
- 官网: https://example.com
- 模块: 认证 / 数据库 / 后端
- 技术栈: TypeScript, PostgreSQL
- 许可证: Apache-2.0
- 适合: 这个组件最适合的项目场景。
- 不适合: 使用这个组件成本过高或风险过大的场景。
- 接入成本: 低 / 中 / 高
- 替代方案: 组件 A, 组件 B
- 评分: 4/5
- 备注: 实际选型时需要注意的判断。
```

不要手写 star 数这类容易过期的字段，除非后续有自动化脚本维护。维护状态应该在新增或提升组件时人工复核。

## 如何拼装一个项目

1. 先列出项目需要的能力：认证、UI、数据库、文件存储、AI、支付、部署、监控。
2. 打开对应的 `catalog/` 分类文件。
3. 每个能力选择 1 个主组件和 1 个备选组件。
4. 在确定技术栈前检查许可证、接入成本、托管方式和数据边界。
5. 把最终组合写进项目 README 或架构说明。

完整流程见 [docs/project-assembly-guide.md](docs/project-assembly-guide.md)。

新增组件时可以从 [templates/component-entry.md](templates/component-entry.md) 复制模板。

发布到 GitHub 前，按 [docs/github-publish-guide.md](docs/github-publish-guide.md) 检查远程仓库、推送和 Actions 设置。

## 校验目录

新增或修改组件后，运行：

```powershell
python tools/validate_catalog.py --write-index
```

这个命令会检查 `catalog/*.md` 的必填字段、GitHub 地址、接入成本和评分格式，并更新 [catalog/index.json](catalog/index.json)。

## 维护原则

- 优先收录成熟、文档完整、许可证清楚的开源项目。
- 优先收录可以独立接入的模块。
- 记录取舍，不只记录优点。
- 条目要短，便于快速扫描。
- 只有当某个组件在真实项目中验证过，再把可运行示例放进 `components/`。
