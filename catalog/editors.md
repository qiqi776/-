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
- 替代方案: Lexical, ProseMirror, Slate
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
- 替代方案: Tiptap, ProseMirror, Slate
- 评分: 4/5
- 备注: 核心设计清晰，但生产级体验通常需要自行组合工具栏、序列化、粘贴处理和插件。

## ProseMirror

- GitHub: https://github.com/ProseMirror/prosemirror
- 官网: https://prosemirror.net
- 模块: 编辑器 / 富文本核心 / 文档模型
- 技术栈: TypeScript, JavaScript, contentEditable
- 许可证: MIT
- 适合: 团队需要成熟的富文本底层框架、自定义文档 schema、事务模型、插件系统、粘贴解析和协作编辑基础能力。
- 不适合: 希望直接获得完整编辑器 UI，或团队不想维护底层编辑器抽象、命令、选择区和序列化边界。
- 接入成本: 高
- 替代方案: Tiptap, Lexical, Slate
- 评分: 4/5
- 备注: 生态成熟且被多个上层编辑器采用；生产前要确认 schema 设计、历史记录、协作协议、输入法、粘贴清洗和测试用例。
