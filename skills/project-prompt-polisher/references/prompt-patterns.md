# Project Prompt Polisher Patterns

Use this reference when the prompt needs more than the default structure.

## Universal Prompt Skeleton

```text
请基于当前项目完成以下任务，先阅读相关代码/文档，复用已有结构、组件、工具函数和工程约定，避免重复造轮子。

背景：
<已知上下文，不确定的不要编造>

目标：
<期望达成的具体结果>

修改范围：
- <文件/目录/模块/页面/API/文档>

具体要求：
1. <可执行要求>
2. <可执行要求>
3. <可执行要求>

约束：
- 不要修改与本任务无关的功能。
- 不要破坏现有路由、权限、接口、数据结构、样式规范或用户流程。
- 如发现当前描述与项目实际不一致，先以项目实际为准，并在结果中说明。

验收标准：
1. <可观察结果>
2. <测试/构建/截图/API/文档检查>

交付说明：
- 说明改了哪些文件。
- 说明如何验证。
- 说明仍需确认的问题。
```

## UI / Frontend Prompt

Add these dimensions when polishing UI work:

- Target page/component and user scenario.
- Layout hierarchy, spacing, alignment, overflow, and responsive behavior.
- Loading, empty, error, disabled, and permission states.
- Design-system reuse and style boundaries.
- Browser or screenshot verification.

Template:

```text
请基于当前项目优化 <页面/组件>，保持现有业务逻辑、接口调用、路由跳转和权限判断不变，只调整本次明确要求的交互与展示。

目标：
<用户看到/操作时应获得什么改善>

具体要求：
1. 明确主次操作层级，避免页面拥挤或误操作。
2. 处理加载、空数据、错误、禁用和权限不足状态。
3. 保证桌面端和移动端布局稳定，不产生遮挡、错位或异常横向滚动。
4. 复用项目已有组件、样式变量和交互规范。

验收标准：
1. 页面在目标尺寸下展示正常。
2. 原有功能仍可触发。
3. 提供截图或说明验证方式。
```

## Backend / API Prompt

Add these dimensions:

- Endpoint, method, request params, response contract.
- Validation, auth, permission, error codes.
- Logging and observability.
- Backward compatibility with existing clients.
- Unit/integration tests.

Template:

```text
请基于当前项目完善 <接口/服务>，保持现有客户端调用兼容，重点补强参数校验、错误处理、权限边界和可验证性。

具体要求：
1. 明确请求参数、必填字段、字段格式和默认值。
2. 明确成功与失败返回结构，避免泄露敏感信息。
3. 覆盖权限不足、参数缺失、资源不存在、状态冲突等异常场景。
4. 保留现有认证、日志和中间件约定，除非发现明确缺陷。
5. 增加或更新测试用例。

验收标准：
1. 正常请求返回符合约定。
2. 主要异常场景返回稳定错误码和提示。
3. 测试覆盖成功路径和失败路径。
```

## Documentation Prompt

Add these dimensions:

- Target docs and source of truth.
- Required sections.
- Stale content removal.
- Links, commands, examples, and screenshots.
- Secret-safe examples.

Template:

```text
请基于当前项目整理 <README/docs/说明文档>，保持项目事实准确，不编造功能、接口、部署方式或负责人信息。

具体要求：
1. 先阅读现有 README、docs 和项目结构，识别过期、重复或缺失内容。
2. 补充项目简介、运行方式、目录结构、核心功能、配置说明、文档索引和后续计划。
3. 将详细需求、接口、数据库、部署、测试、变更记录拆到 docs 中，README 只保留入口信息。
4. 示例配置必须使用占位符，不要写入真实 token、密码、密钥或连接串。

验收标准：
1. README 可作为项目入口。
2. docs 链接有效。
3. 没有明显过期描述或真实敏感信息。
```

## Testing / Debugging Prompt

Add these dimensions:

- Reproduction steps.
- Expected vs actual behavior.
- Suspected scope.
- Diagnostic commands.
- Regression test and verification.

Template:

```text
请基于当前项目定位并修复以下问题，不要直接大范围重写。先复现或推断最小复现场景，再定位根因，最后做最小修复。

问题现象：
<现象>

期望结果：
<期望>

要求：
1. 先检查相关日志、调用链、状态流和边界条件。
2. 给出根因判断，不要只改表面现象。
3. 做最小范围修复，避免影响无关模块。
4. 增加或更新回归验证。

验收标准：
1. 原问题不再出现。
2. 相关正常流程不回归。
3. 说明验证命令或验证步骤。
```

## Refactor Prompt

Add these dimensions:

- Behavior preservation.
- Module boundaries.
- Migration path.
- Test coverage.
- Rollback risk.

Template:

```text
请对 <模块/文件/目录> 做小步重构，目标是提升可维护性和边界清晰度，必须保持外部行为、接口契约和用户流程不变。

具体要求：
1. 先说明当前职责混杂或重复点。
2. 按单一职责拆分模块，保留现有对外调用方式或提供兼容层。
3. 删除重复逻辑前确认已有复用点。
4. 补充或更新测试，证明行为未变化。

验收标准：
1. 外部行为不变。
2. 模块职责更清晰。
3. 测试或构建通过。
```

## Automation / Script Prompt

Add these dimensions:

- Input/output contract.
- Dry-run for risky operations.
- Idempotency.
- Logging.
- Error handling.

Template:

```text
请基于当前项目编写或完善 <脚本/自动化流程>，要求输入输出明确、可重复执行、错误可诊断。

具体要求：
1. 明确输入参数、默认值、输出文件或执行结果。
2. 对可能修改文件、调用外部服务或删除数据的操作提供 dry-run 或确认机制。
3. 增加日志和错误提示，失败时能定位到具体步骤。
4. 保证重复执行不会产生不可控副作用。

验收标准：
1. 正常输入可得到预期输出。
2. 异常输入有明确错误提示。
3. 说明运行命令和验证方式。
```

## Handoff Prompt

Use when the polished prompt is for another Codex thread, another AI agent, or another developer.

```text
请接手以下任务。开始前先阅读项目结构、README/agent.md 以及相关模块代码，不要假设上下文。

任务目标：
<目标>

已知背景：
<事实>

需要修改：
- <范围>

不能修改：
- <边界>

验收标准：
- <标准>

交付要求：
- 列出修改文件。
- 列出验证命令和结果。
- 标明未完成或需确认事项。
```

## Pressure Examples

### Vague UI

Input:

```text
这个页面按钮太乱了，帮我优化一下
```

Expected polishing focus:

- Define primary/secondary/danger action hierarchy.
- Preserve original button behavior.
- Add responsive and overflow checks.

### Vague API

Input:

```text
登录接口帮我完善一下
```

Expected polishing focus:

- Define request/response.
- Add validation and failure cases.
- Preserve auth compatibility.
- Add tests.

### Vague Cleanup

Input:

```text
项目有点乱，帮我整理一下
```

Expected polishing focus:

- Ask or assume a safe scope.
- Avoid broad destructive cleanup.
- Limit to structure/readme/dependency notes unless explicitly told to refactor code.
