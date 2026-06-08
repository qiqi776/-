# 支付组件

支付组件覆盖支付 SDK、电商引擎、结账、订阅和计费基础。

## Stripe Node SDK

- GitHub: https://github.com/stripe/stripe-node
- 官网: https://stripe.com/docs
- 模块: 支付 / 计费 SDK
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: 在 Node.js 应用中接入 Stripe 支付、订阅、Checkout、发票和计费流程。
- 不适合: 需要支付供应商无关抽象，或目标地区无法使用 Stripe。
- 接入成本: 中
- 替代方案: Adyen SDK, Paddle SDK, 其他支付供应商 SDK
- 评分: 4/5
- 备注: SDK 是开源的，但支付平台本身是商业依赖。

## Medusa

- GitHub: https://github.com/medusajs/medusa
- 官网: https://medusajs.com
- 模块: 支付 / 电商 / 后端
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: 自定义电商后端、商品目录、购物车、订单和可扩展电商工作流。
- 不适合: 只需要一个简单结账按钮，或不想拥有电商后端复杂度。
- 接入成本: 高
- 替代方案: Saleor, Vendure, Shopify 集成
- 评分: 4/5
- 备注: 应视为电商平台组件，不是小型支付工具。

## Kill Bill

- GitHub: https://github.com/killbill/killbill
- 官网: https://killbill.io
- 模块: 支付 / 计费
- 技术栈: Java
- 许可证: Apache-2.0
- 适合: 订阅计费、发票、支付工作流和复杂计费领域。
- 不适合: 只需要简单 Checkout 或轻量 SaaS 订阅。
- 接入成本: 高
- 替代方案: Lago, Stripe Billing, Chargebee 集成
- 评分: 3/5
- 备注: 计费能力强，但会增加运维和领域复杂度。

