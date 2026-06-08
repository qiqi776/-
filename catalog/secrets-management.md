# 配置与密钥管理组件

配置与密钥管理组件覆盖密钥托管、环境配置、加密入库、运行时注入和 Kubernetes 外部密钥同步。

## Infisical

- GitHub: https://github.com/Infisical/infisical
- 官网: https://infisical.com
- 模块: 配置与密钥管理 / 密钥平台
- 技术栈: TypeScript, Node.js, PostgreSQL, Docker
- 许可证: MIT
- 适合: 团队需要集中管理环境变量、密钥、访问控制、审计日志、轮换流程和多环境配置。
- 不适合: 只需要单项目本地 `.env` 文件，或不想维护额外密钥平台。
- 接入成本: 中
- 替代方案: HashiCorp Vault, Doppler, Bitwarden Secrets Manager
- 评分: 4/5
- 备注: 适合从 `.env` 迁移到团队级密钥管理；自托管时要优先保护备份、管理员账号和审计日志。

## SOPS

- GitHub: https://github.com/getsops/sops
- 官网: https://getsops.io
- 模块: 配置与密钥管理 / GitOps 加密
- 技术栈: Go, CLI, YAML, JSON
- 许可证: MPL-2.0
- 适合: 需要把加密后的密钥文件提交进 Git，并用 KMS、PGP、age 等方式控制解密权限。
- 不适合: 需要完整 Web 管理台、运行时动态密钥租约或集中审计流程。
- 接入成本: 中
- 替代方案: Sealed Secrets, git-crypt, External Secrets Operator
- 评分: 4/5
- 备注: 适合 GitOps 和基础设施配置；要严格管理解密密钥、审查明文落盘路径，并避免把未加密文件提交进仓库。

## External Secrets Operator

- GitHub: https://github.com/external-secrets/external-secrets
- 官网: https://external-secrets.io
- 模块: 配置与密钥管理 / Kubernetes Secret 同步
- 技术栈: Go, Kubernetes, CRD
- 许可证: Apache-2.0
- 适合: Kubernetes 项目需要从 AWS Secrets Manager、Vault、GCP Secret Manager、Azure Key Vault 等外部系统同步 Secret。
- 不适合: 不使用 Kubernetes，或集群里不能安全管理外部密钥访问凭据。
- 接入成本: 高
- 替代方案: Sealed Secrets, Vault CSI Provider, SOPS
- 评分: 4/5
- 备注: 适合生产集群密钥同步；必须设计 RBAC、命名空间边界、刷新周期和外部密钥读权限。
