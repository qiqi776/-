# 论坛与社区平台组件

论坛与社区平台组件覆盖完整论坛、话题分类、用户资料、版主管理、社区治理、通知、积分/声望和长期讨论沉淀；轻量嵌入式评论放在评论与社区互动分类，客服会话和工单放在客户支持分类，产品反馈投票放在用户反馈与调研分类。

## Discourse

- GitHub: https://github.com/discourse/discourse
- 官网: https://www.discourse.org
- 模块: 论坛 / 社区平台 / 话题讨论
- 技术栈: Ruby on Rails, Ember.js, PostgreSQL, Redis
- 许可证: GPL-2.0
- 适合: 需要成熟社区论坛、分类话题、版主管理、通知、信任等级、搜索、插件和长期知识沉淀的产品或开源社区。
- 不适合: 只需要文章评论、轻量用户反馈、简单客服工单，或无法接受 GPL-2.0 合规要求的商业项目。
- 接入成本: 高
- 替代方案: NodeBB, Flarum, Forem
- 评分: 4/5
- 备注: 生态成熟但部署和治理复杂；上线前要确认 SSO、邮件送达、备份、插件、反垃圾、版主管理和 GPL 合规。

## NodeBB

- GitHub: https://github.com/NodeBB/NodeBB
- 官网: https://www.nodebb.org
- 模块: 论坛 / Node.js 社区 / 实时讨论
- 技术栈: JavaScript, Node.js, Redis, MongoDB
- 许可证: GPL-3.0
- 适合: JavaScript 技术栈团队需要实时论坛、插件主题、通知、用户组、分类话题和较现代的社区体验。
- 不适合: 不想维护 Node.js 实时服务、Redis/MongoDB 存储，或不能接受 GPL-3.0 许可证义务的项目。
- 接入成本: 中
- 替代方案: Discourse, Flarum, Vanilla Forums
- 评分: 4/5
- 备注: 技术栈对前端团队友好；部署前要确认存储选型、插件兼容、WebSocket、搜索、升级和 GPL 合规。

## Flarum

- GitHub: https://github.com/flarum/flarum
- 官网: https://flarum.org
- 模块: 论坛 / 轻量社区 / PHP
- 技术栈: PHP, Laravel Components, MySQL
- 许可证: MIT
- 适合: 需要轻量现代论坛、PHP 部署环境、扩展生态、基础社区讨论和较低许可证约束的团队。
- 不适合: 需要 Discourse 级别的大型社区治理、复杂审核工作流、企业级搜索或深度实时体验。
- 接入成本: 中
- 替代方案: Discourse, NodeBB, phpBB
- 评分: 4/5
- 备注: 许可证宽松、部署相对轻；生产前要确认扩展维护、主题兼容、权限模型、邮件通知和备份恢复。
