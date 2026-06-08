# 工程化工具组件

工程化工具组件覆盖 Monorepo 组织、包管理、构建缓存、任务编排和开发工作区管理。

## Turborepo

- GitHub: https://github.com/vercel/turborepo
- 官网: https://turborepo.dev
- 模块: 工程化 / Monorepo 构建编排
- 技术栈: Rust, TypeScript, JavaScript
- 许可证: MIT
- 适合: JavaScript/TypeScript 多包仓库需要任务管线、增量构建、本地/远程缓存和较轻量 Monorepo 管理。
- 不适合: 需要强项目生成器、跨语言插件生态、复杂依赖图规则或企业级治理。
- 接入成本: 中
- 替代方案: Nx, Lage, Rush
- 评分: 4/5
- 备注: 适合 Next.js、React、Node.js Monorepo；需要把缓存输入输出、环境变量和 CI 缓存策略配置清楚。

## Nx

- GitHub: https://github.com/nrwl/nx
- 官网: https://nx.dev
- 模块: 工程化 / Monorepo 平台
- 技术栈: TypeScript, Rust, JavaScript
- 许可证: MIT
- 适合: 多应用、多库项目需要依赖图、affected 构建、代码生成器、插件生态、CI 分布式执行和跨框架管理。
- 不适合: 小型单应用仓库，或团队只想要轻量任务缓存。
- 接入成本: 高
- 替代方案: Turborepo, Rush, Bazel
- 评分: 4/5
- 备注: 曾发生 2025-08 Nx npm 包供应链事件和 2026-05 Nx Console 扩展事件；使用时要固定版本、审计扩展、监控安全公告并建立凭据轮换流程。

## pnpm

- GitHub: https://github.com/pnpm/pnpm
- 官网: https://pnpm.io
- 模块: 工程化 / 包管理 / Workspace
- 技术栈: TypeScript, Rust, Node.js
- 许可证: MIT
- 适合: Node.js 项目需要更严格依赖声明、节省磁盘空间、可重复安装和 Monorepo workspace 管理。
- 不适合: 团队依赖 npm/Yarn 特定行为，或现有工具不能兼容 pnpm 的符号链接依赖结构。
- 接入成本: 中
- 替代方案: npm, Yarn, Bun
- 评分: 4/5
- 备注: 适合作为 Monorepo 的包管理底座；要统一 Node/pnpm 版本、提交 lockfile，并在 CI 使用 Corepack 或明确安装版本。
