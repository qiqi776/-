# 营销自动化与活动运营组件

营销自动化与活动运营组件覆盖用户分群、活动编排、线索培育、邮件/短信旅程、营销表单、落地页、客户画像和转化运营；邮件投递基础设施放在邮件通知分类，多渠道通知管道放在通知触达分类，事件分析和漏斗报表放在产品分析分类。

## Mautic

- GitHub: https://github.com/mautic/mautic
- 官网: https://www.mautic.org
- 模块: 营销自动化 / 活动编排 / 线索培育
- 技术栈: PHP, Symfony, MySQL
- 许可证: GPL-3.0-or-later
- 适合: 需要自托管营销自动化、联系人分群、邮件活动、落地页、表单、线索评分和营销旅程的团队。
- 不适合: 只需要事务邮件发送，或项目许可证策略不能接受 GPL-3.0-or-later 的 copyleft 义务。
- 接入成本: 中
- 替代方案: Dittofeed, Apache Unomi, Snowplow
- 评分: 4/5
- 备注: 生态成熟但领域配置较多；生产前要确认邮件投递、退订、数据同步、隐私合规和线索评分口径。

## Dittofeed

- GitHub: https://github.com/dittofeed/dittofeed
- 官网: https://www.dittofeed.com
- 模块: 营销自动化 / 用户旅程 / 消息编排
- 技术栈: TypeScript, Node.js, ClickHouse, Postgres
- 许可证: MIT
- 适合: 需要基于事件和用户属性编排邮件、短信、Push、Webhook 等触达流程的产品团队。
- 不适合: 只需要静态 Newsletter，或团队不想维护事件采集、用户画像、消息供应商和分析存储。
- 接入成本: 中
- 替代方案: Mautic, Apache Unomi, Snowplow
- 评分: 4/5
- 备注: 更偏现代产品化生命周期触达；落地时要设计事件 schema、用户身份合并、退订偏好和触达频控。

## Apache Unomi

- GitHub: https://github.com/apache/unomi
- 官网: https://unomi.apache.org
- 模块: 营销自动化 / 客户数据平台 / 分群
- 技术栈: Java, OSGi, Elasticsearch
- 许可证: Apache-2.0
- 适合: 需要开源客户数据平台、用户画像、规则、分群、个性化和跨系统客户上下文管理的团队。
- 不适合: 只需要邮件营销工具，或没有资源维护 Java 服务、搜索存储和跨系统数据治理的项目。
- 接入成本: 高
- 替代方案: Mautic, Dittofeed, Snowplow
- 评分: 4/5
- 备注: Apache 顶级项目，适合作为客户数据、规则和个性化底座；不是开箱即用的营销后台，落地前要验证数据模型、规则性能和隐私合规。
