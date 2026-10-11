---
name: ai-coding-discipline
description: Use when implementing, modifying, refactoring, or debugging code and the main goal is disciplined execution with reuse of existing structure, clear boundaries, incremental verification, error handling, and maintainability.
---

# AI Coding Discipline

Use this skill as an execution gate for engineering changes. Preserve existing behavior unless the task requires changing it, follow current project conventions, and prefer small verified progress over broad unverified rewrites.

Use `project-prompt-polisher` when the user only wants a task description rewritten for another coding agent.

## Core Gate

Before editing code:

For a small, low-risk change, inspect the relevant code, make the narrowest useful edit, and run a relevant check directly. For multi-module or high-risk work, establish impacted contracts, dependencies, state transitions, failure modes, and a focused validation plan before editing. Reuse existing patterns when appropriate; do not force incremental micro-steps if one cohesive change is safer and easier to test.

## Engineering Rules

- Separate orchestration, domain logic, I/O, configuration, formatting, and UI state.
- Handle invalid input, dependency failures, empty states, permission failures, and recovery paths when relevant.
- Avoid duplicate helpers, hardcoded secrets, user-specific paths, happy-path-only logic, and unrelated refactors.
- If asked to skip tests, explain the risk and run the lightest useful alternative check.

## Stop Conditions

Treat destructive operations, production data changes, migrations, credential access, and permission changes as high-risk. Inspect impact and backup or rollback options first. Obtain user authorization where a new destructive action is not already explicitly authorized; do not block routine, reversible edits with repeated confirmations.

## Output Discipline

Report:

- task understanding and assumptions
- inspected files or modules
- material design decisions when relevant
- verification evidence
- remaining risks or blockers

Do not claim completion from inspection alone.

## Supporting Resources

- Read `references/discipline-checklist.md` when the change spans multiple files, boundaries, failure modes, or verification steps and a fuller execution checklist is useful.
- Read `references/pressure-scenarios.md` only when maintaining or testing this skill's resistance to shortcuts and unsafe engineering pressure.
