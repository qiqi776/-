# 项目脚手架与模板生成组件

项目脚手架与模板生成组件覆盖新项目初始化、项目模板渲染、可重复代码片段生成、文件注入、团队最佳实践固化和模板升级；Monorepo、构建缓存和任务编排放在工程化分类，API 客户端代码生成放在 API 客户端与 SDK 生成分类，真实业务项目模板后续可放在 components/ 目录。

## Plop

- GitHub: https://github.com/plopjs/plop
- 官网: https://plopjs.com
- 模块: 项目脚手架 / 微生成器 / 文件模板
- 技术栈: JavaScript, Node.js, Handlebars, CLI
- 许可证: MIT
- 适合: 团队需要在现有项目里统一生成组件、页面、控制器、测试文件和重复目录结构。
- 不适合: 需要从远程模板创建完整项目，或需要跨版本自动升级已生成项目的场景。
- 接入成本: 低
- 替代方案: Hygen, Copier, Yeoman
- 评分: 4/5
- 备注: 适合把团队约定变成最容易执行的命令；上线前要维护模板位置、命名规则、覆盖策略和生成后格式化。

## Copier

- GitHub: https://github.com/copier-org/copier
- 官网: https://copier.readthedocs.io
- 模块: 项目模板 / 模板渲染 / 模板升级
- 技术栈: Python, Jinja, Git, CLI
- 许可证: MIT
- 适合: 需要从本地或 Git 模板创建项目，并在模板演进后把更新同步回已生成项目的团队。
- 不适合: 只需要在 JavaScript 项目中生成少量组件文件，或团队不希望引入 Python 工具链。
- 接入成本: 中
- 替代方案: Plop, Cookiecutter, Yeoman
- 评分: 4/5
- 备注: 模板升级能力适合长期维护 starter；生产前要确认答案文件、冲突处理、模板版本、私有模板权限和生成后检查。

## Yeoman

- GitHub: https://github.com/yeoman/yo
- 官网: https://yeoman.io
- 模块: 项目脚手架 / Generator 生态 / CLI
- 技术栈: JavaScript, Node.js, CLI
- 许可证: BSD-2-Clause
- 适合: 需要利用成熟 generator 生态快速创建 Web、前端、工具链或框架项目，并支持自定义 generator 的团队。
- 不适合: 项目只需要少量本地文件模板，或团队不想依赖全局生成器和外部 generator 质量。
- 接入成本: 中
- 替代方案: Plop, Hygen, Copier
- 评分: 3/5
- 备注: 生态历史长但不同 generator 质量差异大；使用前要核验 generator 维护状态、依赖版本、生成代码安全和升级路径。
