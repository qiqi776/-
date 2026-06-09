# 开源组件库

这个仓库用于整理 GitHub 上可复用的开源模块。目标不是把所有源码搬进来，而是把“开发一个项目时需要哪些组件、每类组件有哪些可靠选择、怎么组合它们”整理成可维护的索引。

## 这个仓库解决什么问题

做新项目时，真正难的通常不是“选哪个框架”，而是这些模块能不能拼起来：

- 登录与权限
- 前端界面
- 移动端应用
- 组件工作台与设计系统文档
- 内部工具与低代码后台
- 表单与数据校验
- 国际化与本地化
- 翻译管理与本地化平台
- 后端 API
- API 文档与接口契约
- API 客户端与 SDK 生成
- API 网关与反向代理
- 边缘交付与 CDN / WAF
- 服务网格与集群网络
- 代码托管与版本协作
- 工程化与多包仓库
- 包与制品仓库
- 项目脚手架与模板生成
- 数据库与 ORM
- 数据库迁移与 Schema 版本管理
- 数据管道与数据集成
- 数据导入导出与表格文件
- 流处理与实时计算
- 数据仓库与 OLAP
- 数据质量与校验
- 数据治理与元数据
- 数据标注与人工审核
- 备份与恢复
- 向量数据库与检索
- 模型服务与推理网关
- LLM 护栏与结构化输出
- LLM 可观测性与评估
- AI / RAG / Agent
- 工作流与任务编排
- 内容管理与编辑
- 文档站与开发者门户
- 富文本与编辑器
- 文档协作与知识库
- 产品分析与转化
- 报表与商业智能
- 图表与数据可视化
- 地图与地理位置
- 实时通信与协作
- 音视频通话与会议
- 后台任务与作业队列
- 功能开关与实验发布
- 配置与密钥管理
- 授权与权限策略
- 数字身份与可验证凭证
- 审计日志与活动记录
- 隐私合规与同意管理
- 反滥用与验证码
- 文档处理与文件预览
- OCR 与文档识别
- 文档生成与模板输出
- 电子签名与合同签署
- 媒体处理与图片视频转码
- 通知触达
- 通信渠道与短信语音
- Webhook 与外部事件投递
- 状态页与事故沟通
- 评论与社区互动
- 论坛与社区平台
- 用户反馈与调研
- 客户支持与工单
- CRM 与销售管理
- 营销自动化与活动运营
- 电商与订单
- 项目管理与任务协作
- 日程预约与日历
- 支付与结账
- 账单与发票
- 财务会计与费用管理
- 基础设施即代码
- 容器与镜像构建
- 部署与托管
- CI/CD 与发布流水线
- 测试与质量
- 性能与负载测试
- 无障碍与可访问性测试
- 安全扫描
- SBOM 与许可证合规
- 错误跟踪与异常上报
- 日志管理与分析
- 监控与可观测性

本仓库把这些选择拆成明确的模块，并记录每个组件适合什么、不适合什么、接入成本和替代方案。

## 目录

