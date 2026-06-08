# 数据库迁移组件

数据库迁移组件覆盖 Schema 版本管理、SQL 迁移、声明式数据库变更、回滚策略和数据库变更审计。

## Flyway

- GitHub: https://github.com/flyway/flyway
- 官网: https://flywaydb.org
- 模块: 数据库迁移 / SQL 版本管理
- 技术栈: Java, SQL, CLI
- 许可证: Apache-2.0
- 适合: 团队希望用显式 SQL 文件管理数据库版本，并在 CI/CD 或应用启动流程中执行迁移。
- 不适合: 需要自动生成复杂迁移、可视化变更审批，或团队不能维护严格的迁移命名和执行顺序。
- 接入成本: 中
- 替代方案: golang-migrate, Atlas, Liquibase
- 评分: 4/5
- 备注: 适合关系型数据库的稳定迁移流程；要规定回滚策略、基线版本和生产执行权限。

## golang-migrate

- GitHub: https://github.com/golang-migrate/migrate
- 官网: https://github.com/golang-migrate/migrate
- 模块: 数据库迁移 / CLI / Go
- 技术栈: Go, SQL, CLI
- 许可证: MIT
- 适合: Go 服务或轻量后端项目需要简单、可脚本化、支持多数据库的 up/down 迁移工具。
- 不适合: 需要图形化审批、复杂依赖分析，或希望工具自动理解完整数据库 Schema 状态。
- 接入成本: 低
- 替代方案: Flyway, Atlas, Goose
- 评分: 4/5
- 备注: 简单可靠但约束少；团队要自己规范事务、锁、回滚脚本和迁移文件评审。

## Atlas

- GitHub: https://github.com/ariga/atlas
- 官网: https://atlasgo.io
- 模块: 数据库迁移 / 声明式 Schema
- 技术栈: Go, HCL, SQL
- 许可证: Apache-2.0
- 适合: 需要从声明式 Schema、ORM 或数据库现状生成迁移，并在 CI 中检查漂移和变更风险。
- 不适合: 团队只接受手写 SQL，或项目数据库模式非常简单、不需要额外治理工具。
- 接入成本: 中
- 替代方案: Flyway, golang-migrate, Prisma Migrate
- 评分: 4/5
- 备注: 适合把数据库结构纳入工程化流程；生产前要验证生成 SQL、权限边界和数据库漂移检测策略。
