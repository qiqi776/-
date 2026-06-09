# AI 组件

AI 组件覆盖 LLM 应用、RAG、Agent、工作流构建器和模型接入基础设施；模型托管、推理服务和多供应商模型网关放在模型服务与推理网关分类，embedding 存储、向量索引和相似度检索后端放在向量数据库与检索分类，输入输出策略、拒答规则和结构化响应放在 LLM 护栏与结构化输出分类，Prompt 版本、模型调用追踪、评估数据集和红队测试放在 LLM 可观测性与评估分类。

## LangChain

- GitHub: https://github.com/langchain-ai/langchain
- 官网: https://www.langchain.com
- 模块: AI / LLM 编排
- 技术栈: Python, TypeScript
- 许可证: MIT
- 适合: 原型和集成 LLM 链、工具、Agent、检索和模型供应商抽象。
- 不适合: 只需要很小的直接模型 API 封装，并希望尽量减少抽象层。
- 接入成本: 中
- 替代方案: LlamaIndex, Haystack, Semantic Kernel
- 评分: 4/5
- 备注: 生态有价值，但要控制抽象层不要失控。

## LlamaIndex

- GitHub: https://github.com/run-llama/llama_index
- 官网: https://www.llamaindex.ai
- 模块: AI / RAG / 数据框架
- 技术栈: Python, TypeScript
- 许可证: MIT
- 适合: 基于文档、数据库和外部数据构建检索增强生成应用。
- 不适合: 项目不需要检索，也不需要数据连接器。
- 接入成本: 中
- 替代方案: LangChain, Haystack, Semantic Kernel
- 评分: 4/5
- 备注: 当核心难点是把私有数据接入 LLM 工作流时很合适。

## Haystack

- GitHub: https://github.com/deepset-ai/haystack
- 官网: https://haystack.deepset.ai
- 模块: AI / RAG / LLM 管线
- 技术栈: Python
- 许可证: Apache-2.0
- 适合: Python 团队需要构建生产级 RAG、检索、重排、生成、评估和可测试的 LLM 数据管线。
- 不适合: 只想用可视化拖拽快速搭建 Demo，或团队主要技术栈不是 Python。
- 接入成本: 中
- 替代方案: LangChain, LlamaIndex, Semantic Kernel
- 评分: 4/5
- 备注: 更适合把 RAG 作为工程管线治理；生产前要确认连接器、评估集、提示词版本、向量库和监控接入。
