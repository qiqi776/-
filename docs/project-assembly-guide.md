# 项目拼装指南

用这个流程从开源组件中拼装一个新项目。

## 1. 定义模块地图

先写清楚项目需要哪些能力，再开始选工具。

可以直接复制 [../templates/project-assembly-worksheet.md](../templates/project-assembly-worksheet.md)，作为项目选型工作表；如果已经知道需要哪些模块，也可以直接生成一份已经填入候选组件的工作表草案。

如果是在本仓库里先做选型，推荐先生成工作表草案：

```powershell
python tools/generate_project_package.py --project-name "SaaS 示例" --preset saas-starter --output-dir project-package
python tools/generate_worksheet.py --list-presets
python tools/generate_worksheet.py --project-name "SaaS 示例" --preset saas-starter --output stack-selection.md
python tools/generate_worksheet.py --project-name "后台示例" --preset "内部管理后台" --output stack-selection.md
```

`--list-presets` 会列出每个预设的中文项目类型、适用场景、可用写法和目录模块。`generate_project_package.py` 会一次生成 `stack-plan.json`、`component-manifest.md`、`risk-check.md`、`integration-plan.md`、`architecture-map.md`、`integration-contracts.md`、`assembly-checklist.md`、`component-decisions.md`、`github-issues.md`、`github-labels.json`、`github-import-commands.md`、`github-issue-template.yml`、`github-pr-template.md`、`CONTRIBUTING.md`、`.env.example`、`PROJECT-README.md` 和说明 README，适合直接放进新项目仓库作为拼装起点。`integration-plan.md` 会按缺失组件、许可证和接入成本风险排序，提示先验证哪个集成；`architecture-map.md` 会把已选模块渲染成组件连接图和连接清单，方便先确认组件之间怎么拼；`integration-contracts.md` 会把架构连接拆成接口、数据、配置、密钥、失败处理和监控责任清单，适合在模块对接前逐条确认；`assembly-checklist.md` 会把每个组件拆成带负责人、状态、风险确认和验收动作的复选任务，适合复制到项目看板或 GitHub Issue；`component-decisions.md` 会记录每个能力的主组件、备选组件、选择理由、风险和切换条件，方便后续复用或替换组件；`github-issues.md` 会把每个组件接入拆成可复制到 GitHub Issues 的中文任务草案，并带上分类和风险标签；`github-labels.json` 会生成与这些 Issue 草案匹配的分类和风险标签配置；`github-import-commands.md` 会生成可复制执行的 GitHub CLI 命令清单，但不会自动访问或修改 GitHub；`github-issue-template.yml` 可复制到目标仓库 `.github/ISSUE_TEMPLATE/component-integration.yml`，统一后续组件接入表单；`github-pr-template.md` 可复制到目标仓库 `.github/pull_request_template.md`，统一组件接入 PR 检查项；`CONTRIBUTING.md` 可放入目标项目仓库，统一新增或替换开源组件的贡献规则；`.env.example` 会按已选组件生成启用开关、服务地址和 API Key 占位，提醒不要提交真实密钥；`PROJECT-README.md` 会生成可放进目标项目仓库的中文 README 草案，记录技术栈、优先集成、配置和维护规则。`generate_worksheet.py` 会把主组件、备选组件、选择理由、许可证检查、项目接入清单和优先验证项写进同一份 Markdown。项目接入清单会集中列出主组件 GitHub、官网、接入成本和首个动作，优先验证项会把许可证、接入成本或缺失组件风险更高的集成排在更前面。内置预设包括 `saas-starter`、`ai-rag-app` 和 `internal-admin`，`--preset` 也可以直接写 `内部管理后台` 这类中文项目类型；如果这些蓝图不匹配项目，可以改用 `--modules` 传入自定义分类列表。脚本不会替代人工判断，特别是许可证、数据边界、托管方式和业务合规仍要逐项确认。

示例：

