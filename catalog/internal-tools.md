# 内部工具与低代码后台组件

内部工具与低代码后台组件覆盖运营控制台、CRUD 管理面板、数据源连接、审批流程、权限控制和内部应用快速搭建平台。

## Appsmith

- GitHub: https://github.com/appsmithorg/appsmith
- 官网: https://www.appsmith.com
- 模块: 内部工具 / 低代码应用构建器
- 技术栈: TypeScript, Java, React, Docker
- 许可证: Apache-2.0
- 适合: 团队需要快速搭建内部 CRUD、运营工具、数据看板、审批页面，并连接数据库、REST API、GraphQL 或第三方 SaaS。
- 不适合: 面向公众的高品牌体验，或需要把内部工具深度嵌入主应用代码库的项目。
- 接入成本: 中
- 替代方案: ToolJet, Budibase, Retool
- 评分: 4/5
- 备注: 适合把内部工具从一次性脚本提升为可维护应用；上线前要核对数据源权限、环境隔离、审计日志和 SSO 配置。

## ToolJet

- GitHub: https://github.com/ToolJet/ToolJet
- 官网: https://www.tooljet.com
- 模块: 内部工具 / 低代码平台 / 工作流
- 技术栈: TypeScript, NestJS, React, Docker
- 许可证: AGPL-3.0
- 适合: 需要自托管低代码内部应用、可视化页面搭建、数据源集成、表单流程和轻量自动化的团队。
- 不适合: 团队不能接受 AGPL 网络服务义务，或内部工具必须完全由代码和普通 CI/CD 管理。
- 接入成本: 中
- 替代方案: Appsmith, Budibase, NocoBase
- 评分: 4/5
- 备注: AGPL-3.0 对网络服务分发有合规要求；生产前要确认企业功能边界、插件能力、权限模型和数据连接密钥管理。

## Budibase

- GitHub: https://github.com/Budibase/budibase
- 官网: https://budibase.com
- 模块: 内部工具 / 低代码后台 / 表单流程
- 技术栈: TypeScript, Svelte, Node.js, Docker
- 许可证: GPL-3.0（整体）
- 适合: 需要快速构建内部表单、审批流、数据库驱动后台、简单自动化和自托管低代码平台的团队。
- 不适合: 团队必须使用宽松许可证，或希望每个内部工具都以常规应用源码方式长期演进。
- 接入成本: 中
- 替代方案: Appsmith, ToolJet, NocoBase
- 评分: 4/5
- 备注: 仓库说明整体可按 GPLv3 看待，且 package 可能有各自许可证；上线前要复核目标版本许可证、用户权限和数据源访问范围。
