# 表单与校验组件

表单与校验组件覆盖表单状态管理、字段校验、Schema 建模和复杂表单流程。

## React Hook Form

- GitHub: https://github.com/react-hook-form/react-hook-form
- 官网: https://react-hook-form.com
- 模块: 表单 / React 表单状态
- 技术栈: TypeScript, React
- 许可证: MIT
- 适合: React 项目需要高性能表单状态、字段注册、校验集成和复杂表单拆分。
- 不适合: 非 React 项目，或只需要极少量原生 HTML 表单且不希望引入表单抽象。
- 接入成本: 低
- 替代方案: Formik, Final Form, TanStack Form
- 评分: 4/5
- 备注: 常和 Zod、Yup、Valibot 等 Schema 校验库配合，适合把表单状态和数据结构校验解耦。

## Zod

- GitHub: https://github.com/colinhacks/zod
- 官网: https://zod.dev
- 模块: 表单 / Schema 校验 / 类型推导
- 技术栈: TypeScript
- 许可证: MIT
- 适合: TypeScript 项目需要运行时数据校验、接口入参校验、表单校验和类型推导保持一致。
- 不适合: 项目不是 TypeScript 栈，或需要极致低开销且校验规则非常简单。
- 接入成本: 低
- 替代方案: Valibot, Yup, Joi
- 评分: 4/5
- 备注: 适合放在前后端共享包中，但要避免把所有业务规则都堆进单个巨大 Schema。

## FormKit

- GitHub: https://github.com/formkit/formkit
- 官网: https://formkit.com
- 模块: 表单 / Vue 表单框架
- 技术栈: TypeScript, Vue
- 许可证: MIT
- 适合: Vue 项目需要统一处理字段组件、表单校验、Schema 渲染、多步骤表单和表单主题。
- 不适合: React 或 Svelte 项目，或团队只需要轻量字段校验而不需要完整表单框架。
- 接入成本: 中
- 替代方案: VeeValidate, VueUse Form, 原生表单组件
- 评分: 4/5
- 备注: 能减少 Vue 复杂表单的重复代码，但需要团队接受它的表单建模方式。
