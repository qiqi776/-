# 测试与质量组件

测试与质量组件覆盖单元测试、端到端测试、集成测试和自动化回归验证；接口压测、容量基线、并发负载和发布性能门禁放在性能与负载测试分类。

## Playwright

- GitHub: https://github.com/microsoft/playwright
- 官网: https://playwright.dev
- 模块: 测试 / 端到端测试
- 技术栈: TypeScript, JavaScript, Python, Java, .NET
- 许可证: Apache-2.0
- 适合: Web 应用需要跨浏览器端到端测试、截图回归、用户流程验证和 CI 自动化。
- 不适合: 只需要纯函数单元测试，或项目没有浏览器交互场景。
- 接入成本: 中
- 替代方案: Cypress, Selenium, WebdriverIO
- 评分: 4/5
- 备注: 适合验证登录、支付、后台流程等关键路径，但要控制测试数量和运行时间。

## Vitest

- GitHub: https://github.com/vitest-dev/vitest
- 官网: https://vitest.dev
- 模块: 测试 / 前端单元测试
- 技术栈: TypeScript, JavaScript, Vite
- 许可证: MIT
- 适合: Vite、Vue、React、Svelte 等前端项目需要快速单元测试、组件测试和覆盖率报告。
- 不适合: 非 JavaScript/TypeScript 项目，或项目构建链完全不基于 Vite 生态。
- 接入成本: 低
- 替代方案: Jest, Node.js test runner, uvu
- 评分: 4/5
- 备注: 对 Vite 项目接入成本很低，适合和 Testing Library 组合验证组件行为。

## pytest

- GitHub: https://github.com/pytest-dev/pytest
- 官网: https://pytest.org
- 模块: 测试 / Python 单元测试
- 技术栈: Python
- 许可证: MIT
- 适合: Python 后端、数据处理、脚本工具和自动化任务需要清晰的测试夹具与断言体验。
- 不适合: 非 Python 项目，或团队必须完全使用标准库 unittest。
- 接入成本: 低
- 替代方案: unittest, nose2, Robot Framework
- 评分: 4/5
- 备注: 插件生态成熟，适合从小型脚本到大型后端服务持续扩展测试覆盖。