| 分类 | 文件 | 用途 |
| --- | --- | --- |
| 前端 | [catalog/frontend.md](catalog/frontend.md) | UI 系统、管理后台、组件库、前端框架 |
| 移动端 | [catalog/mobile.md](catalog/mobile.md) | 跨平台 App、移动 UI、移动端构建工具链 |
| 组件工作台 | [catalog/component-workbench.md](catalog/component-workbench.md) | UI 组件预览、Story、设计系统文档、视觉回归 |
| 内部工具 | [catalog/internal-tools.md](catalog/internal-tools.md) | 低代码后台、运营控制台、CRUD 工具、数据源连接 |
| 表单与校验 | [catalog/forms.md](catalog/forms.md) | 表单状态、字段校验、Schema 建模、复杂表单流程 |
| 国际化 | [catalog/i18n.md](catalog/i18n.md) | 多语言文案、翻译资源、日期数字格式、复数规则 |
| 翻译管理 | [catalog/translation-management.md](catalog/translation-management.md) | 译文协作、审核、术语表、翻译记忆、资源同步 |
| 后端 | [catalog/backend.md](catalog/backend.md) | API 框架、服务框架、后端基础设施 |
| API 文档 | [catalog/api-docs.md](catalog/api-docs.md) | OpenAPI 文档、接口调试、契约协作、开发者门户 |
| API 客户端生成 | [catalog/api-client-generation.md](catalog/api-client-generation.md) | OpenAPI 客户端、类型、SDK、Hooks、Mock 生成 |
| API 网关 | [catalog/api-gateway.md](catalog/api-gateway.md) | 入口流量路由、TLS、限流、鉴权插件、反向代理 |
| 边缘交付 | [catalog/edge-delivery.md](catalog/edge-delivery.md) | CDN 缓存、可编程边缘网关、源站保护、WAF 规则执行 |
| 服务网格 | [catalog/service-mesh.md](catalog/service-mesh.md) | 服务间 mTLS、流量治理、网络策略、eBPF 可观测性 |
| 代码托管 | [catalog/code-hosting.md](catalog/code-hosting.md) | Git 仓库、代码评审、Pull/Merge Request、分支保护、团队协作 |
| 工程化 | [catalog/dev-tooling.md](catalog/dev-tooling.md) | Monorepo、包管理、构建缓存、任务编排、CI 加速 |
| 包与制品仓库 | [catalog/package-artifact-registry.md](catalog/package-artifact-registry.md) | 私有包仓库、依赖代理、Maven/npm/NuGet/PyPI、二进制制品治理 |
| 项目脚手架 | [catalog/scaffolding-templates.md](catalog/scaffolding-templates.md) | 项目模板、脚手架、代码片段生成、模板升级 |
| 认证 | [catalog/auth.md](catalog/auth.md) | 登录、身份、OAuth、用户管理、权限控制 |
| 数字身份 | [catalog/digital-identity.md](catalog/digital-identity.md) | DID、可验证凭证、Issuer、Verifier、钱包、OpenID4VC |
| 数据库 | [catalog/database.md](catalog/database.md) | 关系型数据库、ORM、后端即服务、事务数据 |
| 数据库迁移 | [catalog/database-migrations.md](catalog/database-migrations.md) | Schema 版本管理、SQL 迁移、数据库变更审计 |
| 数据管道 | [catalog/data-pipeline.md](catalog/data-pipeline.md) | ELT、ETL、数据源连接器、批量同步、数据仓库装载 |
| 数据导入导出 | [catalog/data-import-export.md](catalog/data-import-export.md) | CSV、Excel、字段映射、批量导入、报表导出 |
| 流处理 | [catalog/stream-processing.md](catalog/stream-processing.md) | 持续事件流计算、窗口聚合、状态处理、实时转换 |
| 数据仓库 | [catalog/data-warehouse.md](catalog/data-warehouse.md) | OLAP、列式数据库、湖仓查询、嵌入式分析引擎 |
| 数据质量 | [catalog/data-quality.md](catalog/data-quality.md) | 数据断言、规则校验、异常检测、质量报告 |
| 数据治理 | [catalog/data-governance.md](catalog/data-governance.md) | 数据资产目录、元数据采集、数据血缘、治理入口 |
| 数据标注与人工审核 | [catalog/data-labeling-review.md](catalog/data-labeling-review.md) | 训练数据标注、人工复核、视觉标注、文本分类、质检流程 |
| 备份与恢复 | [catalog/backup-recovery.md](catalog/backup-recovery.md) | 文件备份、数据库备份、Kubernetes 灾备、恢复演练 |
| 向量数据库 | [catalog/vector-database.md](catalog/vector-database.md) | Embedding 存储、RAG 检索、相似度搜索、混合检索 |
| 模型服务与推理网关 | [catalog/model-serving-inference.md](catalog/model-serving-inference.md) | 本地模型运行、推理服务、OpenAI 兼容 API、多供应商模型代理 |
| LLM 护栏与结构化输出 | [catalog/llm-guardrails-structured-output.md](catalog/llm-guardrails-structured-output.md) | 输入输出策略、拒答规则、JSON/Schema 约束、结构化生成 |
| LLM 可观测性与评估 | [catalog/llm-observability-evaluation.md](catalog/llm-observability-evaluation.md) | Prompt 版本、模型调用追踪、数据集、RAG 评估、红队测试 |
| AI | [catalog/ai.md](catalog/ai.md) | LLM 应用、RAG、Agent、工作流、模型接入工具 |
| 内容管理 | [catalog/cms.md](catalog/cms.md) | Headless CMS、内容编辑、文档站、营销内容后台 |
| 文档站 | [catalog/documentation-site.md](catalog/documentation-site.md) | 产品文档、开发者门户、Markdown/MDX、版本化文档、静态站点 |
| 富文本编辑器 | [catalog/editors.md](catalog/editors.md) | 嵌入式编辑、结构化文档、协作编辑、内容编辑体验 |
| 文档协作 | [catalog/document-collaboration.md](catalog/document-collaboration.md) | 团队 Wiki、协作文档、空间权限、版本历史、知识库 |
| 支付 | [catalog/payment.md](catalog/payment.md) | 支付 SDK、支付网关、结账入口、收款通道 |
| 账单与发票 | [catalog/billing-invoicing.md](catalog/billing-invoicing.md) | 订阅账单、用量计费、发票生成、客户账务 |
| 财务会计 | [catalog/accounting-finance.md](catalog/accounting-finance.md) | 记账、预算、收支分类、费用追踪、财务报表 |
| 存储 | [catalog/storage.md](catalog/storage.md) | 对象存储、文件上传、媒体资源 |
| 文档处理 | [catalog/document-processing.md](catalog/document-processing.md) | PDF 预览、Office 解析、文本抽取、文件内容入库 |
| OCR 与文档识别 | [catalog/ocr-document-understanding.md](catalog/ocr-document-understanding.md) | 扫描件文字识别、PDF 文本层、版面分析、表格识别 |
| 文档生成 | [catalog/document-generation.md](catalog/document-generation.md) | PDF、DOCX、PPTX、合同、报价单、报表、模板填充 |
| 电子签名 | [catalog/electronic-signature.md](catalog/electronic-signature.md) | PDF 合同签署、签署流程、模板、完成证书、审计轨迹 |
| 媒体处理 | [catalog/media-processing.md](catalog/media-processing.md) | 图片缩放、格式转换、音视频转码、缩略图生成 |
| 邮件通知 | [catalog/email.md](catalog/email.md) | 邮件发送、事务邮件、Newsletter、营销邮件 |
| 通知触达 | [catalog/notifications.md](catalog/notifications.md) | 多渠道通知、站内信、Push、团队告警 |
| 通信渠道与短信语音 | [catalog/communications-api.md](catalog/communications-api.md) | 短信网关、批量短信、可编程语音、电话网络接入 |
| Webhook | [catalog/webhooks.md](catalog/webhooks.md) | 产品事件发布、客户订阅端点、签名、重试、事件重放 |
| 状态页 | [catalog/status-pages.md](catalog/status-pages.md) | 公开服务状态、事故记录、维护窗口、订阅沟通 |
| 评论互动 | [catalog/comments-community.md](catalog/comments-community.md) | 网站评论、嵌入式讨论、审核、反垃圾、社区身份 |
| 论坛社区 | [catalog/forums-community.md](catalog/forums-community.md) | 论坛、话题分类、版主管理、社区治理、长期讨论 |
| 用户反馈 | [catalog/user-feedback-research.md](catalog/user-feedback-research.md) | 产品内反馈、问卷、NPS、功能建议、用户研究 |
| 客户支持 | [catalog/customer-support.md](catalog/customer-support.md) | 在线客服、共享收件箱、工单系统、帮助台 |
| CRM | [catalog/crm.md](catalog/crm.md) | 客户资料、联系人、线索、商机、销售管线 |
| 营销自动化 | [catalog/marketing-automation.md](catalog/marketing-automation.md) | 用户分群、活动编排、线索培育、营销旅程 |
| 电商 | [catalog/ecommerce.md](catalog/ecommerce.md) | 商品目录、购物车、订单、库存、促销、履约 |
| 项目管理 | [catalog/project-management.md](catalog/project-management.md) | Issue、看板、路线图、Sprint、任务协作 |
| 日程预约 | [catalog/scheduling-calendar.md](catalog/scheduling-calendar.md) | 预约链接、可用时间、会议投票、日历视图、时区处理 |
| 搜索 | [catalog/search.md](catalog/search.md) | 全文搜索、站内搜索、语义搜索、搜索基础设施 |
| 缓存 | [catalog/cache.md](catalog/cache.md) | 内存缓存、会话、低延迟数据结构 |
| 消息队列 | [catalog/messaging.md](catalog/messaging.md) | 异步任务、发布订阅、事件流 |
| 后台任务 | [catalog/background-jobs.md](catalog/background-jobs.md) | Worker、任务队列、重试、延迟任务、短周期作业 |
| 实时通信 | [catalog/realtime.md](catalog/realtime.md) | WebSocket、实时推送、多人协作、在线状态 |
| 音视频通话 | [catalog/video-conferencing.md](catalog/video-conferencing.md) | WebRTC、视频会议、SFU、屏幕共享、实时媒体传输 |
| 工作流 | [catalog/workflow.md](catalog/workflow.md) | 任务编排、调度、定时任务、长事务流程 |
| 产品分析 | [catalog/analytics.md](catalog/analytics.md) | 用户行为、网站统计、事件采集、转化漏斗 |
| 商业智能 | [catalog/business-intelligence.md](catalog/business-intelligence.md) | BI 平台、SQL 查询、仪表盘、数据探索、定时报表 |
| 图表与可视化 | [catalog/visualization.md](catalog/visualization.md) | 业务仪表盘、运营报表、交互式图表、数据探索 |
| 地图与地理位置 | [catalog/maps.md](catalog/maps.md) | 交互式地图、瓦片渲染、空间数据、Web GIS |
| 功能开关 | [catalog/feature-flags.md](catalog/feature-flags.md) | 灰度发布、实验平台、远程配置、渐进式交付 |
| 配置与密钥管理 | [catalog/secrets-management.md](catalog/secrets-management.md) | 环境变量、密钥托管、加密入库、运行时注入 |
| 授权策略 | [catalog/authorization.md](catalog/authorization.md) | RBAC、ABAC、ReBAC、策略即代码、资源关系权限 |
| 审计日志 | [catalog/audit-logs.md](catalog/audit-logs.md) | 用户操作留痕、资源变更历史、客户可见审计轨迹 |
| 隐私合规 | [catalog/privacy-compliance.md](catalog/privacy-compliance.md) | Cookie 同意、隐私偏好、数据主体请求、数据地图 |
| 反滥用 | [catalog/anti-abuse.md](catalog/anti-abuse.md) | CAPTCHA、人机验证、登录防爆破、表单防刷、应用限流 |
| 基础设施即代码 | [catalog/infrastructure-as-code.md](catalog/infrastructure-as-code.md) | 云资源声明、环境编排、配置管理、状态管理 |
| 容器与镜像构建 | [catalog/containers.md](catalog/containers.md) | 本地容器运行、OCI 镜像构建、镜像仓库、制品治理 |
| 部署 | [catalog/deployment.md](catalog/deployment.md) | 自托管、PaaS、应用部署、基础设施胶水 |
| CI/CD | [catalog/ci-cd.md](catalog/ci-cd.md) | 持续集成、持续交付、构建流水线、发布门禁 |
| 测试与质量 | [catalog/testing.md](catalog/testing.md) | 单元测试、端到端测试、集成测试、自动化回归 |
| 性能与负载测试 | [catalog/performance-load-testing.md](catalog/performance-load-testing.md) | 接口压测、并发容量、延迟阈值、分布式负载、发布性能门禁 |
| 无障碍与可访问性测试 | [catalog/accessibility-testing.md](catalog/accessibility-testing.md) | WCAG 扫描、ARIA 检查、页面审计、CI 可访问性报告 |
| 安全扫描 | [catalog/security.md](catalog/security.md) | 依赖漏洞、密钥泄露、Web DAST、容器与 IaC 扫描 |
| SBOM 与许可证合规 | [catalog/sbom-license-compliance.md](catalog/sbom-license-compliance.md) | 软件物料清单、许可证识别、版权扫描、合规报告 |
| 错误跟踪 | [catalog/error-tracking.md](catalog/error-tracking.md) | 应用异常、崩溃报告、堆栈聚合、发布版本、会话回放 |
| 日志管理 | [catalog/log-management.md](catalog/log-management.md) | 日志采集、聚合查询、解析转换、保留策略、日志管道 |
| 监控 | [catalog/observability.md](catalog/observability.md) | 指标、仪表盘、链路追踪、遥测管线、告警基础 |

