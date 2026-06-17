---
name: project-prompt-polisher
description: Use when the user asks to polish, optimize, rewrite, clarify, or strengthen a rough Chinese task request or AI coding prompt into an implementation-ready prompt. Applies to product changes, UI/frontend work, backend/API work, documentation, testing, refactoring, automation, repository cleanup, and agent handoff prompts.
---

# Project Prompt Polisher

Rewrite rough Chinese requests into prompts another Codex or AI coding agent can execute with minimal ambiguity.

The output should preserve the user's intent, make hidden constraints explicit, and turn vague wording into concrete scope, files, behaviors, acceptance criteria, and non-regression requirements.

## Use Cases

Use this skill when the user wants to:

- polish a prompt
- optimize a modification request
- turn a vague idea into an executable development instruction
- rewrite Chinese product, UI, frontend, backend, docs, test, refactor, or automation requirements
- prepare a prompt for another Codex thread, agent, developer, or subtask

Do not invent business facts. If important context is missing, keep assumptions explicit or add a short "需要确认" section.

## Rewrite Workflow

1. Identify the task type: UI/frontend, backend/API, data/database, documentation, testing, refactor, automation, or repository/process work.
2. Extract the target: page, component, module, API, file, workflow, document, or repository.
3. Convert vague verbs into concrete actions: add, remove, align, resize, split, rename, validate, persist, query, test, document, deploy, or review.
4. Add boundaries:
   - what must stay unchanged
   - what should not be expanded
   - what existing behavior must not regress
5. Add verification:
   - visual check for UI
   - API response or data check for backend
   - command/test/build check for code
   - checklist or audit result for docs/repository work
6. Return a clean prompt the user can copy directly.

## Output Rules

- Default to Chinese unless the user asks for English.
- Default to one polished prompt only.
- Preserve the user's project terms and naming.
- Add numbered requirements when the request contains multiple changes.
- Add acceptance criteria for anything that can be tested.
- Add "不要" constraints when scope drift is likely.
- Mention assumptions only when they materially affect implementation.
- Do not explain the rewrite unless the user asks why.

## Prompt Template

Use this shape for most implementation prompts:

```text
请基于当前项目完成以下修改，保持现有架构、代码风格、业务逻辑和数据流不变，除非下方明确要求调整。

目标：
<用 1-2 句话说明要解决的问题和期望结果>

修改范围：
- <页面/组件/模块/API/文档/脚本/目录>

具体要求：
1. <可执行改动点>
2. <可执行改动点>
3. <可执行改动点>

约束：
- 不要扩展与本次目标无关的功能。
- 不要破坏现有路由、权限、接口、数据结构或用户流程。
- 复用项目已有组件、工具函数、样式规范和工程约定。

验收标准：
1. <用户或开发者能验证的结果>
2. <测试、构建、截图、接口返回、文档检查等验证方式>
```

## Task-Specific Additions

### UI / Frontend

Add requirements for layout, responsiveness, overflow, loading, empty state, error state, and visual consistency. Ask for screenshots or browser verification when appropriate.

### Backend / API

Add requirements for request/response contract, validation, error handling, permission checks, logging, and compatibility with existing clients.

### Data / Database

Add requirements for schema impact, migration, rollback, sample data, data validation, and backward compatibility.

### Documentation

Add requirements for target files, required sections, source of truth, stale content removal, link consistency, and examples that avoid real secrets.

### Testing / Debugging

Add reproduction steps, expected behavior, actual behavior, suspected scope, tests to add, and verification commands.

### Refactor

Add behavior-preservation constraints, module boundaries, migration path, tests, and rollback risk.

### Automation / Scripts

Add input/output contract, dry-run mode if destructive actions are possible, logging, error handling, and idempotency.

## Examples

### UI Request

User:

```text
这个页面按钮太乱了，帮我优化一下
```

Polished prompt:

```text
请基于当前项目优化该页面的按钮区域，保持现有业务逻辑、路由跳转、权限判断和接口调用不变，只调整按钮的组织方式与视觉层级。

目标：
让主要操作、次要操作和危险操作更容易区分，减少按钮拥挤和误操作风险。

具体要求：
1. 梳理当前页面所有按钮，按主操作、次操作、危险操作进行层级区分。
2. 主操作只保留 1 个视觉重点，其他操作降低视觉权重或收纳到更多操作菜单中。
3. 保持按钮文案清晰，不要使用含糊的“处理”“操作”等泛化词。
4. 在移动端或窄屏下保证按钮不换行挤压、不遮挡内容、不产生横向滚动。

约束：
- 不要改变按钮原有业务逻辑。
- 不要删除现有功能入口，除非明确说明迁移到新的位置。

验收标准：
1. 页面在桌面端和移动端按钮布局稳定。
2. 主操作一眼可见，危险操作有明显区分。
3. 原有按钮功能仍可正常触发。
```

### Backend Request

User:

```text
登录接口帮我完善一下
```

Polished prompt:

```text
请基于当前项目完善登录接口，保持现有认证流程和客户端调用方式兼容，重点补强参数校验、错误返回和安全边界。

目标：
让登录接口在账号不存在、密码错误、参数缺失、账号禁用等情况下返回稳定且可诊断的结果。

具体要求：
1. 明确登录接口的请求参数、必填字段和字段格式校验。
2. 补充账号不存在、密码错误、账号禁用、参数缺失等错误场景处理。
3. 统一返回结构，避免泄露敏感信息。
4. 保留现有 token 或 session 生成逻辑，除非发现明确缺陷。
5. 增加或更新对应测试用例。

验收标准：
1. 正常账号可以登录成功。
2. 异常场景返回明确错误码和提示。
3. 测试覆盖正常登录和主要失败场景。
```

## Quality Checklist

Before returning the polished prompt, check:

- Is the target clear?
- Are concrete changes listed?
- Are unchanged areas protected?
- Is scope drift blocked?
- Are verification steps included?
- Are assumptions visible instead of hidden?
