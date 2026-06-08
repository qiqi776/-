# 容器与镜像构建组件

容器与镜像构建组件覆盖本地容器运行、OCI 镜像构建、镜像缓存、镜像仓库、签名扫描集成和交付制品管理。

## Podman

- GitHub: https://github.com/containers/podman
- 官网: https://podman.io
- 模块: 容器 / 本地运行时 / Docker 替代
- 技术栈: Go, Linux, OCI
- 许可证: Apache-2.0
- 适合: 需要无守护进程、rootless 容器、本地开发和服务器容器管理，并希望兼容 Docker CLI 习惯的团队。
- 不适合: 团队强依赖 Docker Desktop 生态，或需要完整 Kubernetes 编排能力。
- 接入成本: 中
- 替代方案: Docker Engine, containerd, nerdctl
- 评分: 4/5
- 备注: 适合开发机和服务器侧容器运行；要确认 Windows/macOS 虚拟化体验、Compose 兼容性和镜像网络配置。

## BuildKit

- GitHub: https://github.com/moby/buildkit
- 官网: https://github.com/moby/buildkit
- 模块: 容器 / 镜像构建
- 技术栈: Go, OCI, Dockerfile
- 许可证: Apache-2.0
- 适合: 需要高性能 Dockerfile/OCI 镜像构建、并行构建、缓存复用、多平台镜像和 CI 构建加速的团队。
- 不适合: 只需要最简单本地镜像构建，或团队不想理解缓存、构建上下文和远程 builder。
- 接入成本: 中
- 替代方案: Kaniko, Buildah, Docker Buildx
- 评分: 4/5
- 备注: 是现代 Docker 构建能力的核心；要治理缓存来源、secret mount、SBOM/签名流程和多架构构建环境。

## Harbor

- GitHub: https://github.com/goharbor/harbor
- 官网: https://goharbor.io
- 模块: 容器 / 镜像仓库 / 制品治理
- 技术栈: Go, Docker, OCI Registry
- 许可证: Apache-2.0
- 适合: 企业或团队需要自托管镜像仓库、项目权限、复制策略、漏洞扫描、镜像签名和制品生命周期管理。
- 不适合: 只需要公共镜像仓库，或团队不想维护数据库、对象存储和仓库高可用。
- 接入成本: 高
- 替代方案: Docker Distribution, Zot, GitLab Container Registry
- 评分: 4/5
- 备注: 适合组织级制品治理；部署前要规划存储、备份、扫描器、保留策略和镜像复制拓扑。
