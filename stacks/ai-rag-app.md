# AI RAG 应用组合蓝图

这个蓝图适合基于私有文档或结构化数据进行问答的 AI 应用。

## 模块地图

| 能力 | 主组件 | 备选组件 | 选择理由 | 主要风险 |
| --- | --- | --- | --- | --- |
| 前端 | Next.js | Vite + React | 适合聊天、上传、文档工作流 | 如果只是嵌入式工具，可能过重 |
| UI | shadcn/ui | Ant Design | 适合自定义聊天、上传和设置界面 | 团队需要负责组件风格一致性 |
| 后端 API | FastAPI | NestJS | Python 更适合 AI、数据处理和模型工具 | 大团队可能更偏好 TypeScript 服务结构 |
| 模型服务与推理网关 | LiteLLM | Ollama | 统一模型接口、密钥和成本治理 | 本地模型和云供应商的延迟与配额差异需要验证 |
| RAG 框架 | LlamaIndex | LangChain | 数据到 LLM 的检索流程较强 | 抽象可能掩盖检索质量问题 |
| 向量数据库与检索 | Qdrant | pgvector | 独立向量搜索，自托管路径清楚 | 需要多运维一个服务 |
| 认证 | Auth.js | Supabase Auth | Web 用户认证足够轻 | 不是完整企业 IAM 平台 |
| 数据库 | PostgreSQL | Supabase | 可靠保存元数据和应用数据 | 需要负责 schema 和迁移 |
| 部署 | Docker Compose + Coolify | Dokku | 适合自托管 API、前端和向量库 | 生产扩展需要额外规划 |
| 监控 | OpenTelemetry Collector | Prometheus | 更适合追踪 LLM 和检索延迟 | 初始配置成本高于基础日志 |

## 推荐优先验证

先验证文档导入、向量化、检索质量和答案生成，再打磨聊天界面。这个产品成败主要取决于检索质量。

## 适合

- 文档问答
- 知识库助手
- 内部搜索
- AI 客服副驾

## 不适合

- 不接入私有数据的简单聊天壳
- 确定性搜索已经足够的工作流
- 数据权限边界不清楚的产品
