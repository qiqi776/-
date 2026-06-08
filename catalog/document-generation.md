# 文档生成与模板输出组件

文档生成与模板输出组件覆盖把业务数据渲染成 PDF、DOCX、PPTX、HTML 打印件、合同、报价单、收据、报告和批量交付文件。它解决“如何从模板和数据生成可下载、可打印、可归档文件”的问题；PDF 预览、Office 解析和文本抽取放在文档处理分类，电子签署流程放在电子签名分类，发票税务流程放在账单与发票分类。

## WeasyPrint

- GitHub: https://github.com/Kozea/WeasyPrint
- 官网: https://weasyprint.org
- 模块: 文档生成 / HTML CSS 转 PDF / 打印排版
- 技术栈: Python, HTML, CSS, PDF, tinyhtml5, tinycss2, fonttools
- 许可证: BSD-3-Clause
- 适合: 后端服务需要把 HTML/CSS 模板生成高质量 PDF，用于报表、合同、证书、发货单、报价单和可打印文档。
- 不适合: 需要完整浏览器渲染兼容、复杂 JavaScript 执行、交互式 PDF 编辑或像素级复刻 Chromium 页面输出的场景。
- 接入成本: 中
- 替代方案: pdfmake, Paged.js, Playwright PDF
- 评分: 4/5
- 备注: 适合让前端样式和 PDF 模板复用一部分规则；生产前要验证字体、分页、页眉页脚、图片资源、容器依赖和大批量生成性能。

## pdfmake

- GitHub: https://github.com/bpampuch/pdfmake
- 官网: https://pdfmake.github.io/docs
- 模块: 文档生成 / JavaScript PDF / 声明式文档定义
- 技术栈: JavaScript, Node.js, Browser, PDFKit
- 许可证: MIT
- 适合: Web 或 Node.js 项目需要用声明式 JSON 结构生成表格、布局、字体、页眉页脚和下载/打印 PDF。
- 不适合: 文档模板主要由设计师维护在 HTML、Word 或可视化工具里，或需要 CSS 打印标准和复杂分页控制。
- 接入成本: 中
- 替代方案: WeasyPrint, PDFKit, React PDF
- 评分: 4/5
- 备注: 适合代码驱动的 PDF 输出；落地时要定义文档 schema、字体打包、表格换页、浏览器/服务端生成位置和安全输入边界。

## Docxtemplater

- GitHub: https://github.com/open-xml-templating/docxtemplater
- 官网: https://docxtemplater.com
- 模块: 文档生成 / DOCX PPTX 模板 / Office 文件填充
- 技术栈: JavaScript, Node.js, Browser, DOCX, PPTX, PizZip
- 许可证: MIT / GPL-3.0
- 适合: 业务人员或客户需要用 Word、PowerPoint 模板维护版式，再由系统填充占位符、循环和条件生成合同、报告、通知书和演示文件。
- 不适合: 只需要简单 PDF 输出，或项目依赖图片、HTML、图表、Excel 等高级模板能力但不能接受付费模块边界。
- 接入成本: 中
- 替代方案: WeasyPrint, LibreOffice headless, Carbone
- 评分: 4/5
- 备注: 开源核心足够覆盖常见 DOCX/PPTX 占位符和循环；正式选型前要确认双许可、付费模块、模板校验、错误定位和非技术人员编辑流程。
