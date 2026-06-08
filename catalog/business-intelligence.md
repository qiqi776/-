# 报表与商业智能组件

报表与商业智能组件覆盖 BI 平台、SQL 查询、数据源连接、仪表盘、探索分析、权限共享、定时报表和嵌入式分析；底层 OLAP/数据湖查询放在数据仓库分类，前端图表库和可视化 SDK 放在图表与可视化分类，产品行为分析放在产品分析分类。

## Apache Superset

- GitHub: https://github.com/apache/superset
- 官网: https://superset.apache.org/
- 模块: BI / 数据探索 / 仪表盘
- 技术栈: Python, Flask, React, TypeScript, SQLAlchemy
- 许可证: Apache-2.0
- 适合: 需要企业级 BI、SQL Lab、多数据源连接、复杂仪表盘、权限管理、图表插件和数据探索能力的团队。
- 不适合: 只需要几个嵌入式图表、轻量运营报表，或没有能力维护 Python/前端/元数据库/缓存/异步任务组合的项目。
- 接入成本: 高
- 替代方案: Metabase, Redash, Evidence
- 评分: 5/5
- 备注: 能力强但运维面广；生产前要确认元数据库、缓存、Celery、权限模型、数据库凭据、查询隔离、导出策略和资源限制。

## Metabase

- GitHub: https://github.com/metabase/metabase
- 官网: https://metabase.com
- 模块: BI / 自助分析 / 嵌入式分析
- 技术栈: Clojure, Java, React, TypeScript, JDBC
- 许可证: AGPL-3.0 / Commercial
- 适合: 需要快速给业务团队提供自助查询、问答式探索、仪表盘、告警、嵌入式分析和常见数据库连接的产品或内部系统。
- 不适合: 无法接受 AGPL-3.0 或商业许可证边界，或需要完全自定义复杂数据建模和企业治理流程的场景。
- 接入成本: 中
- 替代方案: Apache Superset, Redash, Lightdash
- 评分: 5/5
- 备注: 上手快、体验成熟；上线前要确认开源版/商业版边界、数据源权限、SSO、嵌入方式、查询缓存和敏感数据暴露风险。

## Redash

- GitHub: https://github.com/getredash/redash
- 官网: https://redash.io/
- 模块: BI / SQL 查询 / 仪表盘
- 技术栈: Python, Flask, React, PostgreSQL, Redis
- 许可证: BSD-2-Clause
- 适合: 需要以 SQL 查询为中心连接多数据源、制作图表和仪表盘、共享查询结果、设置定时报表的技术团队。
- 不适合: 需要现代拖拽式 BI 建模、复杂权限治理、活跃企业支持，或不想维护 Python Worker、PostgreSQL 和 Redis 的项目。
- 接入成本: 中
- 替代方案: Apache Superset, Metabase, Lightdash
- 评分: 4/5
- 备注: SQL 驱动、许可证宽松；选型时要复核维护活跃度、数据源驱动、查询队列、权限隔离、升级路径和运维成本。
