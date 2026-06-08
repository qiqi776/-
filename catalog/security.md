# 安全扫描组件

安全扫描组件覆盖依赖漏洞、容器镜像、基础设施配置、密钥泄露和 Web 应用动态安全测试。

## Trivy

- GitHub: https://github.com/aquasecurity/trivy
- 官网: https://trivy.dev
- 模块: 安全扫描 / 依赖与镜像漏洞
- 技术栈: Go, CLI, Docker, Kubernetes, IaC
- 许可证: Apache-2.0
- 适合: 需要在 CI/CD 中扫描容器镜像、文件系统、依赖、IaC 配置、SBOM 和已知漏洞的团队。
- 不适合: 只需要运行时防护，或团队没有流程处理扫描结果和漏洞例外。
- 接入成本: 中
- 替代方案: Grype, Snyk CLI, Docker Scout
- 评分: 4/5
- 备注: 建议固定工具版本、定期更新漏洞库，并先从高危漏洞阻断开始，避免 CI 噪音过高。

## Gitleaks

- GitHub: https://github.com/gitleaks/gitleaks
- 官网: https://gitleaks.io
- 模块: 安全扫描 / 密钥泄露检查
- 技术栈: Go, CLI
- 许可证: MIT
- 适合: 需要扫描代码仓库、提交历史、CI 产物和开发者本地提交中的 API Key、Token、私钥等敏感信息。
- 不适合: 需要统一密钥托管、轮换和运行时注入的完整密钥管理平台。
- 接入成本: 低
- 替代方案: detect-secrets, TruffleHog, GitGuardian
- 评分: 4/5
- 备注: 扫描发现泄露后不能只删除文件，必须轮换对应密钥；适合和 pre-commit、CI 一起使用。

## ZAP

- GitHub: https://github.com/zaproxy/zaproxy
- 官网: https://www.zaproxy.org
- 模块: 安全扫描 / Web 动态安全测试
- 技术栈: Java
- 许可证: Apache-2.0
- 适合: Web 应用需要自动化基线扫描、爬虫扫描、主动扫描和上线前安全回归验证。
- 不适合: 希望完全替代人工渗透测试，或生产环境无法承受主动扫描流量的项目。
- 接入成本: 中
- 替代方案: Nuclei, Burp Suite, Nikto
- 评分: 4/5
- 备注: 建议先在预发环境做基线扫描，再逐步引入主动扫描；主动扫描可能触发写操作或告警。
