# 贡献指南

这个仓库是精选组件目录。贡献的目标是提高选型质量，而不是单纯增加链接数量。

## 新增组件

1. 选择正确的 `catalog/*.md` 文件。
2. 从 [templates/component-entry.md](templates/component-entry.md) 复制条目格式。
3. 填写所有必填字段。
4. 同时说明“适合”和“不适合”的场景。
5. 检查许可证并清楚记录。
6. 补充替代方案，方便读者横向比较。

## 新增项目组合蓝图

当一组组件反复适合某类项目时，可以在 `stacks/` 下新增组合蓝图。

有用的蓝图应该包含：

- 能力地图
- 主组件
- 备选组件
- 选择主组件的理由
- 主要风险
- 推荐优先验证的集成
- 适合和不适合的项目类型

## 更新项目工作表

如果新增了重要组件分类，也要检查 [templates/project-assembly-worksheet.md](templates/project-assembly-worksheet.md)，确认新分类能出现在项目选型流程里。

## Review 标准

提交前检查：

- GitHub 链接没有失效。
- 许可证字段明确。
- 条目不只说“项目很好”，还说明边界和取舍。
- 没有手写 star 数这类容易过期的指标。
- 没有重复组件，除非明确说明差异。

## 本地校验

提交前运行：

```powershell
python tools/validate_catalog.py --write-index
python -m unittest tests.test_validate_catalog -v
python -m unittest tests.test_search_catalog -v
```

第一条命令校验组件目录并更新 `catalog/index.json`，后两条命令验证校验脚本和搜索脚本。

## 写作风格

- 条目要短，服务于选型决策。
- 优先写具体取舍。
- 避免营销式表达。
- 文档和目录条目默认使用中文。
