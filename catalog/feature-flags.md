# 功能开关组件

功能开关组件覆盖灰度发布、实验平台、远程配置和渐进式交付。

## Unleash

- GitHub: https://github.com/Unleash/unleash
- 官网: https://www.getunleash.io
- 模块: 功能开关 / 渐进式交付
- 技术栈: TypeScript, Node.js
- 许可证: Apache-2.0（v7 及之前）/ AGPL-3.0（v8 起）
- 适合: 需要自托管 Feature Flags、渐进式发布、环境隔离和多 SDK 接入的团队。
- 不适合: 团队不能接受 AGPL 义务，或只需要非常简单的环境变量开关。
- 接入成本: 中
- 替代方案: GrowthBook, Flagsmith, PostHog Feature Flags
- 评分: 4/5
- 备注: 许可证随版本变化明显，选型时必须锁定版本并复核许可证。

## GrowthBook

- GitHub: https://github.com/growthbook/growthbook
- 官网: https://www.growthbook.io
- 模块: 功能开关 / A/B 测试 / 实验
- 技术栈: TypeScript, React, Node.js
- 许可证: MIT
- 适合: 需要 Feature Flags、A/B 测试、实验分析和数据仓库集成的增长团队。
- 不适合: 只需要后端灰度开关，或项目没有足够事件数据支撑实验分析。
- 接入成本: 中
- 替代方案: Unleash, Flagsmith, PostHog
- 评分: 4/5
- 备注: 和产品分析、事件埋点一起设计时更有价值。

## Flagsmith

- GitHub: https://github.com/Flagsmith/flagsmith
- 官网: https://www.flagsmith.com
- 模块: 功能开关 / 远程配置
- 技术栈: Python, Django, React
- 许可证: BSD-3-Clause
- 适合: 自托管功能开关、远程配置、多环境配置和需要较完整管理界面的项目。
- 不适合: 团队不想维护额外服务，或只需要代码内静态开关。
- 接入成本: 中
- 替代方案: Unleash, GrowthBook, PostHog Feature Flags
- 评分: 4/5
- 备注: 适合作为宽松许可证下的自托管功能开关候选。
