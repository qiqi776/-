# 数据治理与元数据组件

数据治理与元数据组件覆盖数据资产目录、元数据采集、数据血缘、数据所有权、质量上下文、术语表和跨数据平台的治理入口；数据同步和查询引擎仍分别放在数据管道、数据仓库分类。

## OpenMetadata

- GitHub: https://github.com/open-metadata/OpenMetadata
- 官网: https://open-metadata.org
- 模块: 数据治理 / 元数据目录 / 数据血缘
- 技术栈: Java, Python, TypeScript, Elasticsearch
- 许可证: Apache-2.0
- 适合: 团队需要统一管理数据库、数据仓库、仪表盘、管道、数据质量、血缘和业务术语。
- 不适合: 只需要轻量文档清单，或没有专人维护数据所有权和治理流程。
- 接入成本: 高
- 替代方案: DataHub, Amundsen, Atlan
- 评分: 4/5
- 备注: 覆盖面广，但生产前要验证连接器权限、元数据刷新频率、搜索索引和数据质量规则边界。

## DataHub

- GitHub: https://github.com/datahub-project/datahub
- 官网: https://datahubproject.io
- 模块: 数据治理 / 元数据平台 / 数据发现
- 技术栈: Java, Python, React, Kafka
- 许可证: Apache-2.0
- 适合: 中大型数据平台需要元数据摄取、数据发现、血缘、治理动作、实体模型扩展和平台级集成。
- 不适合: 小团队只需要简单数据目录，或无法承担 Kafka、搜索和多服务部署复杂度。
- 接入成本: 高
- 替代方案: OpenMetadata, Amundsen, Metacat
- 评分: 4/5
- 备注: 模型和生态强，适合平台团队；落地时要设计元数据所有权、变更审批和采集任务可观测性。

## Amundsen

- GitHub: https://github.com/amundsen-io/amundsen
- 官网: https://www.amundsen.io
- 模块: 数据治理 / 数据发现 / 元数据搜索
- 技术栈: Python, React, Neo4j, Elasticsearch
- 许可证: Apache-2.0
- 适合: 需要以数据发现和搜索为核心，快速建立数据资产入口、表字段说明和使用上下文的团队。
- 不适合: 需要一体化数据质量、复杂治理工作流和活跃平台路线图的组织。
- 接入成本: 中
- 替代方案: OpenMetadata, DataHub, Metacat
- 评分: 3/5
- 备注: 数据发现体验清晰，但活跃度和治理覆盖面要单独评估；适合作为轻量目录或迁移前过渡方案。
