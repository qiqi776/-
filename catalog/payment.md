# 支付组件

支付组件覆盖支付 SDK、结账入口、支付网关接入和收款通道；商品目录、购物车和订单放在电商分类，订阅账单、发票、用量计费和客户账务统一放在账单与发票分类。

## Stripe Node SDK

- GitHub: https://github.com/stripe/stripe-node
- 官网: https://stripe.com/docs
- 模块: 支付 / SDK / 结账
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: 在 Node.js 应用中接入 Stripe 支付、订阅、Checkout、发票和计费流程。
- 不适合: 需要支付供应商无关抽象，或目标地区无法使用 Stripe。
- 接入成本: 中
- 替代方案: Adyen SDK, Paddle SDK, 其他支付供应商 SDK
- 评分: 4/5
- 备注: SDK 是开源的，但支付平台本身是商业依赖；复杂账单模型应单独评估账单与发票组件。
