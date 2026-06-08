# API 网关与反向代理组件

API 网关与反向代理组件覆盖入口流量路由、TLS 终止、限流、鉴权插件、服务发现、Ingress 和服务间代理。

## Kong Gateway

- GitHub: https://github.com/Kong/kong
- 官网: https://konghq.com/products/kong-gateway
- 模块: API 网关 / 插件化网关
- 技术栈: Lua, Nginx, PostgreSQL
- 许可证: Apache-2.0
- 适合: 需要成熟 API 网关、插件生态、限流、认证、路由、上游服务治理和混合部署能力的团队。
- 不适合: 只需要简单反向代理，或不能接受部分高级治理能力属于企业版本。
- 接入成本: 高
- 替代方案: Traefik, APISIX, Envoy
- 评分: 4/5
- 备注: 开源网关能力强，但企业管理面、治理和高级安全能力要单独核对版本；生产前要设计插件、数据库和配置发布流程。

## Traefik

- GitHub: https://github.com/traefik/traefik
- 官网: https://traefik.io/traefik
- 模块: API 网关 / 边缘路由 / Ingress
- 技术栈: Go, Docker, Kubernetes
- 许可证: MIT
- 适合: 容器化或 Kubernetes 项目需要自动服务发现、反向代理、Ingress、TLS 自动化和较轻量边缘路由。
- 不适合: 需要复杂 API 生命周期管理、深度插件市场或专门的企业 API 门户。
- 接入成本: 中
- 替代方案: Caddy, Nginx, Kong Gateway
- 评分: 4/5
- 备注: 适合中小型服务入口和自托管应用；要明确动态配置来源、证书存储、访问日志和限流策略。

## Envoy

- GitHub: https://github.com/envoyproxy/envoy
- 官网: https://www.envoyproxy.io
- 模块: API 网关 / 边车代理 / L7 代理
- 技术栈: C++, xDS, HTTP/2, gRPC
- 许可证: Apache-2.0
- 适合: 需要高性能 L7 代理、服务网格数据面、gRPC、动态配置和复杂流量治理的平台团队。
- 不适合: 小团队只需要简单域名转发，或没有能力维护 xDS 配置和代理调试体系。
- 接入成本: 高
- 替代方案: HAProxy, Nginx, Linkerd proxy
- 评分: 4/5
- 备注: 强大但配置和调试成本高；更适合作为平台底座或被 Istio、Contour 等上层项目托管使用。
