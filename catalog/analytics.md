# 产品分析组件

产品分析组件覆盖用户行为分析、网站统计、事件采集和转化漏斗。

## PostHog

- GitHub: https://github.com/PostHog/posthog
- 官网: https://posthog.com
- 模块: 产品分析 / 事件 / 实验
- 技术栈: Python, TypeScript, ClickHouse
- 许可证: MIT（核心）/ 商业许可证（enterprise）
- 适合: SaaS 产品分析、事件采集、漏斗、留存、Feature Flags、A/B 测试和用户行为回放。
- 不适合: 只需要最轻量 PV 统计，或团队不想维护 ClickHouse 等分析基础设施的项目。
- 接入成本: 中
- 替代方案: Plausible Analytics, Matomo, Umami
- 评分: 4/5
- 备注: 功能覆盖面强，open core 模式下要区分社区功能和企业功能。

## Plausible Analytics

- GitHub: https://github.com/plausible/analytics
- 官网: https://plausible.io
- 模块: 产品分析 / 网站统计
- 技术栈: Elixir, ClickHouse
- 许可证: AGPL-3.0
- 适合: 隐私友好的网站统计、营销站、内容站和不想使用重型产品分析套件的项目。
- 不适合: 需要复杂产品事件、实验平台、用户级行为回放或不能接受 AGPL 义务的项目。
- 接入成本: 中
- 替代方案: PostHog, Matomo, Umami
- 评分: 4/5
- 备注: 自托管时要评估 AGPL 义务和 ClickHouse 运维成本。

## Matomo

- GitHub: https://github.com/matomo-org/matomo
- 官网: https://matomo.org
- 模块: 产品分析 / Web Analytics
- 技术栈: PHP, MySQL
- 许可证: GPL-3.0
- 适合: 需要成熟 Web Analytics、报表、合规可控数据归属和较传统部署方式的组织。
- 不适合: 主要做现代事件驱动产品分析，或团队不能接受 GPL 许可证约束的项目。
- 接入成本: 中
- 替代方案: Plausible Analytics, PostHog, Umami
- 评分: 4/5
- 备注: 历史成熟度高，但新产品事件分析体验不一定是最轻快的选择。
