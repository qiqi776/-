# 缓存组件

缓存组件覆盖内存缓存、分布式缓存、任务状态和会话存储。

## Memcached

- GitHub: https://github.com/memcached/memcached
- 官网: https://memcached.org
- 模块: 缓存 / 内存键值缓存
- 技术栈: C
- 许可证: BSD-3-Clause
- 适合: 页面片段、查询结果、会话辅助和临时热点数据缓存。
- 不适合: 需要复杂数据结构、持久化、Lua 脚本或 Redis 兼容协议。
- 接入成本: 低
- 替代方案: Valkey, KeyDB, Apache Ignite
- 评分: 4/5
- 备注: 成熟轻量的内存缓存默认候选，适合只需要简单 key-value 缓存的项目。

## Valkey

- GitHub: https://github.com/valkey-io/valkey
- 官网: https://valkey.io
- 模块: 缓存 / Redis 兼容
- 技术栈: C
- 许可证: BSD-3-Clause
- 适合: 需要 Redis 兼容能力，同时希望使用宽松开源许可证的项目。
- 不适合: 团队依赖 Redis 官方商业生态或特定 Redis 新特性。
- 接入成本: 中
- 替代方案: Memcached, KeyDB, Apache Ignite
- 评分: 4/5
- 备注: 适合作为 Redis 许可证变化后的开源默认候选。

## KeyDB

- GitHub: https://github.com/Snapchat/KeyDB
- 官网: https://docs.keydb.dev
- 模块: 缓存 / Redis 兼容 / 多线程缓存
- 技术栈: C++
- 许可证: BSD-3-Clause
- 适合: 需要 Redis 兼容接口、多线程吞吐和宽松开源许可证的项目。
- 不适合: 团队需要最强社区动能、最新 Redis 生态特性或完全托管缓存服务。
- 接入成本: 中
- 替代方案: Valkey, Memcached, Apache Ignite
- 评分: 4/5
- 备注: Redis 分支方向的成熟候选，进入项目时仍要验证命令兼容性和部署镜像来源。
