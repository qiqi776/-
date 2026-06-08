# 无障碍与可访问性测试组件

无障碍与可访问性测试组件覆盖 WCAG 规则扫描、ARIA 与语义检查、颜色对比度、键盘可用性、页面审计、组件级 a11y 检查和 CI 阻断。它解决“项目上线前如何自动发现明显无障碍问题”的问题；通用单元测试和端到端测试放在测试与质量分类，安全漏洞扫描放在安全扫描分类，组件 story 和视觉回归放在组件工作台分类。

## axe-core

- GitHub: https://github.com/dequelabs/axe-core
- 官网: https://www.deque.com/axe/core-documentation/
- 模块: 无障碍测试 / 规则引擎 / 浏览器注入
- 技术栈: JavaScript, Browser, Node.js, WCAG, ARIA
- 许可证: MPL-2.0
- 适合: 前端项目需要在单元测试、组件测试、E2E 测试、Storybook 或浏览器自动化里嵌入可访问性规则检查。
- 不适合: 希望只用一次 CLI 扫完整站点，或需要人工辅助技术测试、读屏器体验评估和完整合规审计的场景。
- 接入成本: 中
- 替代方案: Pa11y, Lighthouse, HTML_CodeSniffer
- 评分: 5/5
- 备注: 适合作为自动化 a11y 检查底层规则引擎；落地时要确认规则覆盖范围、严重级别阈值、忽略清单、组件状态样例和人工复核流程。

## Pa11y

- GitHub: https://github.com/pa11y/pa11y
- 官网: https://pa11y.org
- 模块: 无障碍测试 / CLI 扫描 / CI 报告
- 技术栈: JavaScript, Node.js, Puppeteer, axe-core, HTML_CodeSniffer
- 许可证: LGPL-3.0-only
- 适合: 需要用命令行或 Node.js 扫描页面 URL、输出 JSON/CSV/HTML 报告，并在 CI 中用阈值控制可访问性问题的项目。
- 不适合: 团队不能接受 LGPL 许可证复核，或页面必须经过复杂登录、多角色、多状态交互才能覆盖关键路径。
- 接入成本: 中
- 替代方案: axe-core, Lighthouse, pa11y-ci
- 评分: 4/5
- 备注: 适合站点级批量扫描和 CI 报告；生产前要确认 Node/Puppeteer 版本、认证脚本、等待策略、阈值、忽略规则和 LGPL-3.0-only 的合规处理。

## Lighthouse

- GitHub: https://github.com/GoogleChrome/lighthouse
- 官网: https://developer.chrome.com/docs/lighthouse/overview
- 模块: 无障碍测试 / 页面审计 / 性能与最佳实践
- 技术栈: JavaScript, Node.js, Chrome, CLI
- 许可证: Apache-2.0
- 适合: Web 应用需要同时审计性能、可访问性、SEO、最佳实践和 PWA 指标，并生成浏览器或 CI 可读的综合报告。
- 不适合: 需要细粒度组件状态扫描、复杂交互后的深度 a11y 覆盖，或只想要可访问性规则引擎而不需要综合审计。
- 接入成本: 低
- 替代方案: axe-core, Pa11y, WebPageTest
- 评分: 4/5
- 备注: 适合发布前健康检查和趋势监控；要避免只看总分，需把具体失败项、运行环境、网络条件和手工检查责任写清楚。
