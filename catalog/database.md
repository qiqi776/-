# 数据库组件

数据库组件覆盖数据库引擎、ORM、后端即服务平台和向量存储。

## PostgreSQL

- GitHub: https://github.com/postgres/postgres
- 官网: https://www.postgresql.org
- 模块: 数据库 / 关系型数据库
- 技术栈: C, SQL
- 许可证: PostgreSQL License
- 适合: 通用关系型数据、事务系统、分析扩展和长期产品数据库。
- 不适合: 只需要嵌入式本地存储，或需要高度专用的非关系型引擎。
- 接入成本: 中
- 替代方案: MySQL, SQLite, MariaDB
- 评分: 5/5
- 备注: 大多数严肃应用的强默认数据库选择。

## Prisma

- GitHub: https://github.com/prisma/prisma
- 官网: https://www.prisma.io
- 模块: 数据库 / ORM
- 技术栈: TypeScript, Rust
- 许可证: Apache-2.0
- 适合: 需要类型化数据库访问和清晰 schema 工作流的 TypeScript 应用。
- 不适合: 团队偏好手写 SQL，或需要 Prisma 不支持的数据库模式。
- 接入成本: 中
- 替代方案: Drizzle ORM, TypeORM, Sequelize
- 评分: 4/5
- 备注: 开发体验好，但 schema 和迁移流程会成为架构的一部分。

## Qdrant

- GitHub: https://github.com/qdrant/qdrant
- 官网: https://qdrant.tech
- 模块: 数据库 / 向量搜索 / AI
- 技术栈: Rust
- 许可证: Apache-2.0
- 适合: 向量搜索、RAG、语义搜索，以及需要独立向量数据库的 AI 应用。
- 不适合: 只需要简单关键词搜索，或现有数据库扩展已经足够。
- 接入成本: 中
- 替代方案: Milvus, Chroma, Weaviate, pgvector
- 评分: 4/5
- 备注: 自托管向量搜索的强候选。

