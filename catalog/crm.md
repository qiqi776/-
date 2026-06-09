# CRM 与销售管理组件

CRM 与销售管理组件覆盖客户资料、联系人、线索、商机、销售管线、报价跟进和基础客户运营；客户支持与工单仍放在客户支持分类，营销触达和通知编排仍放在通知触达分类。

## Odoo

- GitHub: https://github.com/odoo/odoo
- 官网: https://www.odoo.com
- 模块: CRM / 销售管理 / 业务应用套件
- 技术栈: Python, JavaScript, PostgreSQL
- 许可证: LGPL-3.0
- 适合: 需要把 CRM、销售、库存、采购、会计、网站和自动化流程放进同一套业务应用平台的团队。
- 不适合: 只需要轻量联系人管理，或不能接受大型业务套件带来的模块选择、定制和升级复杂度。
- 接入成本: 高
- 替代方案: ERPNext, SuiteCRM, Dolibarr
- 评分: 4/5
- 备注: 社区版采用 LGPL-3.0，但企业功能和应用边界要单独确认；落地前要评估定制开发、数据迁移、权限模型和升级策略。

## ERPNext

- GitHub: https://github.com/frappe/erpnext
- 官网: https://erpnext.com
- 模块: CRM / ERP / 销售与客户管理
- 技术栈: Python, JavaScript, MariaDB, Frappe
- 许可证: GPL-3.0
- 适合: 中小企业希望用一套开源系统覆盖 CRM、销售、采购、库存、制造、会计和人事等核心业务流程。
- 不适合: 只需要独立 CRM，或项目许可证策略不能接受 GPL-3.0 copyleft 义务。
- 接入成本: 高
- 替代方案: Odoo, SuiteCRM, Twenty
- 评分: 4/5
- 备注: 适合业务流程一体化，不适合作为随手接入的小组件；生产前要确认 GPL 合规、Frappe 定制能力、主数据建模和迁移计划。

## SuiteCRM

- GitHub: https://github.com/salesagility/SuiteCRM
- 官网: https://suitecrm.com
- 模块: CRM / 销售管线 / 客户运营
- 技术栈: PHP, Symfony, MySQL
- 许可证: AGPL-3.0
- 适合: 需要自托管传统 CRM、客户账户、联系人、线索、商机、活动记录、销售流程和基础报表的团队。
- 不适合: 不能接受 AGPL-3.0 网络服务义务，或希望获得现代轻量 UI 和低维护成本的项目。
- 接入成本: 中
- 替代方案: Odoo, ERPNext, Twenty
- 评分: 4/5
- 备注: 功能覆盖传统 CRM 场景且项目成熟；上线前要确认 AGPL 合规、字段模型、权限、邮件集成和升级路径。
