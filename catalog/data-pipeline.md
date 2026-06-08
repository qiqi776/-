# 数据管道与数据集成组件

数据管道与数据集成组件覆盖 ELT、ETL、数据源连接器、批量同步、增量加载、数据仓库装载和代码化数据移动流程。

## Airbyte

- GitHub: https://github.com/airbytehq/airbyte
- 官网: https://airbyte.com
- 模块: 数据管道 / ELT / 连接器平台
- 技术栈: Java, Python, Docker, Kubernetes
- 许可证: Elastic License 2.0
- 适合: 团队需要大量现成连接器，把 SaaS、数据库、文件和 API 数据同步到数据仓库、湖仓或分析系统。
- 不适合: 团队必须使用宽松开源许可证，或计划把它作为托管数据同步服务提供给第三方。
- 接入成本: 高
- 替代方案: Meltano, dlt, Fivetran
- 评分: 4/5
- 备注: 连接器生态强，但 ELv2 对托管服务有明确限制；生产前要验证连接器质量、状态存储、增量同步和失败重跑策略。

## Meltano

- GitHub: https://github.com/meltano/meltano
- 官网: https://meltano.com
- 模块: 数据管道 / Singer / ELT 编排
- 技术栈: Python, Singer, CLI
- 许可证: MIT
- 适合: 数据团队希望用代码和配置管理 ELT 项目、Singer tap/target、环境变量、作业调度和版本化数据集成流程。
- 不适合: 需要大量可视化托管连接器管理，或不想维护 Singer 插件兼容性的团队。
- 接入成本: 中
- 替代方案: Airbyte, dlt, Dagster
- 评分: 4/5
- 备注: 适合 GitOps 风格的数据集成；要治理插件版本、凭据注入、环境隔离和目标仓库 schema 演进。

## dlt

- GitHub: https://github.com/dlt-hub/dlt
- 官网: https://dlthub.com
- 模块: 数据管道 / Python ELT / 数据装载
- 技术栈: Python
- 许可证: Apache-2.0
- 适合: Python 团队需要把 API、数据库或文件数据以代码方式抽取、规范化并装载到数据仓库、湖仓或向量数据库。
- 不适合: 需要非技术用户可视化配置大量连接器，或团队不愿用代码维护数据抽取逻辑。
- 接入成本: 中
- 替代方案: Meltano, Airbyte, Dagster
- 评分: 4/5
- 备注: 适合轻量到中型数据集成和应用内数据同步；生产前要验证 schema 变更、幂等、断点续跑和目标端权限。
