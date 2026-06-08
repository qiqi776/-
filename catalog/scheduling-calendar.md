# 日程预约与日历组件

日程预约与日历组件覆盖预约链接、可用时间管理、会议时间协调、日历视图、外部日历同步和时区处理；项目任务排期放在项目管理分类，后台异步调度放在后台任务分类，工作流编排放在工作流分类。

## Cal.com

- GitHub: https://github.com/calcom/cal.com
- 官网: https://cal.com
- 模块: 日程预约 / 可用时间 / 日历同步
- 技术栈: TypeScript, Next.js, React, Prisma, PostgreSQL
- 许可证: MIT
- 适合: SaaS、咨询、销售、教育、医疗等场景需要自托管预约页、团队排班、支付预约、会议集成和日历同步。
- 不适合: 只需要前端日历视图，或团队不想维护完整预约平台和第三方日历集成。
- 接入成本: 高
- 替代方案: Rallly, FullCalendar, SavvyCal
- 评分: 4/5
- 备注: 功能完整但集成面广；上线前要确认账号体系、OAuth 日历权限、时区、会议链接、支付和通知边界。

## Rallly

- GitHub: https://github.com/lukevella/rallly
- 官网: https://rallly.co
- 模块: 日程协调 / 会议投票 / 可用时间
- 技术栈: TypeScript, Next.js, React, PostgreSQL
- 许可证: AGPL-3.0
- 适合: 团队或社区需要发起时间投票、收集参与者可用时间、确定会议时段和轻量协调日程。
- 不适合: 需要完整预约支付、销售排班、客服排班、复杂日历双向同步，或不能接受 AGPL 网络服务义务。
- 接入成本: 中
- 替代方案: Cal.com, Framadate, Doodle
- 评分: 4/5
- 备注: 更像会议时间协调工具；接入前要确认公开链接、匿名参与、邮件通知、过期策略和隐私边界。

## FullCalendar

- GitHub: https://github.com/fullcalendar/fullcalendar
- 官网: https://fullcalendar.io
- 模块: 日历视图 / 事件展示 / 拖拽排程
- 技术栈: TypeScript, JavaScript
- 许可证: MIT
- 适合: 应用内需要月/周/日历视图、事件拖拽、资源排程、日程展示和前端日历交互。
- 不适合: 需要开箱即用的预约后台、用户可用时间规则、外部日历 OAuth 同步或会议投票系统。
- 接入成本: 中
- 替代方案: Schedule-X, React Big Calendar, Cal.com
- 评分: 4/5
- 备注: 是日历 UI 和交互组件，不是完整预约系统；要自己处理权限、持久化、冲突检测、时区和外部日历同步。
