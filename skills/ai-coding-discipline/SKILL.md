---
name: ai-coding-discipline
description: Use when implementing, modifying, refactoring, or debugging code and the main goal is disciplined execution with reuse of existing structure, clear boundaries, incremental verification, error handling, and maintainability.
---

# AI Coding Discipline

Use this skill as an execution gate for engineering changes. Preserve existing behavior unless the task requires changing it, follow current project conventions, and prefer small verified progress over broad unverified rewrites.

Use `project-prompt-polisher` when the user only wants a task description rewritten for another coding agent.

## Core Gate

Before editing code:

1. Understand the outcome, affected workflow, inputs, outputs, state changes, non-goals, and regression risks.
2. Inspect existing structure, tests, helpers, services, schemas, configuration, errors, logging, validation, naming, and style.
3. Prefer extending an existing path over creating a parallel mechanism.
4. Shape the smallest useful change with clear files, responsibilities, contracts, failure behavior, and verification.
5. Implement one closed loop first, then verify before expanding.
6. Refactor only after verification passes.

## Engineering Rules

- Separate orchestration, domain logic, I/O, configuration, formatting, and UI state.
- Handle invalid input, dependency failures, empty states, permission failures, and recovery paths when relevant.
- Avoid duplicate helpers, hardcoded secrets, user-specific paths, happy-path-only logic, and unrelated refactors.
- If asked to skip tests, explain the risk and run the lightest useful alternative check.

## Stop Conditions

Stop and realign before destructive commands, data deletion, migrations, credentials, secret handling, broad rewrites, or risky unverified shortcuts.

## Output Discipline

Report:

- task understanding and assumptions
- inspected files or modules
- design shape before substantial edits
- verification evidence
- remaining risks or blockers

Do not claim completion from inspection alone.

## Supporting Resources

- Read `references/discipline-checklist.md` when the change spans multiple files, boundaries, failure modes, or verification steps and a fuller execution checklist is useful.
- Read `references/pressure-scenarios.md` only when maintaining or testing this skill's resistance to shortcuts and unsafe engineering pressure.
