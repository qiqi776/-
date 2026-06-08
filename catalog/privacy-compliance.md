# 隐私合规与同意管理组件

隐私合规与同意管理组件覆盖 Cookie 和追踪同意、隐私偏好、数据主体请求、数据地图和合规工作流；登录身份放在认证分类，漏洞与密钥检查放在安全扫描分类，通用数据资产治理放在数据治理分类。

## Fides

- GitHub: https://github.com/ethyca/fides
- 官网: https://ethyca.github.io/fides
- 模块: 隐私合规 / 数据地图 / 数据主体请求
- 技术栈: Python, TypeScript, PostgreSQL
- 许可证: Apache-2.0
- 适合: 需要数据地图、隐私请求履约、同意管理、数据发现和隐私工程工作流的产品或平台团队。
- 不适合: 只需要一个简单 Cookie 弹窗，或没有法务、数据负责人和系统 owner 配合隐私流程的项目。
- 接入成本: 高
- 替代方案: Klaro, tarteaucitron.js, OneTrust
- 评分: 4/5
- 备注: 覆盖面比前端同意弹窗更广，生产前要确认数据源连接权限、审计日志、请求 SLA 和目标地区法规要求。

## Klaro

- GitHub: https://github.com/kiprotect/klaro
- 官网: https://klaro.org
- 模块: 隐私合规 / Cookie 同意 / 前端偏好
- 技术栈: JavaScript
- 许可证: BSD-3-Clause
- 适合: Web 项目需要轻量 Cookie 和追踪同意弹窗、服务分组、多语言文案和用户偏好管理。
- 不适合: 需要完整数据主体请求、数据地图、后端数据源治理或企业级合规审批流。
- 接入成本: 低
- 替代方案: tarteaucitron.js, Fides, CookieConsent
- 评分: 4/5
- 备注: 更适合作为前端同意管理组件；落地时要配合脚本阻断、标签管理、隐私政策和同意记录策略。

## tarteaucitron.js

- GitHub: https://github.com/AmauriC/tarteaucitron.js
- 官网: https://tarteaucitron.io
- 模块: 隐私合规 / Cookie 同意 / 第三方脚本管理
- 技术栈: JavaScript
- 许可证: MIT
- 适合: 营销站、内容站或中小型 Web 项目需要按用户同意加载广告、分析、社交和嵌入服务。
- 不适合: 需要后端隐私请求处理、复杂数据主体工作流、跨系统数据发现或企业级同意审计。
- 接入成本: 低
- 替代方案: Klaro, CookieConsent, Fides
- 评分: 4/5
- 备注: 支持较多第三方服务接入，使用前要审查地区文案、默认服务清单、Google Consent Mode 和标签触发逻辑。
