# 备份与恢复组件

备份与恢复组件覆盖通用文件备份、数据库备份、Kubernetes 集群备份、灾难恢复和恢复演练。

## restic

- GitHub: https://github.com/restic/restic
- 官网: https://restic.net
- 模块: 备份与恢复 / 通用备份
- 技术栈: Go, CLI
- 许可证: BSD-2-Clause
- 适合: 需要加密、去重、增量备份，并把文件、目录或服务器数据备份到 S3、SFTP、Backblaze 等后端。
- 不适合: 需要数据库一致性备份但没有快照/停写策略，或需要集中式企业备份管理台。
- 接入成本: 中
- 替代方案: BorgBackup, Kopia, Duplicati
- 评分: 4/5
- 备注: 适合自托管服务器和文件数据保护；必须定期做恢复演练，而不只是确认备份任务成功。

## pgBackRest

- GitHub: https://github.com/pgbackrest/pgbackrest
- 官网: https://pgbackrest.org
- 模块: 备份与恢复 / PostgreSQL
- 技术栈: C, PostgreSQL, CLI
- 许可证: MIT
- 适合: PostgreSQL 生产库需要物理备份、增量备份、归档 WAL、时间点恢复和备份校验。
- 不适合: 非 PostgreSQL 数据库，或团队只需要开发环境里的简单 `pg_dump`。
- 接入成本: 高
- 替代方案: Barman, WAL-G, pg_dump
- 评分: 4/5
- 备注: 2026-04 曾发布维护者不足公告，2026-05 又宣布继续维护；生产采用前要复核当前维护状态和恢复流程。

## Velero

- GitHub: https://github.com/vmware-tanzu/velero
- 官网: https://velero.io
- 模块: 备份与恢复 / Kubernetes 灾备
- 技术栈: Go, Kubernetes
- 许可证: Apache-2.0
- 适合: Kubernetes 集群需要备份资源对象、持久卷快照，并支持迁移、灾难恢复和命名空间级恢复。
- 不适合: 不使用 Kubernetes，或应用状态主要在外部数据库里且没有对应数据库备份策略。
- 接入成本: 高
- 替代方案: Kasten K10, Stash, 云厂商备份服务
- 评分: 4/5
- 备注: 适合集群级灾备，但不能替代数据库级一致性备份；要验证 CSI 快照、对象存储权限和恢复顺序。
