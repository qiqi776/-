# 数据导入导出与表格文件组件

数据导入导出与表格文件组件覆盖 CSV、Excel、表格解析、批量导入、字段映射、报表导出和浏览器端文件生成；跨系统 ETL/ELT 放在数据管道分类，PDF/Office 预览和文本抽取放在文档处理分类，文件上传和对象存储放在存储分类。

## SheetJS

- GitHub: https://github.com/SheetJS/sheetjs
- 官网: https://sheetjs.com
- 模块: 数据导入导出 / Excel / 表格解析
- 技术栈: JavaScript, TypeScript, Browser, Node.js
- 许可证: Apache-2.0
- 适合: Web 或 Node.js 应用需要读取、生成和转换 XLSX、XLS、CSV、ODS 等多种表格文件，并在浏览器或服务端复用同一套逻辑。
- 不适合: 只需要轻量 CSV 解析，或需要复杂 Excel 样式、公式计算、协同编辑和完整电子表格 UI 的场景。
- 接入成本: 中
- 替代方案: ExcelJS, Papa Parse, Handsontable
- 评分: 4/5
- 备注: 适合通用表格导入导出底座；上线前要验证大文件内存、日期数字格式、编码、隐藏工作表、公式安全和用户上传文件隔离。

## ExcelJS

- GitHub: https://github.com/exceljs/exceljs
- 官网: https://github.com/exceljs/exceljs
- 模块: 数据导入导出 / XLSX / 报表生成
- 技术栈: JavaScript, Node.js, Browser
- 许可证: MIT
- 适合: Node.js 或前端项目需要生成带样式、合并单元格、图片、公式、流式写入和多工作表的 Excel 报表。
- 不适合: 需要覆盖大量旧式表格格式、极轻量 CSV 导入，或对浏览器包体积非常敏感的项目。
- 接入成本: 中
- 替代方案: SheetJS, xlsx-populate, FastExcel
- 评分: 4/5
- 备注: 适合业务报表导出；生产前要测试大文件流式写入、中文字体、日期时区、公式兼容性和下载链路超时。

## Papa Parse

- GitHub: https://github.com/mholt/PapaParse
- 官网: https://www.papaparse.com
- 模块: 数据导入导出 / CSV / 浏览器解析
- 技术栈: JavaScript, Browser, Node.js
- 许可证: MIT
- 适合: 前端或 Node.js 应用需要快速解析、校验和导出 CSV，支持分块、worker、多分隔符和浏览器端大文件处理。
- 不适合: 需要读取 XLSX、保留 Excel 样式、多工作表或复杂单元格类型的导入导出场景。
- 接入成本: 低
- 替代方案: SheetJS, csv-parse, fast-csv
- 评分: 4/5
- 备注: 适合 CSV 导入向导和批量上传第一步；要设计字段映射、错误行反馈、编码探测、空值规则、重复行校验和导入回滚策略。
