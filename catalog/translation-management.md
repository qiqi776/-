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
- 替代方案: Tolgee, Pontoon, Crowdin
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
- 替代方案: Weblate, Pontoon, Lokalise
- 评分: 4/5
- 备注: 开源核心是 Apache-2.0，但仓库包含企业许可目录；正式选型前要确认开源版功能、SDK 覆盖语言和生产环境内嵌翻译权限。

## Pontoon

- GitHub: https://github.com/mozilla/pontoon
- 官网: https://pontoon.mozilla.org
- 模块: 翻译管理 / 本地化平台 / 社区翻译
- 技术栈: Python, Django, JavaScript, TypeScript, PostgreSQL
- 许可证: BSD-3-Clause
- 适合: 开源项目或社区驱动产品需要成熟本地化平台、版本控制集成、译者协作、审核流程和 Mozilla 生态实践。
- 不适合: 主要需要应用内上下文翻译 SDK、商业翻译供应商工作流，或希望低运维成本快速接入 SaaS 翻译平台。
- 接入成本: 高
- 替代方案: Weblate, Tolgee, Crowdin
- 评分: 4/5
- 备注: Mozilla 长期使用的成熟本地化平台；生产前要确认部署方式、权限模型、仓库同步、语言团队治理和升级路径。
