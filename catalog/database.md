# 数据库组件

数据库组件覆盖数据库引擎、ORM 和后端即服务平台；embedding 向量存储、RAG 检索和相似度搜索放在向量数据库与检索分类。

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

## SQLite

- GitHub: https://github.com/sqlite/sqlite
- 官网: https://www.sqlite.org
- 模块: 数据库 / 嵌入式关系型数据库
- 技术栈: C, SQL
- 许可证: Public Domain
- 适合: 本地优先应用、移动端、桌面端、边缘节点、测试环境、小型服务和需要零运维嵌入式数据库的项目。
- 不适合: 高并发多写入服务、复杂权限隔离、多租户数据库后端，或需要独立数据库服务器运维能力的系统。
- 接入成本: 低
- 替代方案: PostgreSQL, DuckDB, LiteFS
- 评分: 4/5
- 备注: GitHub 仓库是官方镜像，上游以 SQLite Fossil 仓库为准；上线前要确认并发写入、备份、迁移、加密、文件锁和部署介质。
