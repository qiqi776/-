# 用户反馈与调研组件

用户反馈与调研组件覆盖产品内反馈、问卷、NPS、用户研究、功能建议、投票和反馈路线图；通用字段状态和校验放在表单与校验分类，客服会话和工单放在客户支持分类，公开评论讨论放在评论与社区互动分类。

## Formbricks

- GitHub: https://github.com/formbricks/formbricks
- 官网: https://formbricks.com
- 模块: 用户反馈 / 问卷 / 产品内调研
- 技术栈: TypeScript, Next.js, React, PostgreSQL
- 许可证: AGPL-3.0 / MIT
- 适合: SaaS 产品需要产品内问卷、NPS、用户分群触发、反馈收集、调研分析和自托管客户体验数据。
- 不适合: 只需要静态表单收集，或无法接受主服务 AGPL 许可证义务的闭源商业系统。
- 接入成本: 中
- 替代方案: LimeSurvey, Fider, PostHog Surveys
- 评分: 4/5
- 备注: 主服务以 AGPL 为主，部分 SDK 和 API 包使用 MIT；接入前要核对目录级许可证、事件触发和隐私合规边界。

## Fider

- GitHub: https://github.com/getfider/fider
- 官网: https://fider.io
- 模块: 用户反馈 / 功能建议 / 投票
- 技术栈: Go, TypeScript, React, PostgreSQL
- 许可证: AGPL-3.0
- 适合: 产品需要公开收集功能建议、用户投票、状态更新、路线图沟通和需求优先级排序。
- 不适合: 需要复杂问卷逻辑、匿名研究样本管理、客服工单流转，或不能接受 AGPL 网络服务义务。
- 接入成本: 中
- 替代方案: Astuto, Canny, GitHub Discussions
- 评分: 4/5
- 备注: 适合把用户需求从客服和评论里分离出来；上线前要确认登录方式、审核、通知、去重和公开可见范围。

## LimeSurvey

- GitHub: https://github.com/LimeSurvey/LimeSurvey
- 官网: https://www.limesurvey.org
- 模块: 问卷调研 / 用户研究 / 数据收集
- 技术栈: PHP, Yii, MySQL, PostgreSQL
- 许可证: GPL-2.0-or-later
- 适合: 需要成熟问卷逻辑、题型、配额、匿名答卷、多语言、调研发布和结果导出的研究或运营团队。
- 不适合: 只需要轻量产品内弹窗反馈、实时功能投票，或团队不想维护传统 PHP 问卷系统。
- 接入成本: 中
- 替代方案: Formbricks, SurveyJS, Typeform
- 评分: 4/5
- 备注: 问卷能力成熟但产品形态偏独立调研系统；集成前要确认主题定制、身份打通、数据导出和 GPL 合规。
