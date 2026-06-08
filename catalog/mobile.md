# 移动端应用组件

移动端应用组件覆盖跨平台 App 框架、移动 UI 运行时和配套构建工具链。

## React Native

- GitHub: https://github.com/facebook/react-native
- 官网: https://reactnative.dev
- 模块: 移动端 / 跨平台 App
- 技术栈: JavaScript, TypeScript, React
- 许可证: MIT
- 适合: 已有 React 或 Web 团队，希望用一套业务代码交付 iOS 与 Android，并保留原生扩展能力。
- 不适合: 需要完全原生 Swift/Kotlin 体验，或对图形渲染、启动性能和平台细节有极高要求的 App。
- 接入成本: 中
- 替代方案: Flutter, Expo, Swift/Kotlin 原生开发
- 评分: 4/5
- 备注: 适合复用前端工程能力，但仍需要理解移动端打包、签名、原生模块和应用商店发布流程。

## Flutter

- GitHub: https://github.com/flutter/flutter
- 官网: https://flutter.dev
- 模块: 移动端 / 跨平台 UI
- 技术栈: Dart
- 许可证: BSD-3-Clause
- 适合: 需要高度一致的跨平台 UI、复杂动画、移动端优先产品，以及希望同一套 UI 覆盖更多终端的团队。
- 不适合: 团队主要技能栈是 JavaScript/React 且不愿引入 Dart，或产品必须深度贴合各平台原生控件风格。
- 接入成本: 中
- 替代方案: React Native, Kotlin Multiplatform, Swift/Kotlin 原生开发
- 评分: 4/5
- 备注: UI 一致性强，技术栈选择会影响招聘、组件生态和长期维护方式。

## Expo

- GitHub: https://github.com/expo/expo
- 官网: https://expo.dev
- 模块: 移动端 / React Native 工具链
- 技术栈: TypeScript, React Native
- 许可证: MIT
- 适合: React Native 项目快速启动、云构建、预览发布、OTA 更新，以及需要常见设备 API 封装的团队。
- 不适合: 从第一天起就要求完全掌控原生工程结构，或无法依赖 Expo 生态与构建服务的项目。
- 接入成本: 低
- 替代方案: React Native CLI, Flutter, Ionic Capacitor
- 评分: 4/5
- 备注: 非常适合 MVP 和多数生产应用，需求深入原生能力时要提前检查模块兼容性。
