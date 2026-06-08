# 数据质量组件

数据质量组件覆盖数据断言、规则校验、异常检测、数据测试、质量报告和管道前后置质量门禁；数据同步放在数据管道分类，资产目录、血缘和所有权放在数据治理分类。

## Great Expectations

- GitHub: https://github.com/great-expectations/great_expectations
- 官网: https://greatexpectations.io
- 模块: 数据质量 / 数据断言 / 质量文档
- 技术栈: Python, SQL, Pandas
- 许可证: Apache-2.0
- 适合: 数据团队需要用声明式期望规则验证表、列、分布、空值、唯一性和数据管道输出，并生成质量文档。
- 不适合: 只需要少量 SQL 检查，或团队不想维护 expectation suite、checkpoint 和数据上下文。
- 接入成本: 中
- 替代方案: Soda Core, Deequ, dbt tests
- 评分: 4/5
- 备注: 适合把数据质量规则版本化；生产前要设计规则所有权、失败阈值、告警和与调度系统的集成。

## Soda Core

- GitHub: https://github.com/sodadata/soda-core
- 官网: https://www.soda.io
- 模块: 数据质量 / 监控 / SQL 检查
- 技术栈: Python, SQL
- 许可证: Elastic License 2.0
- 适合: 需要用简单 YAML/SQL 风格规则检查数据质量、接入多种数据仓库并对接告警流程的团队。
- 不适合: 必须使用宽松开源许可证，或计划把它作为托管数据质量服务提供给第三方。
- 接入成本: 中
- 替代方案: Great Expectations, Deequ, dbt tests
- 评分: 4/5
- 备注: 规则表达上手快，但 ELv2 对托管服务有明确限制；使用前要确认许可证和商业边界。

## Deequ

- GitHub: https://github.com/awslabs/deequ
- 官网: https://github.com/awslabs/deequ
- 模块: 数据质量 / Spark / 约束校验
- 技术栈: Scala, Apache Spark
- 许可证: Apache-2.0
- 适合: Spark 数据湖、批处理管道和大规模表数据需要统计约束、异常检测、指标计算和质量校验的团队。
- 不适合: 不使用 Spark，或希望用轻量 Python/SQL 工具完成小规模质量检查的项目。
- 接入成本: 中
- 替代方案: Great Expectations, Soda Core, dbt tests
- 评分: 4/5
- 备注: 适合 Spark 生态的大数据质量校验；要规划指标存储、规则版本、失败处理和计算资源成本。
