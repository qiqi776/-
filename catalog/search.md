# 搜索组件

搜索组件覆盖全文搜索、站内搜索、语义搜索和搜索基础设施；应用日志采集、聚合查询、解析转换和保留策略放在日志管理与分析分类。

## Meilisearch

- GitHub: https://github.com/meilisearch/meilisearch
- 官网: https://www.meilisearch.com
- 模块: 搜索 / 全文搜索
- 技术栈: Rust
- 许可证: MIT（社区版）/ 商业许可证或 BUSL-1.1（企业版）
- 适合: 需要快速接入站内搜索、文档搜索、商品搜索和良好默认排序体验的项目。
- 不适合: 需要企业版特性但不想接受商业许可证，或需要极复杂搜索分析、日志分析和大规模 Elastic 生态能力。
- 接入成本: 低
- 替代方案: Typesense, OpenSearch, Elasticsearch
- 评分: 4/5
- 备注: 社区版是 MIT；分片和 S3 streaming snapshots 等企业能力受企业许可或 BUSL-1.1 约束。

## Typesense

- GitHub: https://github.com/typesense/typesense
- 官网: https://typesense.org
- 模块: 搜索 / 全文搜索
- 技术栈: C++
- 许可证: GPL-3.0
- 适合: 需要 typo-tolerant 搜索、低延迟搜索 API 和相对简单运维的项目。
- 不适合: 团队不能接受 GPL 许可证，或需要完整 Elastic 生态。
- 接入成本: 中
- 替代方案: Meilisearch, OpenSearch, Elasticsearch
- 评分: 4/5
- 备注: 许可证需要结合使用方式审查。

## OpenSearch

- GitHub: https://github.com/opensearch-project/OpenSearch
- 官网: https://opensearch.org
- 模块: 搜索 / 分析 / 日志
- 技术栈: Java
- 许可证: Apache-2.0
- 适合: 需要全文搜索、日志分析、聚合查询和较完整搜索平台能力的项目。
- 不适合: 小项目只需要简单站内搜索，或团队不想承担集群运维。
- 接入成本: 高
- 替代方案: Elasticsearch, Meilisearch, Typesense
- 评分: 4/5
- 备注: 能力强，但引入后会成为重要基础设施。
