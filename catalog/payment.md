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

## Hyperswitch

- GitHub: https://github.com/juspay/hyperswitch
- 官网: https://hyperswitch.io
- 模块: 支付 / 支付编排 / 多 PSP 路由
- 技术栈: Rust, PostgreSQL, Redis, Docker
- 许可证: Apache-2.0
- 适合: 团队需要自托管支付基础设施、多支付处理器连接、智能路由、重试、支付方式编排、金库和支付观测。
- 不适合: 只需要一个 Stripe Checkout 或单一支付服务商，或团队没有 PCI、支付风控、对账和高可用运维能力。
- 接入成本: 高
- 替代方案: Stripe SDK, Adyen, 自研支付编排层
- 评分: 4/5
- 备注: 适合支付体量和供应商复杂度已经上来的团队；上线前要重点验证合规边界、密钥与卡数据处理、Webhook、对账、失败补偿和支付渠道覆盖。

## Open Payments Node SDK

- GitHub: https://github.com/interledger/open-payments-node
- 官网: https://openpayments.dev
- 模块: 支付 / Open Payments / 钱包互通
- 技术栈: TypeScript, Node.js, OpenAPI, HTTP Signatures
- 许可证: Apache-2.0
- 适合: 应用需要接入 Open Payments 钱包地址、授权 grant、incoming/outgoing payment、交易历史和开放支付互通场景。
- 不适合: 目标市场没有 Open Payments 钱包生态，或项目只需要传统银行卡收单、结账页和本地支付方式聚合。
- 接入成本: 中
- 替代方案: Stripe Node SDK, Hyperswitch, 直接调用支付服务商 API
- 评分: 3/5
- 备注: 更偏开放支付协议 SDK，不是传统支付网关；落地前要确认钱包提供方、授权流程、签名密钥、合规边界、错误处理和商户结算路径。
