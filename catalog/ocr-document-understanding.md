# OCR 与文档识别组件

OCR 与文档识别组件覆盖扫描件、图片、PDF 页面中的文字识别、PDF 文本层生成、版面分析、表格识别和文档结构化抽取。它解决“不可搜索或半结构化文件如何转成可检索、可审核、可入库内容”的问题；PDF 预览和 Office 文本抽取放在文档处理分类，PDF/DOCX 输出放在文档生成分类，RAG 编排放在 AI 分类。

## Tesseract OCR

- GitHub: https://github.com/tesseract-ocr/tesseract
- 官网: https://tesseract-ocr.github.io
- 模块: OCR / 文本识别 / 多语言识别引擎
- 技术栈: C++, Leptonica, CLI, OCR
- 许可证: Apache-2.0
- 适合: 需要本地离线识别扫描图片、票据截图、PDF 页面渲染图，并能接受通过预处理、语言包和页面分割模式调优效果的项目。
- 不适合: 需要开箱即用的版面理解、表格结构抽取、手写体识别或复杂商业文档自动字段解析的场景。
- 接入成本: 中
- 替代方案: OCRmyPDF, PaddleOCR, EasyOCR
- 评分: 4/5
- 备注: 适合作为底层 OCR 引擎嵌入批处理流程；生产前要验证图片预处理、语言包、置信度阈值、并发隔离和异常文件资源限制。

## OCRmyPDF

- GitHub: https://github.com/ocrmypdf/OCRmyPDF
- 官网: https://ocrmypdf.readthedocs.io
- 模块: OCR / PDF 文本层 / 批处理
- 技术栈: Python, Tesseract, Ghostscript, PDF, CLI
- 许可证: MPL-2.0
- 适合: 扫描版 PDF 需要保留原文件外观，同时增加可搜索、可复制、可索引的文字层，用于档案、合同、票据和历史资料入库。
- 不适合: 需要直接抽取结构化表格、字段键值对、复杂版面语义，或不愿维护 Tesseract/Ghostscript 运行环境的项目。
- 接入成本: 中
- 替代方案: Tesseract OCR, PaddleOCR, Apache Tika
- 评分: 4/5
- 备注: 适合放在文件上传后的异步任务中；不可信 PDF 要在隔离 worker 中处理，并限制页数、文件大小、超时和临时文件目录。

## PaddleOCR

- GitHub: https://github.com/PaddlePaddle/PaddleOCR
- 官网: https://www.paddleocr.ai
- 模块: OCR / 文档理解 / 版面表格识别
- 技术栈: Python, PaddlePaddle, Deep Learning, OCR
- 许可证: Apache-2.0
- 适合: 需要更高识别准确率、多语言文字检测识别、版面分析、表格识别、公式识别或文档解析流水线的项目。
- 不适合: 团队缺少机器学习运行环境维护能力，或部署目标对镜像体积、GPU/CPU 推理成本和依赖复杂度非常敏感的项目。
- 接入成本: 高
- 替代方案: Tesseract OCR, EasyOCR, docTR
- 评分: 4/5
- 备注: 适合票据、表单、合同、截图和复杂版式识别；落地时要先用真实样本评估模型、语言、推理延迟、硬件成本和人工复核流程。
