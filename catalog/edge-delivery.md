# 边缘交付与 CDN / WAF 组件

边缘交付组件覆盖 CDN 缓存节点、反向缓存、可编程边缘网关、源站保护、WAF 规则执行和静态资源加速。

## Apache Traffic Server

- GitHub: https://github.com/apache/trafficserver
- 官网: https://trafficserver.apache.org
- 模块: 边缘交付 / HTTP 缓存 / CDN 节点
- 技术栈: C++, HTTP, TLS
- 许可证: Apache-2.0
- 适合: 团队需要自建 CDN 节点、反向缓存层、源站保护、高并发 HTTP 代理和可控的缓存失效策略。
- 不适合: 只需要把静态资源放到托管 CDN，或团队没有能力维护缓存节点、证书、日志和回源策略。
- 接入成本: 高
- 替代方案: Varnish Cache, Nginx, OpenResty
- 评分: 4/5
- 备注: 适合作为自建边缘缓存底座；生产前要定义缓存键、回源超时、purge 流程、TLS 终止和可观测性指标。

## OpenResty

- GitHub: https://github.com/openresty/openresty
- 官网: https://openresty.org
- 模块: 边缘交付 / 可编程网关 / Lua 扩展
- 技术栈: C, LuaJIT, Nginx
- 许可证: BSD-2-Clause
- 适合: 需要在 Nginx 兼容边缘层实现自定义路由、鉴权、签名校验、限流、缓存控制和源站保护逻辑的团队。
- 不适合: 团队希望完全托管的 CDN 配置界面，或没有能力调试 Nginx、LuaJIT 和异步 I/O 行为。
- 接入成本: 高
- 替代方案: Nginx, Kong Gateway, Apache APISIX
- 评分: 4/5
- 备注: 灵活性很高，但需要工程化治理配置发布、Lua 模块测试、超时策略和回源降级，避免边缘脚本成为生产风险点。

## Coraza

- GitHub: https://github.com/corazawaf/coraza
- 官网: https://coraza.io
- 模块: 边缘安全 / WAF / 规则引擎
- 技术栈: Go, ModSecurity, OWASP CRS
- 许可证: Apache-2.0
- 适合: 需要可嵌入 WAF 引擎、ModSecurity 兼容规则、OWASP CRS 集成，并希望把攻击检测放到网关或边缘代理里的团队。
- 不适合: 需要托管 DDoS 清洗、全自动 WAF 调优，或没有时间处理误报、规则例外和灰度发布的项目。
- 接入成本: 中
- 替代方案: ModSecurity, NAXSI, BunkerWeb
- 评分: 4/5
- 备注: WAF 规则必须先在预发环境观察误报，再逐步启用阻断模式；它不能替代应用侧鉴权、输入校验和安全编码。