## 项目组合蓝图

这些蓝图可以作为新项目选型的起点：

- [SaaS 起步项目](stacks/saas-starter.md)：认证、前端、后端、数据库、支付、账单与发票、部署、监控。
- [AI RAG 应用](stacks/ai-rag-app.md)：前端、API、LLM 编排、模型服务、LLM 护栏、LLM 评估、向量数据库与检索、部署、监控。
- [内部管理后台](stacks/internal-admin.md)：管理 UI、后端、身份、数据库、部署。

## 组件条目格式

新增组件时使用下面的格式。字段名保持统一，便于后续脚本校验和生成机器可读索引。

```md
## 组件名称

- GitHub: https://github.com/org/repo
- 官网: https://example.com
- 模块: 认证 / 数据库 / 后端
- 技术栈: TypeScript, PostgreSQL
- 许可证: Apache-2.0
- 适合: 这个组件最适合的项目场景。
- 不适合: 使用这个组件成本过高或风险过大的场景。
- 接入成本: 低 / 中 / 高
- 替代方案: 组件 A, 组件 B
- 评分: 4/5
- 备注: 实际选型时需要注意的判断。
```

不要手写 star 数这类容易过期的字段，除非后续有自动化脚本维护。维护状态应该在新增或提升组件时人工复核。

