---
name: project-prompt-polisher
description: Use when the user asks to polish, optimize, rewrite, clarify, strengthen, structure, or refine a rough Chinese task request or AI coding prompt into an implementation-ready prompt for product, UI/frontend, backend/API, database, documentation, testing, debugging, refactoring, automation, repository cleanup, or agent handoff work.
---

# Project Prompt Polisher

## Overview

Rewrite rough Chinese requests into prompts another Codex or AI coding agent can execute with minimal ambiguity. Preserve the user's intent while making scope, constraints, acceptance criteria, verification, and non-regression requirements explicit.

Default to a copy-ready Chinese prompt. Do not explain the rewrite unless the user asks.

## Fast Workflow

1. Identify task type: product, UI/frontend, backend/API, data/database, documentation, testing/debugging, refactor, automation, repository/process, or handoff.
2. Extract the target: page, component, module, API, file, workflow, document, repository, or deployment path.
3. Convert vague verbs into concrete actions: add, remove, align, resize, split, rename, validate, persist, query, test, document, deploy, review, or migrate.
4. Add boundaries:
   - unchanged business logic
   - unchanged routes, permissions, data structure, API contract, or user flow
   - no unrelated feature expansion
   - reuse existing components, utilities, style rules, and project conventions
5. Add verification:
   - UI: screenshot, responsive check, loading/empty/error states
   - backend: request/response, error cases, permission, logs, tests
   - docs/repo: checklist or audit result
   - scripts: dry-run, idempotency, logs, error handling
6. Return one clean prompt unless the user asks for multiple versions.

## Output Contract

Use this structure by default:

```text
请基于当前项目完成以下修改，保持现有架构、代码风格、业务逻辑和数据流不变，除非下方明确要求调整。

目标：
<1-2 句话说明要解决的问题和期望结果>

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

需要确认：
- <仅列出会影响实现的重要未知项；没有则省略>
```

## When to Read References

Read `references/prompt-patterns.md` when:

- the request spans multiple domains
- the user asks for a high-quality or reusable prompt
- the prompt is for another agent, another thread, or a handoff
- the request involves UI, API, database, docs, tests, refactor, automation, or deployment details
- the first rewrite would otherwise be generic

## Quality Bar

Before returning, check:

- Target is explicit.
- Concrete changes are listed.
- Unchanged areas are protected.
- Scope drift is blocked.
- Verification is actionable.
- Missing facts are visible as `需要确认`, not silently invented.
- The final output is copy-ready and does not include analysis unless requested.

## Common Failure Modes

- Keeping the user's vague verb, such as "优化一下", without defining the actual change.
- Forgetting non-regression constraints.
- Adding broad architecture work when the user asked for a narrow change.
- Inventing business background, file paths, API contracts, or dates.
- Returning advice instead of a polished prompt.
