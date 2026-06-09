# 存储组件

存储组件覆盖对象存储、文件上传、媒体资源和自托管文件服务。

## Ceph

- GitHub: https://github.com/ceph/ceph
- 官网: https://ceph.io
- 模块: 存储 / 对象存储 / 块存储 / 文件存储
- 技术栈: C++, Python, RADOS, S3 API
- 许可证: LGPL-2.1-or-3.0（主体）/ BSD-style（部分）
- 适合: 需要生产级对象存储、块存储、共享文件系统或统一分布式存储平台。
- 不适合: 小团队只需要简单文件上传，或没有能力运维分布式存储集群。
- 接入成本: 高
- 替代方案: Garage, Rook, Uppy
- 评分: 4/5
- 备注: 成熟度和生产采用度高，但架构和运维复杂度也高，适合作为大型项目存储候选。

## Garage

- GitHub: https://github.com/deuxfleurs-org/garage
- 官网: https://garagehq.deuxfleurs.fr
- 模块: 存储 / S3 兼容对象存储
- 技术栈: Rust, S3 API
- 许可证: AGPL-3.0
- 适合: 自托管中小规模 S3 兼容对象存储，尤其是多地点轻量部署。
- 不适合: 需要大型企业级存储生态、托管云服务或无法接受 AGPL 义务的项目。
- 接入成本: 中
- 替代方案: Ceph, Rook, Uppy
- 评分: 4/5
- 备注: 轻量、S3 兼容且面向自托管场景，适合在小到中等规模项目中评估。

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
