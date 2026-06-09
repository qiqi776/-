# 包与制品仓库组件

包与制品仓库组件覆盖私有 npm、Maven、PyPI、NuGet、RubyGems 仓库、二进制制品、依赖代理、制品权限、保留策略和发布治理。它解决“构建产物和内部包如何被发布、缓存、审计和复用”的问题；源码托管放在代码托管分类，容器运行与镜像构建放在容器与镜像构建分类，CI 流水线放在 CI/CD 分类，SBOM 与许可证治理放在 SBOM 分类。

## Verdaccio

- GitHub: https://github.com/verdaccio/verdaccio
- 官网: https://verdaccio.org
- 模块: 包与制品仓库 / npm 私有仓库 / 依赖代理
- 技术栈: TypeScript, Node.js, npm, pnpm, Yarn
- 许可证: MIT
- 适合: Node.js 或前端团队需要快速搭建私有 npm 仓库、上游代理缓存、scope 包发布和内部组件共享。
- 不适合: 需要 Maven、NuGet、PyPI、OCI 等多语言制品统一治理，或需要复杂企业级权限、审计和高可用能力的场景。
- 接入成本: 低
- 替代方案: Nexus Repository, Pulp, GitLab Package Registry
- 评分: 4/5
- 备注: 先确认存储目录、上游 npm 源、认证方式、包保留策略、CI 发布 token、lockfile registry 配置和缓存污染防护。

## Nexus Repository

- GitHub: https://github.com/sonatype/nexus-public
- 官网: https://www.sonatype.com/products/sonatype-nexus-repository
- 模块: 包与制品仓库 / 通用制品库 / 依赖代理
- 技术栈: Java, JVM, Maven, npm, NuGet, PyPI, Docker
- 许可证: EPL-1.0
- 适合: 中大型团队需要统一托管 Maven、npm、NuGet、PyPI、Docker 等制品，并配置 hosted、proxy、group 仓库、权限、保留策略和依赖缓存。
- 不适合: 只需要一个轻量 npm 私有仓库的小团队，或无法承担 JVM 服务、存储、备份和商业功能边界评估的项目。
- 接入成本: 高
- 替代方案: Verdaccio, Pulp, GitLab Package Registry
- 评分: 4/5
- 备注: 开源核心和商业能力需要提前划边界；生产前要验证制品格式、blob storage、备份恢复、清理策略、LDAP/SSO、漏洞策略和迁移路径。

## Pulp

- GitHub: https://github.com/pulp/pulpcore
- 官网: https://pulpproject.org
- 模块: 包与制品仓库 / 内容仓库 / 多格式镜像分发
- 技术栈: Python, Django, PostgreSQL, Redis
- 许可证: GPL-2.0-or-later
- 适合: 团队需要镜像、托管和分发多来源软件内容，通过插件管理 Python、RPM、容器、Ansible、Debian 等仓库内容。
- 不适合: 只需要轻量 npm 私有仓库，或项目许可证策略不能接受 GPL-2.0-or-later copyleft 义务。
- 接入成本: 高
- 替代方案: Nexus Repository, Verdaccio, GitLab Package Registry
- 评分: 4/5
- 备注: 适合作为多格式内容仓库平台；生产前要确认插件组合、对象存储、任务队列、权限、同步策略、备份恢复和升级路径。
