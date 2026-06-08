# 数据标注与人工审核组件

数据标注与人工审核组件覆盖训练数据标注、文本分类、实体抽取、图片/视频标注、OCR 结果复核、人工质检、审核队列和标注质量管理。它解决“AI、搜索、OCR、内容审核等项目如何把人工判断沉淀成可追踪数据”的问题；LLM 编排放在 AI 分类，用户调研放在用户反馈分类，客服会话和工单放在客户支持分类。

## Label Studio

- GitHub: https://github.com/HumanSignal/label-studio
- 官网: https://labelstud.io
- 模块: 数据标注 / 多模态标注 / 人工审核
- 技术栈: Python, Django, JavaScript, React, Redis, PostgreSQL
- 许可证: Apache-2.0
- 适合: AI 项目需要统一标注文本、图片、音频、视频、时间序列、LLM 输出和人工审核任务，并希望自定义标注界面和工作流。
- 不适合: 只需要极简文本分类标注，或项目不想维护独立 Web 服务、队列和权限体系。
- 接入成本: 中
- 替代方案: CVAT, doccano, Prodigy
- 评分: 4/5
- 备注: 适合多模态和复杂审核流程；落地时要确认项目模板、标注员权限、任务分配、质检抽样、数据导入导出和隐私隔离。

## CVAT

- GitHub: https://github.com/cvat-ai/cvat
- 官网: https://www.cvat.ai
- 模块: 数据标注 / 计算机视觉 / 图片视频标注
- 技术栈: Python, Django, TypeScript, React, PostgreSQL, Redis, Docker
- 许可证: MIT
- 适合: 计算机视觉项目需要图片、视频、目标检测、分割、关键点、跟踪、多人协作和标注质量管理。
- 不适合: 以文本、实体抽取、问答数据或 LLM 反馈为主的标注任务，或团队不需要复杂视觉标注工具链。
- 接入成本: 中
- 替代方案: Label Studio, Supervisely, LabelImg
- 评分: 4/5
- 备注: 适合视觉数据集生产；上线前要验证存储规模、视频性能、标注格式、任务拆分、模型辅助标注和导出到训练管线的格式。

## doccano

- GitHub: https://github.com/doccano/doccano
- 官网: https://doccano.github.io/doccano
- 模块: 数据标注 / NLP / 文本分类与序列标注
- 技术栈: Python, Django, Vue, PostgreSQL, Docker
- 许可证: MIT
- 适合: NLP 项目需要快速完成文本分类、序列标注、实体识别、情感分析和翻译/文本生成数据标注。
- 不适合: 需要图像、视频、音频、多模态标注，或复杂人工审核工作流和大规模标注员管理的项目。
- 接入成本: 低
- 替代方案: Label Studio, brat, Prodigy
- 评分: 4/5
- 备注: 适合文本数据集起步和中小团队；接入前要确认导入格式、标签体系、多人一致性、权限、导出格式和模型训练脚本衔接。
