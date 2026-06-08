# 翻译管理与本地化平台组件

翻译管理与本地化平台组件覆盖译文协作、审核流程、术语表、翻译记忆、资源导入导出、Git 或仓库同步和上下文截图。它解决产品文案从开发资源到译者协作、质量检查和发布回流的流程问题，不替代应用运行时的国际化 SDK。

## Weblate

- GitHub: https://github.com/WeblateOrg/weblate
- 官网: https://weblate.org
- 模块: 翻译管理 / 连续本地化 / Git 集成
- 技术栈: Python, Django, PostgreSQL, Redis, Celery, Git
- 许可证: GPL-3.0-or-later
- 适合: 需要自托管连续本地化平台、Git 仓库同步、多文件格式支持、译者审核、术语表、翻译记忆和社区翻译流程的项目。
- 不适合: 只需要简单文案文件维护，或不能承担完整 Django 平台部署、权限、邮件、任务队列和 GPL 合规确认的项目。
- 接入成本: 高
- 替代方案: Tolgee, Traduora, Crowdin
- 评分: 4/5
- 备注: 适合把仓库中的翻译资源作为核心资产管理；上线前要设计语言分支、组件拆分、同步冲突处理和译者权限模型。

## Tolgee

- GitHub: https://github.com/tolgee/tolgee-platform
- 官网: https://tolgee.io
- 模块: 翻译管理 / 应用内上下文翻译 / SDK 同步
- 技术栈: Kotlin, Spring Boot, Java, React, TypeScript, PostgreSQL
- 许可证: Apache-2.0 / Tolgee Enterprise License
- 适合: 产品团队希望在应用内直接定位文案、截图上下文、用 SDK 与平台同步翻译，并结合机器翻译、翻译记忆和译者工作台加速本地化。
- 不适合: 希望所有翻译流程完全以 Git 仓库为中心，或无法接受仓库中开源版与企业版目录并存带来的功能边界确认成本。
- 接入成本: 中
- 替代方案: Weblate, Traduora, Lokalise
- 评分: 4/5
- 备注: 开源核心是 Apache-2.0，但仓库包含企业许可目录；正式选型前要确认开源版功能、SDK 覆盖语言和生产环境内嵌翻译权限。

## Traduora

- GitHub: https://github.com/ever-co/ever-traduora
- 官网: https://traduora.co
- 模块: 翻译管理 / REST API / 导入导出
- 技术栈: TypeScript, NestJS, Angular, TypeORM, PostgreSQL, MySQL
- 许可证: AGPL-3.0-only
- 适合: 需要自托管翻译管理后台、REST API、团队协作，以及 JSON、CSV、YAML、XLIFF、Gettext、Android Resources 等格式导入导出的项目。
- 不适合: 不能接受 AGPL 网络服务合规要求，或需要成熟 Git-first 社区翻译平台、深度应用内上下文翻译 SDK 和复杂审核治理的项目。
- 接入成本: 中
- 替代方案: Weblate, Tolgee, Crowdin
- 评分: 3/5
- 备注: 当前 Ever 版本仍在维护，但许可证和平台方向需要重点复核；建议先用真实资源文件验证导入导出、权限、数据库和部署流程。
