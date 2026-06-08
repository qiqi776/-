# 文档协作与知识库组件

文档协作与知识库组件覆盖团队 Wiki、协作文档、空间权限、页面层级、版本历史、全文搜索、评论协作和知识沉淀；编辑器内核放在富文本与编辑器分类，PDF/Office 解析放在文档处理分类，面向营销内容发布的后台放在内容管理分类。对 BSL、Elastic License 等源代码可见但非标准开源的项目，需要在选型时单独审查商业化和托管限制。

## Docmost

- GitHub: https://github.com/docmost/docmost
- 官网: https://docmost.com
- 模块: 文档协作 / Wiki / Notion 替代
- 技术栈: TypeScript, React, NestJS, PostgreSQL, Redis
- 许可证: AGPL-3.0
- 适合: 需要自托管团队知识库、空间管理、嵌套页面、实时协作编辑、权限控制和 Notion/Confluence 风格文档体验的团队。
- 不适合: 无法接受 AGPL 网络服务义务，或只需要嵌入一个轻量编辑器而不想维护完整文档系统的项目。
- 接入成本: 中
- 替代方案: Wiki.js, XWiki, Outline
- 评分: 4/5
- 备注: 产品形态贴近现代协作文档；上线前要确认 PostgreSQL、Redis、文件存储、邀请流程、SSO、备份和 AGPL 合规边界。

## Wiki.js

- GitHub: https://github.com/requarks/wiki
- 官网: https://js.wiki
- 模块: 文档协作 / Wiki / Markdown 知识库
- 技术栈: Node.js, Vue, Markdown, PostgreSQL, MySQL, MariaDB, SQLite
- 许可证: AGPL-3.0
- 适合: 需要现代 Wiki、Markdown 内容、权限、认证集成、多数据源存储和相对完整管理后台的知识库项目。
- 不适合: 无法接受 AGPL，或希望文档系统完全内嵌到现有前端而不是部署独立服务的场景。
- 接入成本: 中
- 替代方案: Docmost, XWiki, HedgeDoc
- 评分: 4/5
- 备注: 生态和部署资料较完整；生产前要验证数据库类型、搜索、备份、认证方式、Git/存储同步和版本升级路径。

## XWiki

- GitHub: https://github.com/xwiki/xwiki-platform
- 官网: https://www.xwiki.org
- 模块: 文档协作 / 企业 Wiki / 应用平台
- 技术栈: Java, Maven, JVM, JavaScript, TypeScript
- 许可证: LGPL-2.1
- 适合: 企业内部需要成熟 Wiki、权限、扩展、宏、结构化页面和可在 Wiki 之上构建业务应用的平台型场景。
- 不适合: 小团队只想快速上线轻量知识库，或团队没有 Java/JVM 运维和插件治理经验。
- 接入成本: 高
- 替代方案: Wiki.js, Docmost, Confluence
- 评分: 4/5
- 备注: 能力成熟但平台感较重；接入前要评估 JVM 部署、扩展兼容、权限模型、迁移脚本、备份恢复和长期维护成本。
