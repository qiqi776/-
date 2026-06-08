# 代码托管与版本协作组件

代码托管与版本协作组件覆盖 Git 仓库托管、仓库权限、分支保护、Pull Request 或 Merge Request、代码评审、Issue、Wiki、Webhook 和团队协作入口。它解决源码如何被保存、审查、合并和迁移的问题；构建流水线放在 CI/CD 分类，长期任务管理放在项目管理分类，容器镜像和制品仓库放在容器与镜像构建分类。

## GitLab

- GitHub: https://github.com/gitlabhq/gitlabhq
- 官网: https://about.gitlab.com
- 模块: 代码托管 / DevSecOps 平台 / Merge Request
- 技术栈: Ruby, Ruby on Rails, PostgreSQL, Redis, Sidekiq, Vue, Git
- 许可证: MIT Expat / GitLab Enterprise License
- 适合: 企业或中大型团队需要自托管 Git 仓库、Merge Request、代码评审、Issue、Wiki、CI/CD、权限治理和更完整 DevSecOps 平台能力。
- 不适合: 只需要一个轻量私有 Git 服务，或团队无法承担 GitLab 对服务器资源、升级、备份、邮件、Runner 和权限治理的运维成本。
- 接入成本: 高
- 替代方案: Gitea, GitBucket, GitHub Enterprise
- 评分: 4/5
- 备注: GitLab 功能覆盖面很广，但 CE、EE 和镜像仓库边界要分清；上线前要规划备份恢复、Runner 隔离、许可证边界、升级窗口和仓库迁移路径。

## Gitea

- GitHub: https://github.com/go-gitea/gitea
- 官网: https://about.gitea.com
- 模块: 代码托管 / 轻量 Git 服务 / Pull Request
- 技术栈: Go, SQLite, MySQL, PostgreSQL, Redis, Git, SSH
- 许可证: MIT
- 适合: 小团队、个人项目、内网环境或轻量自托管场景需要快速搭建 Git 仓库、Issue、Pull Request、Wiki、包管理和基础 Actions Runner。
- 不适合: 需要 GitLab 级企业治理、复杂合规审批、深度 DevSecOps 套件或大量内置企业功能的组织。
- 接入成本: 低
- 替代方案: GitLab, GitBucket, Gogs
- 评分: 4/5
- 备注: 部署和维护成本低，适合先把代码托管私有化；生产前要确认数据库选择、备份、SSH/HTTP 入口、邮件通知、Webhook、Runner 权限和插件生态。

## GitBucket

- GitHub: https://github.com/gitbucket/gitbucket
- 官网: https://gitbucket.github.io
- 模块: 代码托管 / GitHub 风格协作 / 插件扩展
- 技术栈: Scala, JVM, Scalatra, Jetty, H2, MariaDB, Git
- 许可证: Apache-2.0
- 适合: 团队希望用单个 JVM Web 应用获得 GitHub 风格界面、私有仓库、Issue、Pull Request、Wiki、Git LFS 和插件扩展能力。
- 不适合: 非 JVM 运维环境，或需要大规模企业治理、内置 CI/CD、复杂权限模型和活跃商业支持的项目。
- 接入成本: 中
- 替代方案: Gitea, GitLab, Gogs
- 评分: 3/5
- 备注: 安装形态简单但生态规模小于 GitLab 和 Gitea；上线前要验证数据库迁移、插件维护、备份恢复、SSH 配置和 GitHub API 兼容范围。
