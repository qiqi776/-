# 产品分析组件

产品分析组件覆盖用户行为分析、网站统计、事件采集和转化漏斗。

## Umami

- GitHub: https://github.com/umami-software/umami
- 官网: https://umami.is
- 模块: 产品分析 / 网站统计 / 隐私友好分析
- 技术栈: TypeScript, Next.js, Prisma, PostgreSQL, MySQL
- 许可证: MIT
- 适合: 团队需要自托管网站统计、页面浏览、事件、来源渠道、隐私友好分析和较低运维成本。
- 不适合: 需要复杂产品事件、漏斗留存、A/B 实验、用户行为回放或功能开关一体化的重型产品分析平台。
- 接入成本: 低
- 替代方案: Plausible Analytics, Matomo, OpenPanel
- 评分: 4/5
- 备注: 轻量、清晰且适合多数站点统计场景；生产前要确认数据库、反向代理、数据保留、Cookie 策略和隐私合规口径。

## Plausible Analytics

- GitHub: https://github.com/plausible/analytics
- 官网: https://plausible.io
- 模块: 产品分析 / 网站统计
- 技术栈: Elixir, ClickHouse
- 许可证: AGPL-3.0
- 适合: 隐私友好的网站统计、营销站、内容站和不想使用重型产品分析套件的项目。
- 不适合: 需要复杂产品事件、实验平台、用户级行为回放或不能接受 AGPL 义务的项目。
- 接入成本: 中
- 替代方案: Umami, Matomo, OpenPanel
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
- 替代方案: Plausible Analytics, Umami, OpenPanel
- 评分: 4/5
- 备注: 历史成熟度高，但新产品事件分析体验不一定是最轻快的选择。
