# 审计日志与活动记录组件

审计日志与活动记录组件覆盖应用层用户操作留痕、资源变更历史、操作者归因、客户可见审计轨迹、导出和合规查询；系统运行日志放在监控分类，数据库 Schema 变更审计放在数据库迁移分类，授权决策规则放在授权策略分类，隐私请求和同意记录放在隐私合规分类。

## Retraced

- GitHub: https://github.com/retracedhq/retraced
- 官网: https://preview.retraced.io
- 模块: 审计日志 / 嵌入式查看器 / 合规事件
- 技术栈: TypeScript, JavaScript, PostgreSQL, Kubernetes
- 许可证: Apache-2.0
- 适合: B2B SaaS 需要把审计事件发布到独立服务，并向客户暴露可搜索、可导出、可嵌入的审计日志界面。
- 不适合: 只需要在单体应用里记录少量模型变更，或团队不想维护独立审计日志服务和 Kubernetes 部署。
- 接入成本: 高
- 替代方案: PaperTrail, django-auditlog, WorkOS Audit Logs
- 评分: 4/5
- 备注: 适合客户可见审计日志；生产前要确认事件命名、租户隔离、保留周期、导出格式、不可变性保证和审计查看权限。

## PaperTrail

- GitHub: https://github.com/paper-trail-gem/paper_trail
- 官网: https://rubygems.org/gems/paper_trail
- 模块: 审计日志 / Rails 模型版本 / 变更历史
- 技术栈: Ruby, Rails, Active Record
- 许可证: MIT
- 适合: Rails 应用需要记录模型创建、更新、删除、操作者、版本历史，并支持追溯或恢复对象状态。
- 不适合: 非 Rails 项目，或需要跨系统统一查询、客户自助导出、强不可变合规日志和独立审计服务的场景。
- 接入成本: 低
- 替代方案: Audited, Retraced, Laravel Activitylog
- 评分: 4/5
- 备注: 适合 Rails 模型级审计和版本追踪；要提前设计版本表增长、字段过滤、敏感信息脱敏和旧版本清理策略。

## django-auditlog

- GitHub: https://github.com/jazzband/django-auditlog
- 官网: https://django-auditlog.readthedocs.io
- 模块: 审计日志 / Django 模型变更 / 对象历史
- 技术栈: Python, Django
- 许可证: MIT
- 适合: Django 应用需要记录对象变更、操作者、变更摘要、关联请求信息，并通过管理后台或对象历史查看审计记录。
- 不适合: 非 Django 项目，或需要高吞吐事件流、跨服务统一审计账本、外部客户嵌入式查看器的产品。
- 接入成本: 低
- 替代方案: django-simple-history, PaperTrail, Retraced
- 评分: 4/5
- 备注: 适合 Django 模型级审计；上线前要确认注册模型范围、字段屏蔽、关联 ID、日志保留、权限隔离和迁移影响。
