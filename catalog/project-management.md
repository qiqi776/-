# 项目管理与任务协作组件

项目管理与任务协作组件覆盖项目空间、Issue、看板、路线图、Sprint、任务分配、里程碑和团队计划；后台任务执行放在后台任务分类，业务流程自动化放在工作流分类，低延迟多人状态同步放在实时通信分类。

## Plane

- GitHub: https://github.com/makeplane/plane
- 官网: https://plane.so
- 模块: 项目管理 / Issue / Roadmap
- 技术栈: Python, TypeScript, PostgreSQL, Redis
- 许可证: AGPL-3.0
- 适合: 产品和工程团队需要自托管 Issue、Cycles、Modules、路线图、工作区和较现代的 Linear/Jira 替代方案。
- 不适合: 不能接受 AGPL-3.0 网络服务义务，或只需要极轻量个人任务清单的项目。
- 接入成本: 中
- 替代方案: OpenProject, Redmine, Linear
- 评分: 4/5
- 备注: 适合产品研发协作场景；生产前要确认 AGPL 合规、权限模型、导入导出、备份和通知集成。

## OpenProject

- GitHub: https://github.com/opf/openproject
- 官网: https://www.openproject.org
- 模块: 项目管理 / 工单 / 计划
- 技术栈: Ruby on Rails, Angular, PostgreSQL
- 许可证: GPL-3.0
- 适合: 需要成熟项目计划、工作包、甘特图、时间线、看板、文档和组织级项目管理的团队。
- 不适合: 只需要轻量敏捷看板，或项目许可证策略不能接受 GPL-3.0 copyleft 义务。
- 接入成本: 高
- 替代方案: Plane, Redmine, Taiga
- 评分: 4/5
- 备注: 功能覆盖完整但部署和配置较重；要评估权限、邮件通知、插件、备份、升级和企业功能边界。

## Redmine

- GitHub: https://github.com/redmine/redmine
- 官网: https://www.redmine.org
- 模块: 项目管理 / Issue / Wiki / 路线图
- 技术栈: Ruby on Rails, SQL
- 许可证: GPL-2.0-or-later
- 适合: 团队需要成熟自托管项目管理、Issue、Wiki、路线图、里程碑、时间跟踪和多项目权限。
- 不适合: 追求现代极简 UI、实时协作体验，或项目许可证策略不能接受 GPL-2.0-or-later copyleft 义务。
- 接入成本: 中
- 替代方案: Plane, OpenProject, Taiga
- 评分: 4/5
- 备注: 项目管理领域成熟度高；落地前要确认插件、权限、邮件、附件存储、主题和升级路径。
