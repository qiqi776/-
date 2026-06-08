# 服务网格与集群网络组件

服务网格与集群网络组件覆盖服务间 mTLS、流量治理、网络策略、服务可观测性、边车或无边车数据面，以及 Kubernetes 集群中的网络能力增强。

## Istio

- GitHub: https://github.com/istio/istio
- 官网: https://istio.io
- 模块: 服务网格 / 流量治理 / mTLS
- 技术栈: Go, Envoy, Kubernetes
- 许可证: Apache-2.0
- 适合: Kubernetes 平台需要服务间 mTLS、流量拆分、重试熔断、遥测、策略控制和多集群流量治理。
- 不适合: 小型单体或服务数量很少的项目，或团队没有能力维护控制平面和代理调试。
- 接入成本: 高
- 替代方案: Linkerd, Cilium Service Mesh, Kuma
- 评分: 4/5
- 备注: 能力完整但复杂度高；建议先在关键命名空间试点，明确 sidecar/ambient 模式、证书、遥测和故障排查流程。

## Linkerd

- GitHub: https://github.com/linkerd/linkerd2
- 官网: https://linkerd.io
- 模块: 服务网格 / 轻量 mTLS
- 技术栈: Rust, Go, Kubernetes
- 许可证: Apache-2.0
- 适合: 团队需要较轻量的 Kubernetes 服务网格，重点关注自动 mTLS、基础流量指标、重试和渐进式交付集成。
- 不适合: 需要极复杂流量治理、深度 Envoy 生态插件或多维 API 网关能力。
- 接入成本: 中
- 替代方案: Istio, Cilium Service Mesh, Consul
- 评分: 4/5
- 备注: 上手成本通常低于重型网格；要核对边缘路由、HA 控制平面、证书轮换和扩展能力是否满足平台需求。

## Cilium

- GitHub: https://github.com/cilium/cilium
- 官网: https://cilium.io
- 模块: 服务网格 / eBPF 网络 / 网络策略
- 技术栈: Go, eBPF, Kubernetes
- 许可证: Apache-2.0
- 适合: Kubernetes 集群需要 eBPF 网络、网络策略、可观测性、负载均衡，并希望把服务网格能力和 CNI 网络层结合。
- 不适合: 不愿引入 eBPF 运行时要求，或团队只需要应用层 sidecar 网格。
- 接入成本: 高
- 替代方案: Calico, Istio, Linkerd
- 评分: 4/5
- 备注: 仓库用户态组件是 Apache-2.0，BPF 模板有 GPL-2.0-only / BSD-2-Clause 双许可细节；生产前要核对内核版本、网络策略和 Hubble 可观测性。
