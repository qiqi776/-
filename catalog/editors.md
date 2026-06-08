# 富文本与编辑器组件

富文本与编辑器组件覆盖嵌入式内容编辑、协作编辑、结构化文档、Markdown/Rich Text 转换和可扩展编辑体验。

## Tiptap

- GitHub: https://github.com/ueberdosis/tiptap
- 官网: https://tiptap.dev
- 模块: 编辑器 / ProseMirror 富文本
- 技术栈: TypeScript, ProseMirror, React, Vue
- 许可证: MIT
- 适合: 需要高度可扩展富文本、结构化文档、协作编辑和 React/Vue 集成的产品。
- 不适合: 只需要非常简单的 textarea，或团队不想理解 ProseMirror 文档模型。
- 接入成本: 中
- 替代方案: Lexical, Slate, ProseMirror
- 评分: 4/5
- 备注: 扩展能力强，适合知识库、CMS、AI 内容编辑和复杂后台编辑场景。

## Lexical

- GitHub: https://github.com/facebook/lexical
- 官网: https://lexical.dev
- 模块: 编辑器 / React 富文本
- 技术栈: TypeScript, React
- 许可证: MIT
- 适合: React 项目需要现代化、可组合、性能较好的富文本编辑器核心。
- 不适合: 非 React 栈项目，或需要开箱即用的完整编辑器 UI 而不想自行组装插件。
- 接入成本: 中
- 替代方案: Tiptap, Slate, Draft.js
- 评分: 4/5
- 备注: 核心设计清晰，但生产级体验通常需要自行组合工具栏、序列化、粘贴处理和插件。

## Slate

- GitHub: https://github.com/ianstormtaylor/slate
- 官网: https://docs.slatejs.org
- 模块: 编辑器 / 自定义文档编辑
- 技术栈: TypeScript, React
- 许可证: MIT
- 适合: 需要完全自定义文档结构、嵌套块、内联节点和复杂编辑交互的 React 项目。
- 不适合: 希望快速接入标准富文本编辑器，或团队没有时间维护编辑器边界情况。
- 接入成本: 高
- 替代方案: Tiptap, Lexical, ProseMirror
- 评分: 3/5
- 备注: 灵活度高但工程成本也高，适合编辑器本身是核心能力的项目。
