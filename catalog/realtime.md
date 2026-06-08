# 实时通信组件

实时通信组件覆盖 WebSocket、实时推送、多人协作、在线状态、聊天室和低延迟事件广播。

## Socket.IO

- GitHub: https://github.com/socketio/socket.io
- 官网: https://socket.io
- 模块: 实时通信 / WebSocket
- 技术栈: TypeScript, Node.js
- 许可证: MIT
- 适合: Node.js 项目需要双向实时通信、房间、命名空间、断线重连和降级传输。
- 不适合: 只需要单向服务端事件，或项目对协议标准化和跨语言客户端要求很高。
- 接入成本: 中
- 替代方案: ws, Centrifugo, Ably
- 评分: 4/5
- 备注: 易上手但不是裸 WebSocket 协议，客户端和服务端要成套设计。

## Centrifugo

- GitHub: https://github.com/centrifugal/centrifugo
- 官网: https://centrifugal.dev
- 模块: 实时通信 / 实时消息服务
- 技术栈: Go, WebSocket, SSE
- 许可证: Apache-2.0
- 适合: 需要独立实时消息服务、频道订阅、在线状态、后端语言无关和水平扩展的项目。
- 不适合: 只需要很小的单机 WebSocket 功能，或团队不想维护额外服务。
- 接入成本: 中
- 替代方案: Socket.IO, NATS WebSocket, Pusher
- 评分: 4/5
- 备注: 适合把实时层从业务 API 中拆出来，但鉴权、频道命名和消息可靠性要提前设计。

## Liveblocks

- GitHub: https://github.com/liveblocks/liveblocks
- 官网: https://liveblocks.io
- 模块: 实时通信 / 多人协作
- 技术栈: TypeScript, React
- 许可证: Apache-2.0
- 适合: 需要在线协作、多人光标、评论、房间状态、协作编辑和前端快速集成的产品。
- 不适合: 必须完全自托管实时协作后端，或不希望依赖托管协作平台的项目。
- 接入成本: 中
- 替代方案: Yjs, PartyKit, 自研 WebSocket 协作层
- 评分: 4/5
- 备注: 适合快速做协同体验，生产前要确认数据边界、托管成本和离线冲突策略。
