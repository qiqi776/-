# 组件工作台与设计系统文档组件

组件工作台与设计系统文档组件覆盖 UI 组件的独立预览、状态样例、交互调试、视觉回归、设计系统文档和组件用法沉淀。它解决“前端组件如何在真实页面外被开发、评审、测试和复用”的问题；UI 组件库本身放在前端分类，面向用户和开发者的产品文档站放在文档站分类。

## Storybook

- GitHub: https://github.com/storybookjs/storybook
- 官网: https://storybook.js.org
- 模块: 组件工作台 / 设计系统文档 / UI 测试
- 技术栈: TypeScript, JavaScript, React, Vue, Angular, Web Components
- 许可证: MIT
- 适合: 团队需要为多框架或复杂前端项目沉淀组件 story、交互样例、设计系统文档、视觉回归和组件级测试。
- 不适合: 只做少量页面、没有组件复用计划，或团队不愿维护额外构建配置和插件体系的项目。
- 接入成本: 中
- 替代方案: Histoire, Ladle, Styleguidist
- 评分: 5/5
- 备注: 适合设计系统和大型前端团队；落地时要约定 story 命名、Mock 数据、交互测试、可访问性检查、截图回归和 CI 发布流程。

## Histoire

- GitHub: https://github.com/histoire-dev/histoire
- 官网: https://histoire.dev
- 模块: 组件工作台 / Vite 组件演示 / 文档
- 技术栈: TypeScript, Vite, Vue, Svelte, Markdown
- 许可证: MIT
- 适合: Vue、Svelte 或 Vite 生态项目需要轻量组件 playground、状态控制、源码展示和 Markdown 说明。
- 不适合: React 生态为主、需要 Storybook 成熟插件生态，或项目要和现有视觉回归平台深度集成。
- 接入成本: 低
- 替代方案: Storybook, Ladle, VitePress
- 评分: 4/5
- 备注: 适合 Vite 项目快速搭建组件演示；生产前要确认框架支持范围、构建输出、主题定制、路由组织和 CI 截图方案。

## Ladle

- GitHub: https://github.com/tajo/ladle
- 官网: https://ladle.dev
- 模块: 组件工作台 / React Story / 快速预览
- 技术栈: TypeScript, React, Vite, SWC
- 许可证: MIT
- 适合: React 项目希望用较轻量的 story 环境快速预览组件、共享状态样例，并减少启动和构建成本。
- 不适合: 需要跨框架支持、复杂设计系统插件、成熟文档生态或企业级组件治理工作流的团队。
- 接入成本: 低
- 替代方案: Storybook, Histoire, Styleguidist
- 评分: 4/5
- 备注: 适合中小型 React 组件库和应用内部组件沉淀；选型前要验证与现有 Vite 配置、测试工具、样式方案和静态发布流程的兼容性。
