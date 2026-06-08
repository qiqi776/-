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
- 替代方案: Nexus Repository, GitLab Package Registry, npm Enterprise
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
- 替代方案: Verdaccio, Apache Archiva, JFrog Artifactory
- 评分: 4/5
- 备注: 开源核心和商业能力需要提前划边界；生产前要验证制品格式、blob storage、备份恢复、清理策略、LDAP/SSO、漏洞策略和迁移路径。

## Apache Archiva

- GitHub: https://github.com/apache/archiva
- 官网: https://archiva.apache.org
- 模块: 包与制品仓库 / Maven 仓库 / 依赖代理
- 技术栈: Java, Maven, Jetty, Repository Manager
- 许可证: Apache-2.0
- 适合: Java 或 Maven 团队需要自托管 Maven 制品仓库、内部 release/snapshot 发布和上游依赖代理。
- 不适合: 需要 npm、NuGet、PyPI、OCI 多格式统一治理，或需要更活跃生态、现代企业权限和安全治理能力的项目。
- 接入成本: 中
- 替代方案: Nexus Repository, JFrog Artifactory, GitLab Package Registry
- 评分: 3/5
- 备注: 更适合 Maven 中心化且需求简单的团队；落地前要确认项目维护活跃度、权限模型、存储备份、清理策略和未来迁移方案。
