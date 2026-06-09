# 数据管道与数据集成组件

数据管道与数据集成组件覆盖 ELT、ETL、数据源连接器、批量同步、增量加载、数据仓库装载和代码化数据移动流程。

## Dagster

- GitHub: https://github.com/dagster-io/dagster
- 官网: https://dagster.io
- 模块: 数据管道 / 数据资产编排 / 工作流编排
- 技术栈: Python, DAG, Assets
- 许可证: Apache-2.0
- 适合: 团队需要用数据资产模型编排 ETL、ELT、数据仓库任务、批处理作业和跨系统依赖。
- 不适合: 主要需求是无代码连接器市场，或希望非技术用户直接配置 SaaS 数据同步。
- 接入成本: 高
- 替代方案: Meltano, dlt, Apache Airflow
- 评分: 4/5
- 备注: 适合把数据资产、调度和观测结合起来；生产前要治理资产定义、资源配置、运行隔离和告警。

## Meltano

- GitHub: https://github.com/meltano/meltano
- 官网: https://meltano.com
- 模块: 数据管道 / Singer / ELT 编排
- 技术栈: Python, Singer, CLI
- 许可证: MIT
- 适合: 数据团队希望用代码和配置管理 ELT 项目、Singer tap/target、环境变量、作业调度和版本化数据集成流程。
- 不适合: 需要大量可视化托管连接器管理，或不想维护 Singer 插件兼容性的团队。
- 接入成本: 中
- 替代方案: Dagster, dlt, Apache Airflow
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
- 替代方案: Meltano, Dagster, Apache Airflow
- 评分: 4/5
- 备注: 适合轻量到中型数据集成和应用内数据同步；生产前要验证 schema 变更、幂等、断点续跑和目标端权限。
