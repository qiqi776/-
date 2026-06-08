# 音视频通话与会议组件

音视频通话与会议组件覆盖 WebRTC 音视频通话、视频会议、SFU、房间管理、屏幕共享、录制和实时媒体传输；普通 WebSocket 推送放在实时通信分类，离线转码和缩略图生成放在媒体处理分类，会议预约放在日程预约分类。

## LiveKit

- GitHub: https://github.com/livekit/livekit
- 官网: https://livekit.io
- 模块: 音视频通话 / WebRTC / SFU
- 技术栈: Go, WebRTC, Redis
- 许可证: Apache-2.0
- 适合: 需要自托管实时音视频、低延迟直播、互动课堂、语音房、AI 语音代理和多端 SDK 的产品。
- 不适合: 只需要嵌入一个现成会议页面，或团队没有 WebRTC、TURN、带宽和媒体服务器运维经验。
- 接入成本: 高
- 替代方案: Jitsi Meet, mediasoup, Daily
- 评分: 4/5
- 备注: 平台能力完整但运维复杂；上线前要确认 TURN/STUN、区域部署、录制、权限令牌、带宽成本和端到端延迟。

## Jitsi Meet

- GitHub: https://github.com/jitsi/jitsi-meet
- 官网: https://jitsi.org/jitsi-meet
- 模块: 视频会议 / WebRTC / 会议房间
- 技术栈: JavaScript, React, WebRTC, XMPP
- 许可证: Apache-2.0
- 适合: 需要开箱即用的视频会议房间、屏幕共享、会议链接、主持人控制和自托管会议应用。
- 不适合: 需要深度嵌入自定义产品流程、精细媒体管线控制，或团队不想维护 Jitsi Videobridge 和 XMPP 组件。
- 接入成本: 高
- 替代方案: LiveKit, BigBlueButton, Element Call
- 评分: 4/5
- 备注: 更适合完整会议应用；集成前要验证部署拓扑、移动端体验、认证、录制、品牌定制和大会议性能。

## mediasoup

- GitHub: https://github.com/versatica/mediasoup
- 官网: https://mediasoup.org
- 模块: WebRTC / SFU / 媒体服务器库
- 技术栈: TypeScript, Node.js, C++
- 许可证: ISC
- 适合: 团队要自研实时音视频产品，需要底层 SFU、媒体路由、生产者/消费者模型和灵活服务端控制。
- 不适合: 想快速上线会议产品、缺少 WebRTC 专业经验，或不想自己设计信令、房间、鉴权、录制和客户端 SDK。
- 接入成本: 高
- 替代方案: LiveKit, Pion WebRTC, Janus
- 评分: 4/5
- 备注: 自由度高但工程责任重；必须自行设计信令协议、房间生命周期、带宽估计、NAT 穿透和故障恢复。
