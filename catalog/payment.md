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
- 替代方案: Adyen Node API Library, Hyperswitch, 其他支付供应商 SDK
- 评分: 4/5
- 备注: SDK 是开源的，但支付平台本身是商业依赖；复杂账单模型应单独评估账单与发票组件。

## Hyperswitch

- GitHub: https://github.com/juspay/hyperswitch
- 官网: https://hyperswitch.io
- 模块: 支付 / 支付编排 / 多 PSP 路由
- 技术栈: Rust, PostgreSQL, Redis, Docker
- 许可证: Apache-2.0
- 适合: 团队需要自托管支付基础设施、多支付处理器连接、智能路由、重试、支付方式编排、金库和支付观测。
- 不适合: 只需要一个 Stripe Checkout 或单一支付服务商，或团队没有 PCI、支付风控、对账和高可用运维能力。
- 接入成本: 高
- 替代方案: Stripe Node SDK, Adyen Node API Library, 自研支付编排层
- 评分: 4/5
- 备注: 适合支付体量和供应商复杂度已经上来的团队；上线前要重点验证合规边界、密钥与卡数据处理、Webhook、对账、失败补偿和支付渠道覆盖。

## Adyen Node API Library

- GitHub: https://github.com/Adyen/adyen-node-api-library
- 官网: https://docs.adyen.com/development-resources/libraries
- 模块: 支付 / SDK / 收单与平台支付
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: Node.js 应用需要接入 Adyen Checkout、Payments、Payouts、Platforms、终端支付和管理 API。
- 不适合: 目标地区或业务模型不适合 Adyen，或团队需要完全支付服务商无关的自托管支付编排层。
- 接入成本: 中
- 替代方案: Stripe Node SDK, Hyperswitch, 直接调用支付服务商 API
- 评分: 4/5
- 备注: 官方 SDK 成熟且许可证清楚，但支付平台本身是商业依赖；上线前要确认地区覆盖、PCI 边界、Webhook、幂等、对账和退款流程。
