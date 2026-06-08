# 可运行组件示例

这个目录用于保存未来的可运行模板、集成示例和可复用胶水代码。

当前仓库先从文档索引开始，不急着收集代码。只有满足下面条件时，才把代码放进这里：

- 对应 catalog 条目已经在真实项目或验证项目中使用过。
- 示例足够小，能够长期维护。
- README 写清楚前置条件和启动命令。
- 示例不是简单复制上游项目。

建议的未来结构：

```text
components/
  auth/
    supabase-auth-nextjs/
    keycloak-node-api/
  ai/
    rag-fastapi-qdrant/
    langchain-agent-template/
  deployment/
    coolify-docker-app/
```