```md
# 项目模块地图

- 前端应用:
- 移动端应用:
- 组件工作台与设计系统文档:
- 管理后台:
- 内部工具:
- 表单与校验:
- 国际化:
- 翻译管理与本地化平台:
- 后端 API:
- API 文档:
- API 客户端与 SDK 生成:
- API 网关:
- 边缘交付:
- 服务网格:
- 代码托管与版本协作:
- 工程化:
- 包与制品仓库:
- 项目脚手架与模板生成:
- 认证:
- 授权策略:
- 数字身份与可验证凭证:
- 审计日志:
- 数据库:
- 数据库迁移:
- 数据管道:
- 数据导入导出:
- 流处理:
- 数据仓库:
- 数据质量:
- 数据治理:
- 数据标注与人工审核:
- 备份恢复:
- 向量数据库与检索:
- 模型服务与推理网关:
- LLM 护栏与结构化输出:
- LLM 可观测性与评估:
- 文件存储:
- 文档处理:
- OCR 与文档识别:
- 文档生成与模板输出:
- 电子签名:
- 媒体处理:
- 邮件通知:
- 通知触达:
- 通信渠道与短信语音:
- Webhook 投递:
- 状态页:
- 评论互动:
- 论坛社区:
- 用户反馈:
- 客户支持:
- CRM:
- 营销自动化:
- 电商:
- 项目管理:
- 日程预约:
- AI / LLM:
- 内容管理:
- 文档站与开发者门户:
- 富文本编辑:
- 文档协作:
- 搜索:
- 缓存:
- 消息队列:
- 后台任务:
- 工作流 / 任务编排:
- 实时通信:
- 音视频通话:
- 产品分析:
- 商业智能:
- 图表可视化:
- 地图地理:
- 功能开关:
- 配置密钥:
- 隐私合规:
- 反滥用:
- 支付:
- 账单与发票:
- 财务会计:
- 基础设施即代码:
- 容器镜像:
- 部署:
- CI/CD:
- 测试:
- 性能与负载测试:
- 无障碍与可访问性测试:
- 安全扫描:
- SBOM 许可证合规:
- 错误跟踪:
- 日志管理:
- 监控:
```

## 2. 按能力选择候选组件

打开对应的 catalog 文件，为每个能力选择：

- 1 个主组件。
- 1 个备选组件。
- 选择主组件的理由。
- 可能迫使你切换到备选组件的主要风险。

## 3. 检查兼容性

实现前至少检查：

