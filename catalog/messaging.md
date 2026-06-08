# 消息队列组件

消息队列组件覆盖异步任务、事件流、队列、发布订阅和服务解耦。

## RabbitMQ

- GitHub: https://github.com/rabbitmq/rabbitmq-server
- 官网: https://www.rabbitmq.com
- 模块: 消息队列 / AMQP
- 技术栈: Erlang
- 许可证: MPL-2.0
- 适合: 任务队列、可靠消息投递、传统业务系统解耦和 AMQP 场景。
- 不适合: 需要超大规模事件流回放，或团队更偏向日志型消息系统。
- 接入成本: 中
- 替代方案: NATS, Kafka, Redis Queue
- 评分: 4/5
- 备注: 成熟稳健，适合大多数业务队列场景。

## NATS

- GitHub: https://github.com/nats-io/nats-server
- 官网: https://nats.io
- 模块: 消息队列 / 发布订阅 / 事件系统
- 技术栈: Go
- 许可证: Apache-2.0
- 适合: 轻量发布订阅、微服务通信、事件驱动系统和低运维消息基础设施。
- 不适合: 需要完整 Kafka 风格长期日志和复杂流处理生态的项目。
- 接入成本: 中
- 替代方案: RabbitMQ, Kafka, Redis Pub/Sub
- 评分: 4/5
- 备注: 对小到中型服务系统很友好。

## Apache Kafka

- GitHub: https://github.com/apache/kafka
- 官网: https://kafka.apache.org
- 模块: 消息队列 / 事件流
- 技术栈: Java, Scala
- 许可证: Apache-2.0
- 适合: 大规模事件流、日志回放、数据管道和多消费者数据分发。
- 不适合: 小项目只需要简单异步任务或轻量发布订阅。
- 接入成本: 高
- 替代方案: Redpanda, NATS JetStream, RabbitMQ
- 评分: 4/5
- 备注: 能力强但运维成本高，适合事件流成为核心基础设施时引入。

