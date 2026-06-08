# 反滥用与验证码组件

反滥用与验证码组件覆盖验证码、人机验证、登录防爆破、表单防刷、接口限流、反垃圾和基础机器人防护；依赖漏洞扫描放在安全扫描分类，入口代理限流放在 API 网关分类，字段合法性校验放在表单与校验分类，LLM 输入输出护栏和结构化响应放在 LLM 护栏与结构化输出分类。反滥用策略通常需要和认证、评论、论坛、支付、Webhook、监控和审计日志一起设计，不能只接一个验证码控件就结束。

## ALTCHA

- GitHub: https://github.com/altcha-org/altcha
- 官网: https://altcha.org
- 模块: 反滥用 / 隐私友好 CAPTCHA / Proof-of-Work
- 技术栈: TypeScript, Web Components, JavaScript
- 许可证: MIT
- 适合: 登录、注册、评论、表单和 API 入口需要隐私友好、可自托管、无追踪的人机验证组件。
- 不适合: 需要现成托管风控评分、设备指纹、复杂行为分析或企业级风险决策平台的场景。
- 接入成本: 低
- 替代方案: mCaptcha, hCaptcha, reCAPTCHA
- 评分: 4/5
- 备注: 适合作为传统图片验证码替代；上线前要确认挑战生成、服务端验证、重放防护、难度参数、无障碍体验和高峰期 CPU 成本。

## mCaptcha

- GitHub: https://github.com/mCaptcha/mCaptcha
- 官网: https://mcaptcha.org
- 模块: 反滥用 / 自托管 CAPTCHA 服务 / Proof-of-Work
- 技术栈: Rust, Actix Web, PostgreSQL, MariaDB
- 许可证: AGPL-3.0
- 适合: 需要完整自托管 CAPTCHA 服务、隐私优先、人机验证、站点密钥管理和 PoW 挑战的组织。
- 不适合: 无法接受 AGPL 网络服务义务，或只需要前端嵌入式轻量验证、不想维护独立服务的项目。
- 接入成本: 中
- 替代方案: ALTCHA, Friendly Captcha, hCaptcha
- 评分: 4/5
- 备注: 更像独立验证码平台；生产前要验证部署拓扑、数据库、密钥轮换、挑战过期、失败日志、可用性和许可证边界。

## rate-limiter-flexible

- GitHub: https://github.com/animir/node-rate-limiter-flexible
- 官网: https://github.com/animir/node-rate-limiter-flexible
- 模块: 反滥用 / 应用限流 / 防暴力破解
- 技术栈: JavaScript, Node.js, Redis, Valkey, PostgreSQL, MySQL, MongoDB
- 许可证: ISC
- 适合: Node.js 后端需要登录失败计数、IP/用户/API Key 限流、分布式计数、DoS 缓解和暴力破解防护。
- 不适合: 非 Node.js 技术栈，或需要全局边缘防护、WAF、Bot Management 和托管风控评分的系统。
- 接入成本: 中
- 替代方案: Envoy ratelimit, express-rate-limit, API 网关限流插件
- 评分: 4/5
- 备注: 适合在应用层按用户、租户和业务动作做精细限制；要设计 Redis/数据库故障策略、滑动窗口、封禁时长、误伤申诉和监控告警。
