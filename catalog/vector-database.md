# 向量数据库与检索组件

向量数据库与检索组件覆盖 embedding 向量存储、近似最近邻搜索、混合检索、RAG 知识库、相似度过滤、索引构建、集合分片和检索质量调优。它解决“语义向量如何被存储、查询、过滤和扩展”的问题；通用关系型数据库和 ORM 放在数据库分类，LLM/RAG 编排框架放在 AI 分类，关键词全文搜索放在搜索分类，文档抽取与入库前处理放在文档处理和 OCR 分类。

## Qdrant

- GitHub: https://github.com/qdrant/qdrant
- 官网: https://qdrant.tech
- 模块: 向量数据库 / RAG 检索 / 相似度搜索
- 技术栈: Rust, HNSW, REST, gRPC, Docker
- 许可证: Apache-2.0
- 适合: RAG、语义搜索、推荐、相似图片或文本检索，以及需要自托管独立向量数据库和 payload 过滤的 AI 应用。
- 不适合: 只需要关键词搜索，或现有 PostgreSQL + pgvector 扩展已经能满足数据规模和运维边界。
- 接入成本: 中
- 替代方案: Milvus, pgvector, Weaviate, Chroma
- 评分: 4/5
- 备注: 自托管向量搜索的强候选；落地前要验证 embedding 维度、payload schema、过滤条件、集合分片、备份恢复和检索质量评估集。

## Milvus

- GitHub: https://github.com/milvus-io/milvus
- 官网: https://milvus.io
- 模块: 向量数据库 / 大规模检索 / 分布式索引
- 技术栈: Go, C++, Kubernetes, etcd, MinIO, Pulsar
- 许可证: Apache-2.0
- 适合: 需要大规模向量集合、分布式部署、多索引类型、云原生扩展和高吞吐检索的平台团队。
- 不适合: 小型 RAG 应用、单机知识库，或团队不想维护多组件分布式存储和集群依赖。
- 接入成本: 高
- 替代方案: Qdrant, Weaviate, pgvector
- 评分: 4/5
- 备注: 能力强但基础设施成本高；生产前要确认部署拓扑、资源配额、索引构建时间、数据一致性、备份恢复和运维告警。

## pgvector

- GitHub: https://github.com/pgvector/pgvector
- 官网: https://github.com/pgvector/pgvector
- 模块: 向量数据库 / PostgreSQL 扩展 / 混合检索
- 技术栈: C, PostgreSQL, SQL, HNSW, IVFFlat
- 许可证: PostgreSQL License
- 适合: 已经使用 PostgreSQL，希望把元数据、权限过滤、事务数据和中小规模向量检索放在同一个数据库里的团队。
- 不适合: 需要超大规模独立向量集群、独立扩缩容、复杂多租户向量服务或非常高吞吐相似度检索的项目。
- 接入成本: 低
- 替代方案: Qdrant, Milvus, Weaviate
- 评分: 4/5
- 备注: 适合降低 RAG 起步运维成本；要验证索引类型、召回率、VACUUM/ANALYZE、查询计划、维度变化和数据库整体负载。
