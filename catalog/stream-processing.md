# 流处理组件

流处理组件覆盖持续事件流计算、窗口聚合、状态处理、事件时间、实时转换和流批一体任务；消息持久化放在消息队列分类，批量同步和连接器装载放在数据管道分类。

## Apache Flink

- GitHub: https://github.com/apache/flink
- 官网: https://flink.apache.org
- 模块: 流处理 / 状态计算 / 事件时间
- 技术栈: Java, Scala, Python
- 许可证: Apache-2.0
- 适合: 需要高吞吐低延迟流计算、窗口聚合、Exactly-once 状态、复杂事件处理和流批一体数据应用的平台团队。
- 不适合: 只需要简单消息转发、轻量 ETL，或团队没有能力维护集群、checkpoint 和状态后端。
- 接入成本: 高
- 替代方案: Apache Beam, Kafka Streams, Spark Structured Streaming
- 评分: 4/5
- 备注: 能力强但运维要求高；生产前要验证状态大小、checkpoint 存储、反压、作业升级和灾备恢复。

## Kafka Streams

- GitHub: https://github.com/apache/kafka
- 官网: https://kafka.apache.org/documentation/streams
- 模块: 流处理 / Kafka 应用库 / 状态转换
- 技术栈: Java, Scala
- 许可证: Apache-2.0
- 适合: 已经使用 Kafka，且希望在普通应用进程内完成事件转换、聚合、Join、状态存储和拓扑部署的团队。
- 不适合: 需要跨多种流引擎运行、独立作业调度平台，或团队不想把流处理逻辑绑定在 Kafka 生态。
- 接入成本: 中
- 替代方案: Apache Flink, Apache Beam, Faust
- 评分: 4/5
- 备注: 适合 Kafka 原生实时业务逻辑；要设计 topic、分区、状态目录、重平衡和应用版本兼容策略。

## Apache Beam

- GitHub: https://github.com/apache/beam
- 官网: https://beam.apache.org
- 模块: 流处理 / 批流统一 / 数据处理 SDK
- 技术栈: Java, Python, Go
- 许可证: Apache-2.0
- 适合: 希望用统一模型编写批处理和流处理，并在 Flink、Spark、Google Dataflow 等 Runner 之间迁移的数据工程团队。
- 不适合: 只会固定使用单一执行引擎，或项目更看重引擎原生 API 和最低运行复杂度。
- 接入成本: 高
- 替代方案: Apache Flink, Spark Structured Streaming, Kafka Streams
- 评分: 4/5
- 备注: 抽象层带来可移植性，也会增加调试和 Runner 差异成本；要先验证窗口、触发器和状态语义。
