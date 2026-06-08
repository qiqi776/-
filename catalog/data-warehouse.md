# 数据仓库与 OLAP 组件

数据仓库与 OLAP 组件覆盖列式分析数据库、嵌入式分析引擎、湖仓查询、跨数据源查询和面向报表/分析的高吞吐读写场景。

## ClickHouse

- GitHub: https://github.com/ClickHouse/ClickHouse
- 官网: https://clickhouse.com
- 模块: 数据仓库 / OLAP / 列式数据库
- 技术栈: C++, SQL
- 许可证: Apache-2.0
- 适合: 高吞吐事件分析、产品指标、日志分析、实时仪表盘和需要自托管列式 OLAP 数据库的团队。
- 不适合: 需要强事务、多表更新、复杂 OLTP 约束或团队没有能力维护分片、压缩和查询调优的项目。
- 接入成本: 高
- 替代方案: Apache Druid, Apache Pinot, PostgreSQL
- 评分: 4/5
- 备注: 性能强但数据建模和运维要求高；生产前要设计分区键、排序键、TTL、物化视图和冷热数据策略。

## DuckDB

- GitHub: https://github.com/duckdb/duckdb
- 官网: https://duckdb.org
- 模块: 数据仓库 / 嵌入式 OLAP / 本地分析
- 技术栈: C++, SQL
- 许可证: MIT
- 适合: 本地分析、Notebook、数据应用、轻量报表、文件数据查询，以及不想部署独立 OLAP 服务的场景。
- 不适合: 多用户高并发线上数据仓库，或需要长期运行的分布式查询服务。
- 接入成本: 低
- 替代方案: SQLite, ClickHouse, Polars
- 评分: 5/5
- 备注: 很适合项目早期和分析原型；要注意文件并发、数据体量、持久化位置和与生产数据源的边界。

## Trino

- GitHub: https://github.com/trinodb/trino
- 官网: https://trino.io
- 模块: 数据仓库 / 分布式 SQL / 湖仓查询
- 技术栈: Java, SQL
- 许可证: Apache-2.0
- 适合: 团队需要跨对象存储、Hive/Iceberg、关系数据库和多种数据源做交互式分布式 SQL 查询。
- 不适合: 只需要单一数据库报表，或团队没有能力维护协调节点、工作节点、连接器和查询资源治理。
- 接入成本: 高
- 替代方案: Presto, Spark SQL, ClickHouse
- 评分: 4/5
- 备注: 适合湖仓和多源查询平台；生产前要规划连接器权限、查询队列、资源组、缓存和元数据治理。