## 如何拼装一个项目

1. 先列出项目需要的能力：认证、授权策略、数字身份与可验证凭证、审计日志、UI、移动端、组件工作台与设计系统文档、内部工具、表单与校验、国际化、翻译管理与本地化平台、后端 API、API 文档、API 客户端与 SDK 生成、API 网关、边缘交付、服务网格、代码托管与版本协作、工程化、包与制品仓库、项目脚手架与模板生成、数据库、数据库迁移、数据管道、数据导入导出、流处理、数据仓库、数据质量、数据治理、数据标注与人工审核、备份恢复、向量数据库与检索、模型服务与推理网关、LLM 护栏与结构化输出、LLM 可观测性与评估、文件存储、文档处理、OCR 与文档识别、文档生成与模板输出、电子签名、媒体处理、邮件通知、通知触达、通信渠道与短信语音、Webhook 投递、状态页、评论互动、论坛社区、用户反馈、客户支持、CRM、营销自动化、电商、项目管理、日程预约、AI、内容管理、文档站与开发者门户、富文本编辑、文档协作、搜索、缓存、消息队列、后台任务、工作流、实时通信、音视频通话、产品分析、商业智能、图表可视化、地图地理、功能开关、配置密钥、隐私合规、反滥用、支付、账单与发票、财务会计、基础设施即代码、容器镜像、部署、CI/CD、测试、性能与负载测试、无障碍与可访问性测试、安全扫描、SBOM 许可证合规、错误跟踪、日志管理、监控。
2. 打开对应的 `catalog/` 分类文件。
3. 每个能力选择 1 个主组件和 1 个备选组件。
4. 在确定技术栈前检查许可证、接入成本、托管方式和数据边界。
5. 把最终组合写进项目 README 或架构说明。

