# 模型服务与推理网关组件

模型服务与推理网关组件覆盖本地模型运行、GPU/CPU 推理服务、OpenAI 兼容 API、多供应商模型代理、路由、限流、成本控制、缓存、观测和推理部署。它解决“模型请求如何被托管、转发、加速、治理和接入应用”的问题；LLM/RAG 编排、Agent 和工作流放在 AI 分类，Prompt 版本、模型调用追踪、评估数据集和红队测试放在 LLM 可观测性与评估分类，embedding 存储与向量检索放在向量数据库与检索分类，普通 API 框架放在后端分类，运行环境和发布放在部署分类。

## Ollama

- GitHub: https://github.com/ollama/ollama
- 官网: https://ollama.com
- 模块: 模型服务 / 本地模型运行 / OpenAI 兼容 API
- 技术栈: Go, llama.cpp, GGUF, Docker
- 许可证: MIT
- 适合: 团队需要在本机、开发环境或轻量服务器快速运行开源 LLM，验证提示词、RAG 原型和离线模型能力。
- 不适合: 需要大规模多副本推理、复杂 GPU 调度、企业级限流审计或生产级高吞吐模型网关的场景。
- 接入成本: 低
- 替代方案: vLLM, llama.cpp, LocalAI
- 评分: 4/5
- 备注: 适合原型和小规模自托管；上线前要确认模型许可证、显存/内存、上下文长度、并发能力、API 兼容性和模型文件分发方式。

## vLLM

- GitHub: https://github.com/vllm-project/vllm
- 官网: https://docs.vllm.ai
- 模块: 模型服务 / 高吞吐推理 / OpenAI 兼容服务
- 技术栈: Python, CUDA, PyTorch, PagedAttention, Kubernetes
- 许可证: Apache-2.0
- 适合: 平台团队需要高吞吐 GPU 推理、OpenAI 兼容接口、批处理调度和服务化部署开源大模型。
- 不适合: 没有 GPU 资源、只做本地原型，或团队无法维护 CUDA、模型权重、推理性能和版本兼容的项目。
- 接入成本: 高
- 替代方案: Ollama, Text Generation Inference, TensorRT-LLM
- 评分: 4/5
- 备注: 适合把推理作为平台能力；生产前要验证模型支持矩阵、显存占用、并发吞吐、延迟 P95、量化策略、滚动发布和安全隔离。

## LiteLLM

- GitHub: https://github.com/BerriAI/litellm
- 官网: https://www.litellm.ai
- 模块: 模型服务 / LLM 网关 / 多供应商代理
- 技术栈: Python, FastAPI, OpenAI API, Redis, PostgreSQL
- 许可证: MIT（enterprise 目录另行许可）
- 适合: 团队需要统一接入 OpenAI、Anthropic、Azure、本地模型等多供应商接口，并集中处理路由、预算、重试、日志和密钥治理。
- 不适合: 只调用一个模型供应商，或团队不想在应用和模型供应商之间维护额外网关、数据库和权限边界。
- 接入成本: 中
- 替代方案: Portkey, Helicone, OpenRouter, 自研模型代理
- 评分: 4/5
- 备注: 主体代码按 MIT 使用，enterprise 目录有单独许可边界；接入前要确认模型路由策略、密钥隔离、审计日志、成本限额、缓存和故障降级。
