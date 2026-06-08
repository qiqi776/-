# 电商与订单组件

电商与订单组件覆盖商品目录、购物车、订单、库存、促销、履约和电商 API；支付 SDK 和收款通道放在支付分类，订阅账单、发票和用量计费放在账单与发票分类，内容编辑放在内容管理分类。

## Medusa

- GitHub: https://github.com/medusajs/medusa
- 官网: https://medusajs.com
- 模块: 电商 / 商品目录 / 订单后端
- 技术栈: TypeScript, Node.js, PostgreSQL
- 许可证: MIT
- 适合: 需要自定义电商后端、商品目录、购物车、订单、促销、库存和可扩展工作流的团队。
- 不适合: 只需要一个简单结账按钮，或不想维护电商领域模型、库存和订单状态机的项目。
- 接入成本: 高
- 替代方案: Saleor, Vendure, Shopify 集成
- 评分: 4/5
- 备注: 更适合作为可定制 commerce backend，而不是支付工具；要提前设计商品模型、支付集成、订单履约和后台运营流程。

## Saleor

- GitHub: https://github.com/saleor/saleor
- 官网: https://saleor.io
- 模块: 电商 / GraphQL API / 商品与订单
- 技术栈: Python, Django, GraphQL, PostgreSQL
- 许可证: BSD-3-Clause
- 适合: 需要 headless commerce、GraphQL API、多渠道商品目录、订单、折扣和可扩展电商后端的团队。
- 不适合: 只需要轻量店铺页面，或团队没有 GraphQL、Django 和电商运营后台维护经验。
- 接入成本: 高
- 替代方案: Medusa, Vendure, WooCommerce
- 评分: 4/5
- 备注: API 设计成熟，适合和自定义前端拼装；上线前要验证渠道模型、插件、税费、支付和履约集成。

## Vendure

- GitHub: https://github.com/vendure-ecommerce/vendure
- 官网: https://www.vendure.io
- 模块: 电商 / Headless Commerce / 订单与插件
- 技术栈: TypeScript, Node.js, GraphQL, NestJS
- 许可证: GPL-3.0-or-later
- 适合: TypeScript 团队需要可插件化 headless commerce、商品目录、订单、库存、促销和管理后台扩展。
- 不适合: 项目许可证策略不能接受 GPL-3.0-or-later，或只需要托管式低维护网店。
- 接入成本: 高
- 替代方案: Medusa, Saleor, Shopify 集成
- 评分: 4/5
- 备注: 插件架构清晰，但 GPL 和商业许可边界要提前确认；要评估 GraphQL API、支付插件、履约和升级策略。
