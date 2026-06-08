# AI 组件

AI 组件覆盖 LLM 应用、RAG、Agent、工作流构建器和模型接入基础设施；模型托管、推理服务和多供应商模型网关放在模型服务与推理网关分类，embedding 存储、向量索引和相似度检索后端放在向量数据库与检索分类，Prompt 版本、模型调用追踪、评估数据集和红队测试放在 LLM 可观测性与评估分类。

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
- 替代方案: LangChain, Haystack, 自研 RAG 管线
- 评分: 4/5
- 备注: 当核心难点是把私有数据接入 LLM 工作流时很合适。

## Flowise

- GitHub: https://github.com/FlowiseAI/Flowise
- 官网: https://flowiseai.com
- 模块: AI / 工作流构建器
- 技术栈: TypeScript, Node.js
- 许可证: Apache-2.0
- 适合: 可视化 LLM 工作流、快速 Demo、内部 AI 自动化和低代码实验。
- 不适合: 需要严格代码级控制、严肃评审流程或复杂生产工程实践的项目。
- 接入成本: 中
- 替代方案: Dify, Langflow, n8n AI 节点
- 评分: 3/5
- 备注: 适合探索；生产使用需要治理和部署评审。
