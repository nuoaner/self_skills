---
name: ai-coding-discipline
description: Use when writing, modifying, refactoring, reviewing, or planning code where maintainability, reuse, clear boundaries, incremental verification, error handling, or engineering discipline matters; also use for Chinese-language requests that ask to write standardized code, implement in an engineering-oriented way, design before coding, avoid reinventing existing mechanisms, keep code stable, or avoid messy code.
---

# AI Coding Discipline

Use this skill as an execution gate for engineering work. Preserve existing behavior unless the task requires changing it, follow the current project's conventions, and prefer small verified progress over broad unverified rewrites.

Mirror the user's language. Do not treat this as advice to summarize after coding; use it before and during the work.

## Core Gate

Before editing code:

1. Understand the outcome, affected workflow, inputs, outputs, state changes, non-goals, and regression risks.
2. Inspect existing structure, tests, helpers, services, hooks, schemas, configuration, errors, logging, validation, naming, and style.
3. Prefer extending an existing path over creating a parallel mechanism.
4. Shape the smallest useful change: touched files, responsibilities, public contracts, failure behavior, and verification.
5. Implement one closed loop first, then verify before expanding.
6. Refactor only after verification passes, then re-run relevant checks.

Ask the user only when ambiguity changes behavior, data, security, cost, or irreversible work. Otherwise make a safe assumption and state it briefly.

## Engineering Rules

- Keep orchestration, domain logic, I/O, configuration, formatting, and UI state separated.
- Handle invalid input, dependency failures, empty states, permission failures, and rollback or recovery paths when relevant.
- Avoid duplicate helpers, overloaded `utils`, hardcoded secrets, user-specific paths, happy-path-only logic, and broad unrelated refactors.
- Do less work with stronger verification under pressure; do not do more work with weaker verification.
- If asked to skip tests, explain the risk and run the lightest useful alternative check.

## Stop Conditions

Stop and realign before continuing when the work requires destructive commands, data deletion, migrations, credentials, secret handling, broad rewrites, risky unverified shortcuts, or unrelated module changes made only for convenience.

## Output Discipline

Keep progress updates concise:

- task understanding and assumptions
- files or modules inspected
- design shape before substantial edits
- verification evidence after checks
- remaining risk or blocker

Do not claim completion from code inspection alone. If verification fails, report the failure and next diagnostic step.

## Resource Use

- Use [discipline-checklist.md](references/discipline-checklist.md) as the execution checklist for implementation work.
- Use [prompt-template.md](references/prompt-template.md) when the user wants a reusable coding prompt.
- Use [pressure-scenarios.md](references/pressure-scenarios.md) when testing whether this skill resists shortcuts and rationalizations.

## Common Mistakes

- Creating abstractions before searching for existing ones.
- Reporting "done" without fresh verification evidence.
- Weakening tests instead of correcting behavior.
- Asking minor questions instead of making safe assumptions.
- Adding comments that explain obvious code rather than important constraints.
