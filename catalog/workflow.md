# 工作流组件

工作流组件覆盖任务编排、调度、定时任务和长事务流程；数据连接器、ELT/ETL 和装载流程单独放在数据管道分类。

## Temporal

- GitHub: https://github.com/temporalio/temporal
- 官网: https://temporal.io
- 模块: 工作流 / Durable Execution / 长事务
- 技术栈: Go, Java, TypeScript, Python
- 许可证: MIT
- 适合: 需要可靠执行长时间业务流程、重试、补偿、超时和跨服务状态机的系统。
- 不适合: 只需要简单 cron 或一次性后台任务，且不想引入独立服务和 SDK 约束的项目。
- 接入成本: 高
- 替代方案: Prefect, Apache Airflow, 自研状态机
- 评分: 4/5
- 备注: 能力强，适合把业务流程可靠性作为核心需求时引入。

## Prefect

- GitHub: https://github.com/PrefectHQ/prefect
- 官网: https://www.prefect.io
- 模块: 工作流 / 数据管道 / Python 自动化
- 技术栈: Python
- 许可证: Apache-2.0
- 适合: Python 数据任务、ETL、定时自动化和需要可观察运行状态的脚本编排。
- 不适合: 主要是跨语言业务长事务，或团队不想围绕 Python 构建工作流的项目。
- 接入成本: 中
- 替代方案: Apache Airflow, Dagster, Temporal
- 评分: 4/5
- 备注: 对数据和自动化团队友好，生产使用要设计任务状态和部署方式。

## Apache Airflow

- GitHub: https://github.com/apache/airflow
- 官网: https://airflow.apache.org
- 模块: 工作流 / 数据管道 / 调度
- 技术栈: Python
- 许可证: Apache-2.0
- 适合: 批处理数据管道、DAG 调度、定时任务依赖和成熟数据平台生态。
- 不适合: 低延迟业务流程、事件驱动长事务，或不想维护调度器和元数据库的项目。
- 接入成本: 高
- 替代方案: Prefect, Dagster, Kestra
- 评分: 4/5
- 备注: 生态成熟但偏重，适合数据平台而不是普通 Web 小项目的默认后台任务方案。
