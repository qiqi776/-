# 财务会计与费用管理组件

财务会计与费用管理组件覆盖记账、预算、收支分类、银行账户、费用追踪、财务报表和个人/小企业财务管理；订阅计费和发票放在账单与发票分类，支付收款放在支付分类，商品订单放在电商分类，完整 ERP/CRM 套件放在 CRM 分类。

## Frappe Books

- GitHub: https://github.com/frappe/books
- 官网: https://frappebooks.com
- 模块: 财务会计 / 小企业记账 / 发票
- 技术栈: TypeScript, Vue, Electron, SQLite
- 许可证: AGPL-3.0
- 适合: 小企业、本地桌面记账、发票、分类账、报表和离线优先的轻量财务管理。
- 不适合: 需要 Web SaaS 多租户会计后端，或无法接受 AGPL 许可证义务的闭源商业系统。
- 接入成本: 中
- 替代方案: Actual Budget, Firefly III, ERPNext
- 评分: 4/5
- 备注: 更适合作为桌面会计应用或本地财务工作台参考，接入前要确认数据模型和许可证边界。

## Actual Budget

- GitHub: https://github.com/actualbudget/actual
- 官网: https://actualbudget.org
- 模块: 预算 / 个人财务 / 本地优先
- 技术栈: TypeScript, React, Node.js, SQLite
- 许可证: MIT
- 适合: 个人、家庭或小团队做本地优先预算、账户管理、交易分类、同步和自托管财务记录。
- 不适合: 企业会计、税务开票、应收应付、复杂总账和多主体财务合并场景。
- 接入成本: 中
- 替代方案: Firefly III, Frappe Books, 自建预算模块
- 评分: 4/5
- 备注: 许可证友好且产品边界清楚，但它偏预算管理，不应当替代正式会计系统。

## Firefly III

- GitHub: https://github.com/firefly-iii/firefly-iii
- 官网: https://www.firefly-iii.org
- 模块: 个人财务 / 预算 / 交易管理
- 技术栈: PHP, Laravel, MySQL, PostgreSQL
- 许可证: AGPL-3.0
- 适合: 自托管个人财务、账户、交易、分类、预算、规则、报表和导入流程。
- 不适合: 正式企业会计、税务申报、发票系统，或无法接受 AGPL 网络服务义务的商业项目。
- 接入成本: 中
- 替代方案: Actual Budget, Frappe Books, HomeBank
- 评分: 4/5
- 备注: 功能完整且 API 能力强，作为个人财务模块接入时要先明确隐私、备份和导入格式。
