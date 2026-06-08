# 文档处理组件

文档处理组件覆盖 PDF 预览、Office 文档解析、文本抽取和文件内容入库。

## PDF.js

- GitHub: https://github.com/mozilla/pdf.js
- 官网: https://mozilla.github.io/pdf.js/
- 模块: 文档处理 / PDF 预览
- 技术栈: JavaScript, TypeScript, PDF
- 许可证: Apache-2.0
- 适合: Web 应用需要在浏览器内预览 PDF、分页渲染、缩放、文本层和基础批注能力。
- 不适合: 需要服务端高保真 PDF 生成、复杂编辑、签章或 Office 文档预览。
- 接入成本: 中
- 替代方案: React PDF, PSPDFKit, 浏览器原生 PDF Viewer
- 评分: 4/5
- 备注: 适合自定义 PDF 阅读器；大文件、移动端性能和字体渲染要单独测试。

## Apache Tika

- GitHub: https://github.com/apache/tika
- 官网: https://tika.apache.org
- 模块: 文档处理 / 内容抽取
- 技术栈: Java, JVM, CLI, Server
- 许可证: Apache-2.0
- 适合: 需要从 PDF、Office、HTML、图片元数据等多格式文件中抽取文本、元数据和 MIME 类型。
- 不适合: 只处理单一格式，或团队不想引入 JVM 服务/进程。
- 接入成本: 中
- 替代方案: textract, unstructured, Apache POI
- 评分: 4/5
- 备注: 适合搜索索引、RAG 入库、文件审计；要注意不可信文件隔离和资源限制。

## Mammoth.js

- GitHub: https://github.com/mwilliamson/mammoth.js
- 官网: https://github.com/mwilliamson/mammoth.js
- 模块: 文档处理 / DOCX 转换
- 技术栈: JavaScript, Node.js, Browser
- 许可证: BSD-2-Clause
- 适合: 需要把 DOCX 转成干净 HTML 或 Markdown 风格内容，供 CMS、编辑器或文档导入流程使用。
- 不适合: 需要完整保留 Word 版式、批注、复杂表格、页眉页脚或高保真预览。
- 接入成本: 低
- 替代方案: Apache Tika, Pandoc, LibreOffice headless
- 评分: 4/5
- 备注: 关注语义化转换而不是像素级还原，适合导入内容而不是查看原稿。
