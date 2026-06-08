# 评论与社区互动组件

评论与社区互动组件覆盖网站评论、嵌入式讨论、用户登录、匿名评论、审核、反垃圾、通知和迁移；客服会话和工单放在客户支持分类，多人光标和协同编辑评论放在实时通信分类，内容后台放在内容管理分类。

## Remark42

- GitHub: https://github.com/umputun/remark42
- 官网: https://remark42.com
- 模块: 评论 / 自托管 / 审核
- 技术栈: Go, JavaScript, Docker
- 许可证: MIT
- 适合: 内容站、文档站或产品需要自托管评论系统，支持匿名评论、社交登录、邮件通知、投票、审核、导入导出和多站点部署。
- 不适合: 需要完整论坛、社区积分体系、私信、复杂版主管理或商业托管评论平台的项目。
- 接入成本: 中
- 替代方案: Isso, giscus, Commento
- 评分: 4/5
- 备注: 适合把评论数据掌握在自己手里；上线前要确认登录方式、反垃圾策略、备份、嵌入脚本 CSP、邮件通知和迁移路径。

## Isso

- GitHub: https://github.com/isso-comments/isso
- 官网: https://isso-comments.de
- 模块: 评论 / 轻量自托管 / SQLite
- 技术栈: Python, JavaScript, SQLite
- 许可证: MIT
- 适合: 静态博客、文档站和小型内容站需要轻量自托管评论，偏好匿名或邮箱评论，不想依赖第三方 SaaS。
- 不适合: 需要多租户、大规模社区治理、复杂社交登录、实时通知或完整后台运营能力的产品。
- 接入成本: 低
- 替代方案: Remark42, giscus, Disqus
- 评分: 3/5
- 备注: 部署简单但能力边界较窄；生产前要确认垃圾评论过滤、邮件配置、SQLite 备份、迁移和前端主题适配。

## giscus

- GitHub: https://github.com/giscus/giscus
- 官网: https://giscus.app
- 模块: 评论 / GitHub Discussions / 嵌入式组件
- 技术栈: TypeScript, React, GitHub Discussions
- 许可证: MIT
- 适合: 开源项目、技术博客、文档站想用 GitHub Discussions 承载评论，并复用 GitHub 登录、通知、反垃圾和社区身份。
- 不适合: 面向非技术用户、不能要求 GitHub 账号、评论数据不能公开在 GitHub，或需要完全自托管评论数据库的项目。
- 接入成本: 低
- 替代方案: Remark42, Isso, Utterances
- 评分: 4/5
- 备注: 适合开源项目文档和开发者社区；要确认 Discussions 分类、仓库公开性、隐私提示、主题样式和 GitHub API 限制。
