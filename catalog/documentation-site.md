# 文档站与开发者门户组件

文档站与开发者门户组件覆盖产品文档、开发者手册、项目官网、Markdown/MDX 内容、版本化文档、站内搜索、导航、主题和静态站点生成。它解决“用户和开发者如何阅读、搜索和维护项目文档”的问题；OpenAPI 接口渲染放在 API 文档分类，内容编辑后台放在内容管理分类，团队内部知识库放在文档协作分类。

## Docusaurus

- GitHub: https://github.com/facebook/docusaurus
- 官网: https://docusaurus.io
- 模块: 文档站 / React 静态站点 / MDX
- 技术栈: TypeScript, React, MDX, Node.js
- 许可证: MIT
- 适合: 开源项目、开发者平台和产品团队需要文档、博客、版本化、多语言、本地化和高度可定制的 React/MDX 文档站。
- 不适合: 团队不希望维护 Node.js 前端构建链，或文档主要由非技术编辑在 CMS 中管理。
- 接入成本: 中
- 替代方案: VitePress, Material for MkDocs, Nextra
- 评分: 4/5
- 备注: 适合把文档和代码一起版本化；落地时要提前设计信息架构、版本策略、侧边栏、搜索、国际化和部署目标。

## VitePress

- GitHub: https://github.com/vuejs/vitepress
- 官网: https://vitepress.dev
- 模块: 文档站 / Vue 静态站点 / Vite
- 技术栈: TypeScript, Vue, Vite, Markdown, Node.js
- 许可证: MIT
- 适合: Vue 或 Vite 生态项目需要轻量快速的 Markdown 文档站，要求开发体验简单、构建速度快、可嵌入 Vue 组件。
- 不适合: 需要复杂插件生态、内置博客工作流、强版本化体系或 React/MDX 组件文档体验的团队。
- 接入成本: 低
- 替代方案: Docusaurus, Material for MkDocs, VuePress
- 评分: 4/5
- 备注: 很适合框架、组件库和工具项目文档；生产前要确认搜索方案、内容分层、部署路径和主题自定义边界。

## Material for MkDocs

- GitHub: https://github.com/squidfunk/mkdocs-material
- 官网: https://squidfunk.github.io/mkdocs-material
- 模块: 文档站 / Python 静态站点 / MkDocs 主题
- 技术栈: Python, MkDocs, Markdown, Pygments
- 许可证: MIT
- 适合: Python、数据、后端和基础设施项目需要专业 Markdown 技术文档站，偏好配置式导航、搜索、代码高亮、插件和 Docker/Python 部署。
- 不适合: 需要深度前端交互、React/Vue 组件嵌入或完全自定义应用式前端体验的文档站。
- 接入成本: 低
- 替代方案: Docusaurus, VitePress, MkDocs
- 评分: 4/5
- 备注: 写作门槛低，适合快速沉淀项目手册；上线前要验证主题配置、搜索索引、插件许可证、构建镜像和文档发布流程。
