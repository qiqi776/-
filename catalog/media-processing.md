# 媒体处理组件

媒体处理组件覆盖图片裁剪压缩、图片代理、音视频转码、缩略图生成和格式转换。

## FFmpeg

- GitHub: https://github.com/FFmpeg/FFmpeg
- 官网: https://ffmpeg.org
- 模块: 媒体处理 / 音视频转码
- 技术栈: C, CLI, Libraries
- 许可证: LGPL-2.1-or-later / GPL-2.0-or-later
- 适合: 需要处理音视频转码、抽帧、剪切、封装转换、流媒体处理和批量媒体任务的项目。
- 不适合: 团队不能处理 LGPL/GPL 合规、编解码器专利风险，或项目只需要简单图片处理。
- 接入成本: 高
- 替代方案: GStreamer, Bento4, HandBrake
- 评分: 4/5
- 备注: 编译选项会影响许可证义务；商业产品需要法务和专利检查，并记录二进制来源。

## Sharp

- GitHub: https://github.com/lovell/sharp
- 官网: https://sharp.pixelplumbing.com
- 模块: 媒体处理 / 图片转换
- 技术栈: JavaScript, Node.js, libvips
- 许可证: Apache-2.0
- 适合: Node.js 服务里做图片缩放、裁剪、格式转换、压缩和缩略图生成。
- 不适合: 需要完整视频处理、浏览器端纯前端图片编辑，或部署环境无法使用原生依赖。
- 接入成本: 低
- 替代方案: ImageMagick, GraphicsMagick, Jimp
- 评分: 4/5
- 备注: 性能适合服务端图片管线；需要关注平台预编译包、内存峰值和大图安全限制。

## imgproxy

- GitHub: https://github.com/imgproxy/imgproxy
- 官网: https://imgproxy.net
- 模块: 媒体处理 / 图片代理
- 技术栈: Go, HTTP, libvips
- 许可证: Apache-2.0
- 适合: 需要把图片缩放、裁剪、格式转换、签名 URL 和缓存友好输出从业务服务中拆出去。
- 不适合: 只需要离线批处理，或必须自己控制每一步图片处理管线逻辑。
- 接入成本: 中
- 替代方案: Thumbor, Imaginary, 自建 Sharp 服务
- 评分: 4/5
- 备注: 适合配合 CDN 和对象存储；必须开启 URL 签名、限制源站和尺寸参数，避免被滥用。
