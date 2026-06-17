---
name: ai-coding-discipline
description: Use when writing, modifying, refactoring, reviewing, or planning code where maintainability, reuse, clear boundaries, incremental verification, error handling, or engineering discipline matters; also use for Chinese requests such as 按规范写代码, 工程化实现, 先设计再编码, 不要重复造轮子, 代码写稳一点, 不要写乱.
---

# AI Coding Discipline

Use this skill as an execution gate for engineering work. Its job is to make the agent behave like a disciplined maintainer while coding, not merely explain good habits afterward.

Mirror the user's language. Prefer small verified progress over broad unverified rewrites.

## Core Contract

When this skill is active, the agent must preserve these properties unless the user explicitly accepts the tradeoff:

- Existing behavior stays stable unless the task requires changing it.
- New code follows current project structure, naming, style, and dependency patterns.
- Responsibilities stay separated: orchestration, domain logic, I/O, configuration, and formatting should not collapse into one blob.
- Edge cases, invalid input, dependency failures, and rollback or recovery paths are considered before completion.
- Every meaningful change has a verification path: test, build, lint, smoke check, script output, or documented manual check.

## When To Use

Use this skill for:

- feature implementation
- bug fixes
- refactoring
- architecture or module design
- repository scaffolding
- performance or quality cleanup
- prompts that ask another agent to write code carefully

Strong Chinese triggers include: 按规范写代码, 工程化实现, 不要重复造轮子, 代码写稳一点, 先设计再编码, 不要写乱, 保持可维护, 小步验证.

Do not use it for purely conceptual discussion with no implementation, review, planning, or prompt-writing outcome.

## Execution Gate

Before editing code, pass these gates in order. If a gate cannot be completed, say what is missing and choose the lowest-risk fallback.

### 1. Understand The Work

Identify:

- requested outcome
- affected users or workflows
- input, output, and state changes
- explicit non-goals
- likely regression risks

Ask only when ambiguity changes behavior, data, security, or irreversible work. Otherwise make a reasonable assumption and state it briefly.

### 2. Inspect Before Adding

Search before creating:

- project structure and entry points
- nearby modules and tests
- existing helpers, services, hooks, utilities, types, schemas, and configuration
- conventions for errors, logging, validation, styling, naming, and tests

If a reusable path exists, prefer extending it over creating a parallel mechanism.

### 3. Shape The Change

Before implementation, define the smallest useful design:

- files or modules to touch
- responsibility of each changed unit
- public contracts: function signatures, API shape, events, props, data schema, CLI args, or file format
- validation and failure behavior
- verification command or manual check

For non-trivial work, tell the user this shape before editing. Keep it short.

### 4. Implement A Small Closed Loop

Build one verified slice first:

- one behavior
- one entry point
- one verification path

Do not spread partial complexity across many files before one flow works.

### 5. Verify Before Expanding

After each meaningful change, run the narrowest useful verification. Examples:

- focused unit test
- type check or build
- lint for touched code
- smoke script
- browser or API check
- documented manual reproduction

Do not claim completion based only on code inspection.

### 6. Refactor Only While Green

After verification passes, improve structure without changing behavior:

- remove duplication
- tighten names
- extract focused helpers
- move configuration out of logic
- isolate I/O from domain logic
- reduce hidden coupling

Re-run relevant verification after refactoring.

## Stop Conditions

Stop and realign with the user before continuing when:

- the change requires deleting data, migrations, secrets, credentials, broad rewrites, or destructive commands
- the requested shortcut would skip necessary verification for a risky behavior change
- the existing design contradicts the requested implementation path
- the change touches unrelated modules only to make the current idea convenient
- the task is actually multiple independent projects hidden in one request

## Anti-Patterns

Avoid:

- giant functions mixing I/O, business logic, validation, persistence, and formatting
- duplicate helper code that ignores existing utilities
- hidden assumptions about environment, file paths, locale, time, network, or data shape
- hardcoded secrets, tokens, ports, model names, thresholds, or user-specific paths in core logic
- happy-path-only behavior with no invalid input handling
- vague catch-all modules such as overloaded `utils`, `common`, or `helpers`
- broad refactors not required by the task
- "fixing" tests by weakening assertions instead of correcting behavior

## Pressure Rules

Under time pressure, do less work with stronger verification. Do not do more work with weaker verification.

If the user says "just do it quickly", still inspect first, make a small change, and verify. If the user asks to skip tests, explain the risk and run the lightest alternative check available.

## Output Discipline

During work, keep updates concise:

- task understanding and assumption
- files or modules being inspected
- design shape before substantial edits
- verification evidence after checks
- remaining risk, if any

Do not bury failures. If verification fails, report the failure and next diagnostic step.

## Quick Reference

| Moment | Required behavior |
|---|---|
| Before coding | Inspect existing structure and reuse paths |
| Before design | Define inputs, outputs, constraints, and failure modes |
| Before broad changes | Find the smallest safe slice |
| Before completion | Run fresh verification and read the result |
| If blocked | State the blocker, evidence, and safe next step |
| If asked for a prompt | Produce a copyable prompt using the template |

## Resource Use

- Use [discipline-checklist.md](references/discipline-checklist.md) as the execution checklist for implementation work.
- Use [prompt-template.md](references/prompt-template.md) when the user wants a reusable coding prompt.
- Use [pressure-scenarios.md](references/pressure-scenarios.md) when testing whether this skill resists shortcuts and rationalizations.

## Common Mistakes

- Treating this skill as advice instead of a gate.
- Creating new abstractions before searching for existing ones.
- Reporting "done" without fresh verification evidence.
- Refactoring unrelated code to make the task feel cleaner.
- Adding comments that explain what code obviously does instead of why a constraint exists.
- Asking the user minor questions instead of making safe assumptions.