完整流程见 [docs/project-assembly-guide.md](docs/project-assembly-guide.md)。

新增组件时可以从 [templates/component-entry.md](templates/component-entry.md) 复制模板。

开始新项目选型时，可以复制 [templates/project-assembly-worksheet.md](templates/project-assembly-worksheet.md) 作为项目技术栈工作表，也可以直接生成一份已经填入候选组件的草案。

推荐落地顺序：

```powershell
python tools/generate_worksheet.py --list-presets
python tools/generate_worksheet.py --project-name "SaaS 示例" --preset saas-starter --output stack-selection.md
python tools/check_stack.py --components FastAPI,PostgreSQL,Grafana
```

`generate_worksheet.py` 会按评分和接入成本选择主组件与备选组件，并生成能力地图、许可证检查和优先验证项。优先验证项会把许可证、接入成本或缺失组件风险更高的集成排在前面。脚本输出只是第一版草案，最终仍要按业务约束人工确认。

发布到 GitHub 前，按 [docs/github-publish-guide.md](docs/github-publish-guide.md) 检查远程仓库、推送和 Actions 设置；仓库描述和 topics 可参考 [docs/repository-profile.md](docs/repository-profile.md)。

## 校验目录

新增或修改组件后，运行：

```powershell
python tools/validate_catalog.py --write-index
```

