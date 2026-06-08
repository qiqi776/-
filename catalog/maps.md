# 地图与地理位置组件

地图与地理位置组件覆盖交互式地图、瓦片渲染、空间数据展示、地理信息图层和 Web GIS 场景。

## MapLibre GL JS

- GitHub: https://github.com/maplibre/maplibre-gl-js
- 官网: https://maplibre.org
- 模块: 地图 / WebGL 矢量地图
- 技术栈: TypeScript, WebGL
- 许可证: BSD-3-Clause
- 适合: 需要矢量瓦片、地图样式、自托管地图数据、WebGL 性能和 Mapbox GL 风格 API 的项目。
- 不适合: 只需要简单点位地图，或团队不想处理瓦片服务、样式文件和地图数据源。
- 接入成本: 中
- 替代方案: Leaflet, OpenLayers, Mapbox GL JS
- 评分: 4/5
- 备注: 适合需要避免商业地图 SDK 绑定的项目，但底图、瓦片和地理编码仍要单独选型。

## Leaflet

- GitHub: https://github.com/Leaflet/Leaflet
- 官网: https://leafletjs.com
- 模块: 地图 / 轻量交互地图
- 技术栈: JavaScript
- 许可证: BSD-2-Clause
- 适合: 需要快速展示点位、线面、弹窗、简单图层和移动端友好交互的 Web 项目。
- 不适合: 需要大规模矢量瓦片渲染、复杂 3D 地图或重度 GIS 分析的项目。
- 接入成本: 低
- 替代方案: MapLibre GL JS, OpenLayers, Google Maps SDK
- 评分: 4/5
- 备注: 生态插件丰富，适合门店、资产点位、配送范围等常见业务地图。

## OpenLayers

- GitHub: https://github.com/openlayers/openlayers
- 官网: https://openlayers.org
- 模块: 地图 / Web GIS
- 技术栈: JavaScript, TypeScript
- 许可证: BSD-2-Clause
- 适合: 需要复杂图层、投影坐标、空间数据格式、地图编辑和专业 GIS 能力的项目。
- 不适合: 只需要在页面里放一个简单点位地图，或团队缺少 GIS 背景。
- 接入成本: 高
- 替代方案: MapLibre GL JS, Leaflet, Cesium
- 评分: 4/5
- 备注: GIS 能力强，但概念和 API 更专业，适合空间数据是核心资产的项目。
