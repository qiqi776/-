# CI/CD 组件

CI/CD 组件覆盖持续集成、持续交付、构建流水线、任务执行、发布门禁和可复用自动化流程。

## Jenkins

- GitHub: https://github.com/jenkinsci/jenkins
- 官网: https://www.jenkins.io
- 模块: CI/CD / 自动化服务器
- 技术栈: Java, Groovy, Plugins
- 许可证: MIT
- 适合: 团队需要高度可扩展的自托管自动化服务器、丰富插件生态和复杂流水线编排。
- 不适合: 小团队只需要简单 GitHub 仓库 CI，或不想维护插件、安全补丁和控制器/执行器架构。
- 接入成本: 高
- 替代方案: GitHub Actions, GitLab CI, Woodpecker CI
- 评分: 4/5
- 备注: 成熟但运维成本高；要治理插件版本、凭据权限、执行器隔离和流水线脚本评审。

## Woodpecker CI

- GitHub: https://github.com/woodpecker-ci/woodpecker
- 官网: https://woodpecker-ci.org
- 模块: CI/CD / 自托管流水线
- 技术栈: Go, Docker, YAML
- 许可证: Apache-2.0
- 适合: 需要轻量自托管 CI、容器化步骤、Git 平台集成和较简单流水线配置的团队。
- 不适合: 需要极复杂企业插件生态、可视化审批流或深度云厂商托管能力。
- 接入成本: 中
- 替代方案: Jenkins, Drone, GitLab CI
- 评分: 4/5
- 备注: 适合中小团队自托管；要规划 runner 隔离、镜像缓存、密钥注入和失败重试策略。

## Dagger

- GitHub: https://github.com/dagger/dagger
- 官网: https://dagger.io
- 模块: CI/CD / 可移植流水线引擎
- 技术栈: Go, SDK, Containers
- 许可证: Apache-2.0
- 适合: 希望把构建、测试、发布流程写成可复用代码，并在本地和不同 CI 平台中一致执行的团队。
- 不适合: 只想使用平台内置 YAML，或需要开箱即用的完整 CI 托管界面和排队系统。
- 接入成本: 中
- 替代方案: Earthly, Nix, GitHub Actions reusable workflows
- 评分: 4/5
- 备注: 适合复杂流水线复用和本地复现；要控制 SDK 抽象层级、容器缓存和密钥传递边界。
