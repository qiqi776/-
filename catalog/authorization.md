# 授权与权限策略组件

授权与权限策略组件覆盖 RBAC、ABAC、ReBAC、策略即代码、资源关系授权、集中式权限检查和多服务权限决策。

## Open Policy Agent

- GitHub: https://github.com/open-policy-agent/opa
- 官网: https://www.openpolicyagent.org
- 模块: 授权 / 策略即代码 / ABAC
- 技术栈: Go, Rego, CLI, Kubernetes
- 许可证: Apache-2.0
- 适合: 多服务系统需要把授权、准入控制、配置策略或合规规则集中为可测试、可审计的策略代码。
- 不适合: 只需要简单角色判断，或团队不愿学习 Rego 和策略测试流程。
- 接入成本: 高
- 替代方案: Casbin, Cedar, OpenFGA
- 评分: 4/5
- 备注: 能力强但抽象层较重；建议先从单一授权边界试点，并把策略单元测试、版本发布和决策日志纳入工程流程。

## Casbin

- GitHub: https://github.com/casbin/casbin
- 官网: https://casbin.org
- 模块: 授权 / RBAC / ABAC
- 技术栈: Go, 多语言 SDK
- 许可证: Apache-2.0
- 适合: 应用需要嵌入式权限模型，覆盖 RBAC、ABAC、多租户角色、资源权限和多语言服务接入。
- 不适合: 需要跨系统统一权限审计、关系图授权或托管式权限 API 的大型平台。
- 接入成本: 中
- 替代方案: OPA, OpenFGA, Keycloak Authorization Services
- 评分: 4/5
- 备注: 适合在应用内快速落地权限模型；要提前设计模型文件、策略存储、租户隔离和权限变更审计。

## OpenFGA

- GitHub: https://github.com/openfga/openfga
- 官网: https://openfga.dev
- 模块: 授权 / ReBAC / Zanzibar 模型
- 技术栈: Go, gRPC, HTTP
- 许可证: Apache-2.0
- 适合: 协作产品、文档系统、组织空间、项目资源等需要关系型授权和细粒度共享权限的应用。
- 不适合: 只有少量固定角色的应用，或团队不想维护关系元组、授权模型迁移和权限查询性能。
- 接入成本: 高
- 替代方案: SpiceDB, OPA, Casbin
- 评分: 4/5
- 备注: 适合复杂资源关系授权；生产前要验证模型演进、批量写入、缓存、审计和最坏情况下的权限查询延迟。
