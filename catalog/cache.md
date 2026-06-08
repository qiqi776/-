# 缓存组件

缓存组件覆盖内存缓存、分布式缓存、任务状态和会话存储。

## Redis

- GitHub: https://github.com/redis/redis
- 官网: https://redis.io
- 模块: 缓存 / 数据结构服务
- 技术栈: C
- 许可证: RSALv2 / SSPLv1 / AGPL-3.0（Redis 8+）
- 适合: 缓存、排行榜、会话、速率限制、队列辅助和低延迟数据结构需求。
- 不适合: 团队必须使用宽松开源许可证，或不想接受 Redis 新许可证限制。
- 接入成本: 中
- 替代方案: Valkey, KeyDB, Dragonfly
- 评分: 4/5
- 备注: Redis 7.4 到 7.8 是 RSALv2 / SSPLv1；Redis 8+ 增加 AGPL-3.0 选项，仍需按版本审查。

## Valkey

- GitHub: https://github.com/valkey-io/valkey
- 官网: https://valkey.io
- 模块: 缓存 / Redis 兼容
- 技术栈: C
- 许可证: BSD-3-Clause
- 适合: 需要 Redis 兼容能力，同时希望使用宽松开源许可证的项目。
- 不适合: 团队依赖 Redis 官方商业生态或特定 Redis 新特性。
- 接入成本: 中
- 替代方案: Redis, KeyDB, Dragonfly
- 评分: 4/5
- 备注: 适合作为 Redis 许可证变化后的开源默认候选。

## Dragonfly

- GitHub: https://github.com/dragonflydb/dragonfly
- 官网: https://www.dragonflydb.io
- 模块: 缓存 / Redis 兼容 / 高性能缓存
- 技术栈: C++
- 许可证: BUSL-1.1
- 适合: 需要 Redis 兼容接口和更高吞吐缓存能力的项目。
- 不适合: 团队必须使用当前完全开源许可证，或对 BSL 有合规限制。
- 接入成本: 中
- 替代方案: Redis, Valkey, KeyDB
- 评分: 3/5
- 备注: 性能方向明确，但许可证和兼容性需要评估。
