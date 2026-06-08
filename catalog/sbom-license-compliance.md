# SBOM 与许可证合规组件

SBOM 与许可证合规组件覆盖软件物料清单生成、依赖许可证识别、版权扫描、第三方组件归因、许可证策略校验和开源合规报告；漏洞扫描放在安全扫描分类，隐私请求和 Cookie 同意放在隐私合规分类，数据资产目录放在数据治理分类。这个分类适合在 CI/CD、发布审计和企业采购合规中使用，不应替代正式法务审查。

## Syft

- GitHub: https://github.com/anchore/syft
- 官网: https://github.com/anchore/syft
- 模块: SBOM / 依赖清单 / 容器镜像
- 技术栈: Go, SPDX, CycloneDX, OCI
- 许可证: Apache-2.0
- 适合: 需要从容器镜像、文件系统、包管理器和源码目录生成 SPDX/CycloneDX SBOM 的 CI/CD 或安全供应链流程。
- 不适合: 需要深度源码许可证文本识别、版权归因审查或复杂法务审批工作流的场景。
- 接入成本: 中
- 替代方案: ScanCode Toolkit, Trivy SBOM, cdxgen
- 评分: 4/5
- 备注: 适合和 Grype、Trivy、签名/制品系统组合；生产前要确认 SBOM 格式、制品绑定、生成时机、存档位置和漏洞扫描链路。

## ScanCode Toolkit

- GitHub: https://github.com/aboutcode-org/scancode-toolkit
- 官网: https://scancode-toolkit.readthedocs.io/
- 模块: 许可证合规 / 源码扫描 / 第三方归因
- 技术栈: Python, SPDX, CycloneDX, Package URL
- 许可证: Apache-2.0 / CC-BY-4.0 / Other
- 适合: 需要扫描源码、依赖、版权声明、许可证文本、归因信息和第三方组件清单的开源合规团队。
- 不适合: 只需要快速生成应用依赖 SBOM，或无法处理扫描结果中的许可证例外、误报和人工复核流程。
- 接入成本: 高
- 替代方案: Syft, LicenseFinder, FOSSology
- 评分: 4/5
- 备注: 扫描深度强但结果解释成本高；上线前要确认扫描范围、规则版本、许可证例外库、归因模板、性能和报告归档。

## LicenseFinder

- GitHub: https://github.com/pivotal/LicenseFinder
- 官网: https://github.com/pivotal/LicenseFinder
- 模块: 许可证合规 / 依赖策略 / 包管理器扫描
- 技术栈: Ruby, Bundler, npm, pip, Maven, Gradle
- 许可证: MIT
- 适合: 多语言应用需要按包管理器识别依赖许可证，并用允许/禁止列表生成可执行的许可证例外报告。
- 不适合: 需要生成完整 SBOM、扫描源码版权声明、识别 vendored 代码或做企业级第三方组件治理平台的场景。
- 接入成本: 中
- 替代方案: ScanCode Toolkit, REUSE, FOSSA
- 评分: 3/5
- 备注: 适合在 CI 中建立许可证门禁；选型时要复核维护活跃度、包管理器覆盖、许可证映射准确性和人工审批流程。
