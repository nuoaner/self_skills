---
name: project-prompt-polisher
description: Use when the user asks to polish, optimize, rewrite, clarify, strengthen, structure, or refine a rough Chinese task request or AI coding prompt into an implementation-ready prompt for product, UI/frontend, backend/API, database, documentation, testing, debugging, refactoring, automation, repository cleanup, or agent handoff work.
---

# Project Prompt Polisher

## Overview

Rewrite rough Chinese requests into prompts another Codex or AI coding agent can execute with minimal ambiguity. Preserve the user's intent while making scope, constraints, acceptance criteria, verification, and non-regression requirements explicit.

Default to a copy-ready Chinese or English prompt that matches the user's language. Do not explain the rewrite unless the user asks.

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
Please complete the following changes based on the current project. Keep the existing architecture, code style, business logic, and data flow unchanged unless the requirements below explicitly say otherwise.

Goal:
<Explain the problem to solve and expected result in 1-2 sentences.>

Change scope:
- <Page/component/module/API/document/script/directory>

Requirements:
1. <Executable change>
2. <Executable change>
3. <Executable change>

Constraints:
- Do not expand functionality unrelated to this goal.
- Do not break existing routes, permissions, APIs, data structures, or user flows.
- Reuse existing components, utilities, style conventions, and engineering patterns.

Acceptance criteria:
1. <User- or developer-verifiable result>
2. <Verification method such as tests, build, screenshot, API response, or documentation audit>

Needs confirmation:
- <Only list unknowns that affect implementation. Omit this section if there are none.>
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
- Missing facts are visible as `Needs confirmation`, not silently invented.
- The final output is copy-ready and does not include analysis unless requested.

## Common Failure Modes

- Keeping the user's vague verb, such as "optimize it", without defining the actual change.
- Forgetting non-regression constraints.
- Adding broad architecture work when the user asked for a narrow change.
- Inventing business background, file paths, API contracts, or dates.
- Returning advice instead of a polished prompt.
