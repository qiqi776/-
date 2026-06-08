# 图表与数据可视化组件

图表与数据可视化组件覆盖业务仪表盘、运营报表、交互式图表和复杂数据探索界面。

## Apache ECharts

- GitHub: https://github.com/apache/echarts
- 官网: https://echarts.apache.org
- 模块: 可视化 / 通用图表库
- 技术栈: JavaScript, TypeScript, Canvas, SVG
- 许可证: Apache-2.0
- 适合: 需要丰富图表类型、中文生态、地图、仪表盘、大屏和复杂业务报表的 Web 项目。
- 不适合: 只需要少量极简图表，或项目希望完全使用 React 声明式组件模型。
- 接入成本: 中
- 替代方案: Recharts, AntV G2, Chart.js
- 评分: 4/5
- 备注: 功能覆盖广，但复杂配置容易堆积，建议封装项目内统一图表组件和主题。

## Recharts

- GitHub: https://github.com/recharts/recharts
- 官网: https://recharts.org
- 模块: 可视化 / React 图表
- 技术栈: TypeScript, React, SVG
- 许可证: MIT
- 适合: React 项目需要快速构建折线图、柱状图、面积图、饼图和业务仪表盘。
- 不适合: 需要超大数据量渲染、复杂地图、关系图或高度定制底层绘制的场景。
- 接入成本: 低
- 替代方案: Apache ECharts, Nivo, Visx
- 评分: 4/5
- 备注: React 组件心智负担低，适合中小型后台和 SaaS 面板。

## D3

- GitHub: https://github.com/d3/d3
- 官网: https://d3js.org
- 模块: 可视化 / 底层数据驱动渲染
- 技术栈: JavaScript, SVG, Canvas
- 许可证: ISC
- 适合: 需要高度定制的交互式可视化、数据探索、复杂布局和非标准图表的团队。
- 不适合: 只需要常见业务图表且团队缺少可视化工程经验。
- 接入成本: 高
- 替代方案: Apache ECharts, Vega, Observable Plot
- 评分: 4/5
- 备注: 自由度很高，但工程封装和交互设计成本也高；适合做底层能力而不是简单报表首选。
