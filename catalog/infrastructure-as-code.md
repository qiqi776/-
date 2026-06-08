# 基础设施即代码组件

基础设施即代码组件覆盖云资源声明、环境编排、配置管理、状态管理和基础设施变更审计。

## OpenTofu

- GitHub: https://github.com/opentofu/opentofu
- 官网: https://opentofu.org
- 模块: 基础设施即代码 / Terraform 兼容
- 技术栈: Go, HCL, CLI
- 许可证: MPL-2.0
- 适合: 需要 Terraform 生态兼容、声明式管理云资源、模块复用和开源治理的团队。
- 不适合: 团队已经深度依赖 Terraform Cloud 专有能力，或只需要手动管理极少量云资源。
- 接入成本: 高
- 替代方案: Terraform, Pulumi, Crossplane
- 评分: 4/5
- 备注: 适合多环境基础设施治理；要设计远程状态、锁、权限边界、模块版本和变更审批流程。

## Pulumi

- GitHub: https://github.com/pulumi/pulumi
- 官网: https://www.pulumi.com
- 模块: 基础设施即代码 / 编程语言式 IaC
- 技术栈: Go, TypeScript, Python, C#, Java
- 许可证: Apache-2.0
- 适合: 团队希望用熟悉的编程语言定义云资源，并复用类型系统、函数抽象和测试工具。
- 不适合: 团队更偏好纯声明式 HCL，或不希望基础设施定义里出现复杂程序逻辑。
- 接入成本: 高
- 替代方案: OpenTofu, Terraform, AWS CDK
- 评分: 4/5
- 备注: 灵活度高但也容易过度抽象；要约束代码结构、状态后端、密钥处理和跨环境配置。

## Ansible

- GitHub: https://github.com/ansible/ansible
- 官网: https://www.ansible.com
- 模块: 基础设施即代码 / 配置管理
- 技术栈: Python, YAML, SSH
- 许可证: GPL-3.0-or-later
- 适合: 需要通过 SSH 管理服务器配置、应用部署、系统初始化和重复运维任务的团队。
- 不适合: 只管理云资源生命周期，或产品需要把 Ansible 作为嵌入式库分发但无法接受 GPL 义务。
- 接入成本: 高
- 替代方案: Salt, Chef, Puppet
- 评分: 4/5
- 备注: 适合传统服务器和混合环境自动化；要维护幂等性、主机清单、凭据边界和剧本评审流程。
