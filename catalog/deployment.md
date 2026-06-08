# 部署组件

部署组件覆盖自托管、PaaS、应用托管和基础设施胶水。

## Dokku

- GitHub: https://github.com/dokku/dokku
- 官网: https://dokku.com
- 模块: 部署 / 自托管 PaaS
- 技术栈: Shell, Docker
- 许可证: MIT
- 适合: 小团队在自有服务器上获得类似 Heroku 的 Git push 部署体验。
- 不适合: 需要多节点编排、复杂 Kubernetes 运维或深度云平台抽象的项目。
- 接入成本: 中
- 替代方案: Coolify, CapRover, Fly.io
- 评分: 4/5
- 备注: 小应用自托管部署的低摩擦选择。

## Coolify

- GitHub: https://github.com/coollabsio/coolify
- 官网: https://coolify.io
- 模块: 部署 / 自托管 PaaS
- 技术栈: PHP, Svelte, Docker
- 许可证: Apache-2.0
- 适合: 自托管部署面板、应用托管、数据库和服务管理。
- 不适合: 团队希望服务器状态尽量少，或完全依赖托管平台运维。
- 接入成本: 中
- 替代方案: Dokku, CapRover, Railway, Render
- 评分: 4/5
- 备注: 当项目需要自托管平台界面，而不只是 CLI 部署时很有用。

## Kubernetes

- GitHub: https://github.com/kubernetes/kubernetes
- 官网: https://kubernetes.io
- 模块: 部署 / 编排
- 技术栈: Go
- 许可证: Apache-2.0
- 适合: 多服务平台、编排、扩缩容和基础设施标准化。
- 不适合: 可以运行在单服务器或简单 PaaS 上的小应用。
- 接入成本: 高
- 替代方案: Docker Compose, Nomad, 托管 PaaS
- 评分: 4/5
- 备注: 在正确规模下有价值，过早采用会很贵。