这个命令会检查 `catalog/*.md` 的必填字段、GitHub 地址、接入成本和评分格式，并更新 [catalog/index.json](catalog/index.json)。

## 查看分类概览

可以先生成分类概览，快速确认每个模块下已经收录了多少组件：

```powershell
python tools/summarize_catalog.py
```

输出会列出分类、组件数量、该分类的最高评分组件和最低接入成本，适合在开始拼装项目前先确认候选范围。

## 搜索组件

可以用命令行按分类、接入成本和关键词筛选组件：

```powershell
python tools/search_catalog.py --category ai --cost 中
python tools/search_catalog.py --keyword PostgreSQL
```

输出是 Markdown 表格，可以直接复制到项目选型工作表或技术栈决策文档里。

## 生成技术栈草案

确定项目需要哪些模块后，可以用组合生成器输出一份初始决策表：

```powershell
python tools/assemble_stack.py --list-presets
python tools/assemble_stack.py --preset saas-starter
python tools/assemble_stack.py --modules frontend,backend,auth,database,deployment,observability
python tools/assemble_stack.py --modules 后端,认证,数据库
```

模块名称可以使用 `catalog/` 目录中的英文分类名，也可以使用常用中文别名，例如 `后端,认证,数据库`。`--preset` 适合快速套用常见项目蓝图，`--modules` 适合自定义能力清单。生成结果会按评分和接入成本选择主组件与备选组件，并直接带出主组件许可证和接入成本，适合作为项目工作表的第一版草案，再由人工检查托管方式和业务边界。

如果希望直接生成完整工作表，可以运行：

```powershell
python tools/generate_worksheet.py --list-presets
python tools/generate_worksheet.py --project-name "SaaS 示例" --preset saas-starter --output stack-selection.md
python tools/generate_worksheet.py --project-name "中文模块示例" --modules 后端,认证,数据库 --output stack-selection.md
```

`--list-presets` 会列出每个预设的中文项目类型、适用场景和目录模块。内置预设包括 `saas-starter`、`ai-rag-app` 和 `internal-admin`；如果项目不符合这些蓝图，仍然可以用 `--modules` 自行传入分类列表或常用中文模块名。

## 检查技术栈风险

确定候选组件后，可以按组件名生成拼装前的风险检查表：

```powershell
python tools/check_stack.py --components FastAPI,PostgreSQL,Grafana
```

这个命令会标出目录中记录的许可证风险、接入成本和缺失组件，适合放进技术栈决策文档作为上线前的人工复核清单。

## 许可证

本仓库使用 [MIT License](LICENSE)。组件条目中记录的是上游项目各自的许可证；使用这些组件时，仍需要按上游仓库的许可证要求处理。

## 维护原则

- 优先收录成熟、文档完整、许可证清楚的开源项目。
- 优先收录可以独立接入的模块。
- 记录取舍，不只记录优点。
- 条目要短，便于快速扫描。
- 只有当某个组件在真实项目中验证过，再把可运行示例放进 `components/`。
