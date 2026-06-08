# 账单与发票组件

账单与发票组件覆盖订阅账单、用量计量、发票生成、客户账务和收款编排；支付 SDK、结账入口和电商订单仍放在支付分类。

## Lago

- GitHub: https://github.com/getlago/lago
- 官网: https://www.getlago.com
- 模块: 账单与发票 / 用量计费 / 订阅管理
- 技术栈: Ruby on Rails, TypeScript, PostgreSQL
- 许可证: AGPL-3.0
- 适合: 需要自托管用量计费、订阅账单、发票生成、多支付网关编排和收入分析的 SaaS 产品。
- 不适合: 只需要一个简单收款按钮，或无法接受 AGPL 网络服务义务的闭源商业系统。
- 接入成本: 高
- 替代方案: OpenMeter, Kill Bill, Stripe Billing
- 评分: 4/5
- 备注: 账单领域模型完整，但许可证、数据同步和财务口径需要提前审查。

## OpenMeter

- GitHub: https://github.com/openmeterio/openmeter
- 官网: https://openmeter.io
- 模块: 账单与发票 / 用量计量 / 限额
- 技术栈: Go, TypeScript, ClickHouse, Kafka
- 许可证: Apache-2.0
- 适合: AI、API、DevTool、FinOps 等需要高频用量采集、实时聚合、限额和用量计费的产品。
- 不适合: 没有事件流和用量维度的小型订阅产品，或团队不想维护 ClickHouse / Kafka。
- 接入成本: 高
- 替代方案: Lago, M3ter, 自建用量计量服务
- 评分: 4/5
- 备注: 更偏实时用量计量基础设施，落地时要先定义事件 schema、幂等策略和计费窗口。

## Kill Bill

- GitHub: https://github.com/killbill/killbill
- 官网: https://killbill.io
- 模块: 账单与发票 / 订阅计费 / 支付编排
- 技术栈: Java
- 许可证: Apache-2.0
- 适合: 订阅计费、发票、支付工作流、账户账务和复杂计费领域。
- 不适合: 只需要简单 Checkout、轻量 SaaS 订阅，或团队没有 Java 计费系统运维经验。
- 接入成本: 高
- 替代方案: Lago, OpenMeter, Stripe Billing
- 评分: 3/5
- 备注: 计费能力强且成熟，但会显著增加运维、集成和财务领域复杂度。
