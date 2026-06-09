# 客户支持与工单组件

客户支持与工单组件覆盖在线客服、共享收件箱、工单流转、帮助台、客服协作和知识库入口；多渠道通知仍放在通知触达分类，内部运营后台仍放在内部工具分类。

## Chatwoot

- GitHub: https://github.com/chatwoot/chatwoot
- 官网: https://www.chatwoot.com
- 模块: 客户支持 / 在线客服 / 共享收件箱
- 技术栈: Ruby on Rails, Vue, PostgreSQL, Redis
- 许可证: MIT Expat
- 适合: 需要网站聊天组件、共享收件箱、多渠道会话、客服分配、自动化规则和客户沟通历史的 SaaS 或电商项目。
- 不适合: 只需要简单邮件工单，或不希望维护 Rails、Redis、PostgreSQL 和实时通信部署的团队。
- 接入成本: 中
- 替代方案: Zammad, osTicket, Intercom
- 评分: 4/5
- 备注: 开源主体使用 MIT Expat，但 enterprise 目录有单独许可证；生产前要确认渠道接入、客服权限、会话保留和企业功能边界。

## Zammad

- GitHub: https://github.com/zammad/zammad
- 官网: https://zammad.org
- 模块: 客户支持 / 工单系统 / 服务台
- 技术栈: Ruby on Rails, Elasticsearch, PostgreSQL
- 许可证: AGPL-3.0
- 适合: 需要成熟工单队列、邮件与渠道接入、客服 SLA、知识库、组织客户管理和服务台工作流的团队。
- 不适合: 不能接受 AGPL-3.0 网络服务义务，或没有资源维护搜索、邮件接入和工单规则的项目。
- 接入成本: 中
- 替代方案: Chatwoot, osTicket, OTOBO
- 评分: 4/5
- 备注: 功能更偏传统服务台；上线前要验证 AGPL 合规、邮件收发可靠性、搜索索引、权限分组和 SLA 规则。

## osTicket

- GitHub: https://github.com/osTicket/osTicket
- 官网: https://osticket.com
- 模块: 客户支持 / 工单系统 / 帮助台
- 技术栈: PHP, MySQL
- 许可证: GPL-2.0
- 适合: 需要成熟自托管工单系统、邮件转工单、客服分配、客户门户和基础 SLA 流程的团队。
- 不适合: 需要现代实时聊天、全渠道客服运营、深度自动化或不想维护 PHP/MySQL 帮助台的项目。
- 接入成本: 低
- 替代方案: Zammad, Chatwoot, OTOBO
- 评分: 4/5
- 备注: 适合传统工单和共享邮箱场景；上线前要确认 GPL 合规、邮件收发、权限分组、备份和升级路径。