- 许可证是否兼容。
- 托管方式和运行环境是否可接受。
- 编程语言和框架是否符合团队能力。
- 组件 story、Mock 数据、设计系统文档、视觉回归、可访问性检查和静态发布责任是否清楚。
- 翻译资源同步、语言回退、术语表、翻译记忆、审核流程、上下文截图、分支版本和发布责任是否清楚。
- 代码仓库权限、分支保护、代码评审、合并策略、SSH/HTTP 访问、备份、Webhook/CI 集成和迁移路径是否清楚。
- 认证边界是否清楚。
- 授权模型是否能覆盖角色、资源关系和审计需求。
- DID 方法、凭证格式、Issuer/Verifier/Wallet 责任、密钥托管、撤销机制和协议互操作是否清楚。
- 审计事件命名、操作者归因、资源标识、保留周期、导出和查看权限是否清楚。
- 数据归属和迁移路径是否可控。
- 数据同步、重跑和 schema 演进是否有可验证方案。
- CSV/Excel 导入的字段映射、错误行反馈、幂等、回滚、编码和大文件限制是否清楚。
- 流处理的事件时间、状态恢复、重放策略和反压处理是否明确。
- 分析查询和业务主库是否隔离，资源成本是否可控。
- 数据质量规则是否覆盖空值、唯一性、分布漂移、延迟和关键业务口径。
- 数据资产所有权、元数据刷新、血缘可信度和治理责任是否明确。
- 标注任务定义、标签体系、标注员权限、质检抽样、一致性评估、导入导出格式和隐私隔离是否清楚。
- 通知渠道、退订规则和告警噪音是否可控。
- 短信、语音、号码资源、国家地区覆盖、退订规则、送达回执、录音、费用和通信合规边界是否清楚。
- Webhook 事件 schema、签名、幂等、重试、失败告警和客户端点权限是否清楚。
- 状态页组件、事故等级、维护窗口、订阅通知、历史保留和对外沟通责任是否清楚。
- 评论登录方式、审核策略、反垃圾、通知、数据归属和迁移路径是否清楚。
- 论坛分类、用户信任等级、版主管理、反垃圾、邮件通知、SSO 和社区治理规则是否清楚。
- OCR 的输入格式、语言包、版面识别、置信度阈值、预处理、批量性能、隐私隔离和错误复核流程是否清楚。
- 文档生成的模板来源、字段映射、字体、分页、图片资源、批量生成性能、文件存储、权限和归档策略是否清楚。
- 电子签名的签署人身份、邮件送达、签署证据、完成证书、文件存储、审计留痕和法律合规边界是否清楚。
- 反馈入口、问卷触发、匿名策略、NPS 口径、数据保留和公开投票范围是否清楚。
- 客服会话、工单 SLA、邮件送达、权限分组和客户数据保留是否清楚。
- 客户、联系人、线索、商机、销售阶段和客户主数据归属是否定义清楚。
- 用户分群、退订偏好、活动频控、触达日志和隐私合规是否清楚。
- 商品目录、购物车、订单状态、库存、促销、支付和履约边界是否清楚。
- 项目空间、Issue 权限、任务状态、路线图、通知和归档策略是否清楚。
- 可用时间规则、时区、日历同步权限、会议链接、预约冲突和取消改期流程是否清楚。
- 知识库空间、页面权限、协同编辑、版本历史、搜索、导出、备份、SSO 和数据迁移边界是否清楚。
- 文档站的信息架构、版本化、多语言、搜索、部署目标、链接检查、贡献流程和文档归属是否清楚。
- WebRTC 信令、TURN/STUN、房间权限、录制、带宽成本、区域部署和通话质量监控是否清楚。
- 后台任务是否具备幂等、重试、超时、死信处理和 worker 监控。
- Cookie 同意、隐私偏好、数据主体请求、同意日志和数据地图是否满足目标地区要求。
- 验证码、登录失败限制、接口限流、误伤处理、挑战过期、重放防护和风控告警是否清楚。
- 账单口径、发票税务、退款流程和支付网关边界是否清楚。
- 会计科目、预算口径、费用分类、银行账户、报表和税务边界是否清楚。
- BI 元数据库、数据源凭据、查询权限、缓存、导出、定时报表、嵌入方式和资源限制是否清楚。
- 向量维度、embedding 模型、索引类型、召回率评估集、元数据过滤、权限隔离、备份恢复、冷热数据和扩缩容路径是否清楚。
- 模型来源、模型许可证、上下文长度、推理硬件、吞吐延迟、网关路由、密钥隔离、成本限额、缓存和降级策略是否清楚。
- LLM 输入输出策略、结构化 schema、拒答规则、工具调用边界、校验失败重试、误拒率、敏感内容处理和人工升级流程是否清楚。
- LLM 调用追踪字段、Prompt 版本、评估数据集、RAG 指标、人工反馈、敏感信息脱敏、采样率、保留周期和红队测试阈值是否清楚。
- 异常上报 SDK、版本标记、源码映射、敏感字段脱敏、采样率、告警路由和错误保留周期是否清楚。
- 日志采集范围、字段规范、敏感信息脱敏、保留周期、查询权限、存储成本、背压丢弃策略和告警联动是否清楚。
- SBOM 格式、生成时机、制品绑定、许可证允许清单、例外审批和归因报告是否清楚。
- 压测目标、并发模型、测试数据、执行节点、限流边界、延迟阈值、失败判定、报告归档和生产保护策略是否清楚。
- 可访问性测试的 WCAG 目标级别、规则引擎、页面状态覆盖、CI 阈值、忽略清单、人工复核和辅助技术验证责任是否清楚。
- API 是否稳定。
- OpenAPI 规范来源、生成器版本、生成代码提交策略、客户端认证注入、错误模型和破坏性接口变更检查是否清楚。
- 包仓库格式、上游代理、发布权限、制品保留策略、存储备份、凭据、缓存污染防护和迁移路径是否清楚。
- 项目模板来源、模板版本、生成后文件覆盖策略、模板升级路径和团队约定是否清楚。
- 部署复杂度是否匹配项目规模。
- 监控和调试路径是否明确。

