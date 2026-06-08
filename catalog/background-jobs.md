# 后台任务与作业队列组件

后台任务与作业队列组件覆盖应用内异步任务、worker、重试、延迟任务、定时触发和短周期作业执行；消息中间件放在消息队列分类，跨服务长事务和 DAG 编排放在工作流分类。

## Celery

- GitHub: https://github.com/celery/celery
- 官网: https://docs.celeryq.dev
- 模块: 后台任务 / Python Worker / 分布式任务队列
- 技术栈: Python, Redis, RabbitMQ
- 许可证: BSD-3-Clause
- 适合: Python / Django / Flask 项目需要成熟 worker、任务重试、定时任务、结果后端和多 broker 支持。
- 不适合: 只需要极轻量本地任务，或团队不想维护 broker、worker、beat 和结果存储。
- 接入成本: 中
- 替代方案: ARQ, RQ, Dramatiq
- 评分: 4/5
- 备注: 生态成熟但配置面较大；生产前要设计幂等、超时、重试、任务序列化和 worker 监控。

## BullMQ

- GitHub: https://github.com/taskforcesh/bullmq
- 官网: https://docs.bullmq.io
- 模块: 后台任务 / Node.js Queue / Redis Worker
- 技术栈: TypeScript, Node.js, Redis
- 许可证: MIT
- 适合: Node.js / NestJS 项目需要 Redis 驱动的队列、延迟任务、重复任务、优先级、并发 worker 和可观察任务状态。
- 不适合: 不想依赖 Redis，或需要跨语言统一 worker 协议和企业级编排平台的系统。
- 接入成本: 中
- 替代方案: Bee-Queue, Agenda, Temporal
- 评分: 4/5
- 备注: 和 Node 生态贴合；要规划 Redis 高可用、job 幂等、失败队列、任务版本和清理策略。

## ARQ

- GitHub: https://github.com/python-arq/arq
- 官网: https://arq-docs.helpmanual.io
- 模块: 后台任务 / Async Python / Redis Queue
- 技术栈: Python, asyncio, Redis
- 许可证: MIT
- 适合: FastAPI、asyncio 服务和轻中量 Python 项目需要简单 Redis 队列、异步 worker、延迟任务和定时任务。
- 不适合: 需要 Celery 级生态、复杂 routing、多 broker，或团队大量使用同步 Python 框架。
- 接入成本: 低
- 替代方案: Celery, RQ, Dramatiq
- 评分: 4/5
- 备注: 轻量且适合 async 应用；生产前仍要处理任务幂等、Redis 持久化、重试上限和失败告警。
