# 存储组件

存储组件覆盖对象存储、文件上传、媒体资源和自托管文件服务。

## MinIO

- GitHub: https://github.com/minio/minio
- 官网: https://min.io
- 模块: 存储 / 对象存储
- 技术栈: Go, S3 API
- 许可证: AGPL-3.0
- 适合: 需要评估历史成熟的 S3 兼容对象存储，或能接受源码构建和 AGPL 义务的内部项目。
- 不适合: 需要活跃维护的社区仓库、预编译社区版本、宽松许可证，或只想使用完全托管云存储。
- 接入成本: 高
- 替代方案: SeaweedFS, Garage, Ceph
- 评分: 2/5
- 备注: GitHub 仓库已于 2026-04-25 归档并标注不再维护；新项目应优先评估替代方案。

## SeaweedFS

- GitHub: https://github.com/seaweedfs/seaweedfs
- 官网: https://github.com/seaweedfs/seaweedfs
- 模块: 存储 / 分布式文件系统 / 对象存储
- 技术栈: Go
- 许可证: Apache-2.0
- 适合: 需要分布式文件存储、对象存储、卷管理和较灵活部署方式的项目。
- 不适合: 只需要最简单文件上传，或团队不想维护存储集群。
- 接入成本: 高
- 替代方案: MinIO, Ceph, Garage
- 评分: 3/5
- 备注: 功能覆盖面广，适合有明确存储规模需求时评估。

## Uppy

- GitHub: https://github.com/transloadit/uppy
- 官网: https://uppy.io
- 模块: 存储 / 文件上传 / 前端
- 技术栈: TypeScript, JavaScript
- 许可证: MIT
- 适合: 构建浏览器文件上传、拖拽上传、断点续传和多来源文件选择体验。
- 不适合: 项目只需要一个最简单的单文件 input，或不需要前端上传体验控制。
- 接入成本: 低
- 替代方案: FilePond, Dropzone, 自研上传组件
- 评分: 4/5
- 备注: 适合和对象存储、后端签名上传流程组合使用。