可以先用风险检查脚本生成一版人工复核表：

```powershell
python tools/check_stack.py --components FastAPI,PostgreSQL,Grafana
python tools/check_stack.py --stack-plan stack-plan.json
```

脚本只根据目录中已有字段提示明显风险，不能替代正式的许可证、数据合规和生产架构审查。`--stack-plan` 可以直接读取组合生成器 JSON 清单里的主组件，适合在选型后批量检查许可证和接入成本风险。

## 4. 形成技术栈决策

把决策写进项目仓库。

可以先用组合生成器生成一版 Markdown 表格，再粘贴到工作表或项目架构文档中：

```powershell
python tools/generate_project_package.py --project-name "后台示例" --preset "内部管理后台" --output-dir project-package
python tools/assemble_stack.py --list-presets
python tools/assemble_stack.py --preset saas-starter
python tools/assemble_stack.py --preset "内部管理后台"
python tools/assemble_stack.py --modules frontend,backend,auth,database,deployment,observability
python tools/assemble_stack.py --modules 后端,认证,数据库
python tools/assemble_stack.py --preset "内部管理后台" --format json
python tools/assemble_stack.py --preset "内部管理后台" --format json --output stack-plan.json
python tools/assemble_stack.py --preset "内部管理后台" --format manifest --output component-manifest.md
python tools/check_stack.py --stack-plan stack-plan.json
```

组合生成器适合先快速比较主组件和备选组件，并在同一张表里看到主组件许可证和接入成本。`generate_project_package.py` 会把 JSON 技术栈、组件清单、风险报告、集成实施计划、组件架构图、集成契约清单、拼装执行清单、组件决策记录、GitHub Issue 草案、GitHub Labels 配置、GitHub CLI 导入命令、GitHub Issue 表单模板、GitHub PR 模板、中文贡献指南、环境变量样例和目标项目 README 草案集中写到一个目录；`--preset` 支持英文 slug 和中文项目类型，`--modules` 支持英文分类名和常用中文模块名，例如 `后端,认证,数据库`；默认 Markdown 输出适合复制到决策文档，`--format json` 适合交给脚手架、模板或后续自动化读取，`--format manifest` 适合放进新项目仓库追踪每个能力的主组件、链接、首个动作和待确认事项，`--output` 可以直接把清单保存到新项目仓库。保存 JSON 清单后，可以用 `check_stack.py --stack-plan` 继续检查所有主组件的目录风险。如果需要完整的许可证检查、验证项和最终决策草案，再使用工作表生成器。

如果需要完整工作表，优先使用：

```powershell
python tools/generate_worksheet.py --list-presets
python tools/generate_worksheet.py --project-name "SaaS 示例" --preset saas-starter --output stack-selection.md
python tools/generate_worksheet.py --project-name "后台示例" --preset "内部管理后台" --output stack-selection.md
python tools/generate_worksheet.py --project-name "中文模块示例" --modules 后端,认证,数据库 --output stack-selection.md
```

```md
# 技术栈决策

| 能力 | 主组件 | 备选组件 | 选择理由 | 主要风险 |
| --- | --- | --- | --- | --- |
| 认证 | Supabase Auth | Keycloak | 能快速完成登录和用户系统 | 不一定适合复杂企业 IAM |
| 后端 | FastAPI | NestJS | Python API 开发快，适合 AI 项目 | 团队可能更偏好 TypeScript |
```

## 5. 先验证风险最高的集成

不要因为 UI 最容易做就先做完整界面。如果项目最大的风险是认证、支付、账单与发票、AI 检索、LLM 护栏、LLM 评估或部署，应该先用最小样例验证这些模块。

## 6. 沉淀可复用模板

某个组件在真实项目中验证有效后，再把可运行示例或模板放到 `components/`。
