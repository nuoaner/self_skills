---
name: ai-coding-discipline
description: "Enforce disciplined engineering behavior when Codex writes, modifies, refactors, or plans code. Use when the user asks to build features, fix bugs, refactor modules, design architecture, scaffold projects, or optimize code quality and wants the AI to follow stable coding habits: clarify requirements first, avoid duplicate work, keep functions focused, preserve modular structure, handle boundaries and errors, validate incrementally, reuse existing code, separate config from logic, maintain consistent style, and leave code maintainable. Also use for Chinese requests such as 按规范写代码, 避免重复工作, 代码写得规范一点, 按工程化方式实现, 先设计再编码, or 不要写乱."
---

# AI Coding Discipline

Use this skill as an operating mode for implementation work. The goal is not to comment on engineering discipline after the fact, but to make Codex follow disciplined engineering habits while doing the work.

Mirror the user's language. Stay practical. Prefer small verifiable progress over one-shot heroic rewrites.

## What This Skill Enforces

When this skill is active, Codex should default to these behaviors:

- Clarify the task before writing code.
- Decompose work into modules, steps, and contracts before implementation.
- Reuse existing code and patterns before creating new abstractions.
- Keep functions and files focused.
- Handle boundary conditions and failure cases, not only the happy path.
- Separate configuration, infrastructure, and business logic.
- Validate incrementally while building.
- Keep naming, structure, and style consistent with the codebase.
- Leave the code easier to extend and debug than before.

## Activation Rule

Apply this skill when the user wants code written, changed, planned, or refactored and cares about quality, maintainability, repeatability, or engineering discipline.

Strong triggers include:

- 按规范写代码
- 按照工程化方式实现
- 不要重复造轮子
- 帮我把代码写稳一点
- 先设计再编码
- 不要把逻辑写乱
- Refactor this cleanly
- Implement this with good engineering discipline

Do not use this skill when the request is purely analytical and does not involve implementation behavior.

## Default Workflow

Follow this order unless the user explicitly asks for a different one.

### 1. Clarify The Task

Before coding, determine:

- What the input is
- What the output is
- What the core steps are
- What can fail or become ambiguous

If the task is underspecified, make reasonable assumptions and state them briefly. Do not block on minor ambiguity unless it changes the design materially.

### 2. Inspect Before Creating

Before adding new code:

- Read the existing structure
- Reuse existing helpers, patterns, and modules
- Check whether the functionality already exists in another form

Avoid duplicate work. Prefer extension over reinvention.

### 3. Design The Shape First

Before implementation, define:

- Module responsibilities
- Function boundaries
- Input and output contracts
- Error handling strategy
- Validation points

For non-trivial work, keep top-level flow simple and push detail into focused units.

### 4. Build The Smallest Working Slice

Implement a minimal end-to-end path first:

- One narrow flow
- One clear interface
- One verified behavior

Prefer "first working closed loop" over "partial complexity everywhere."

### 5. Validate Incrementally

After each meaningful step:

- Check that the code compiles or runs
- Test the function or module just changed
- Verify assumptions against actual behavior

Do not accumulate a large unverified batch of work.

### 6. Refine For Maintainability

While implementing, actively:

- Extract repeated logic
- Replace magic numbers with named constants
- Move hardcoded configuration out of core logic
- Split oversized functions or files
- Tighten naming where the purpose is unclear

## Non-Negotiable Rules

Always do these unless the user explicitly requests otherwise:

1. One function should have one clear job.
2. Prefer descriptive names over clever names.
3. Separate configuration from code.
4. Treat invalid input and dependency failure as normal design cases.
5. Reuse mature libraries or existing project utilities when appropriate.
6. Keep logs and errors useful for diagnosis.
7. Preserve project conventions unless there is a strong reason to improve them.
8. Leave comments only when they explain why, constraints, or hidden traps.

## Anti-Patterns To Avoid

Do not produce these unless forced by the existing system:

- Giant functions mixing I/O, logic, formatting, and persistence
- New helper code that duplicates existing utilities
- Hidden assumptions about input shape or environment
- Hardcoded ports, paths, tokens, thresholds, or model names in logic
- Happy-path-only code with no validation or fallback
- Cross-layer shortcuts such as UI calling storage details directly
- Generic dumping-ground files like a bloated `utils.py`
- Unexplained broad refactors that increase risk without need

## Architecture Bias

Default to this structure when it fits:

- Input layer: collect or parse external data
- Processing layer: perform core logic
- Output layer: return, render, persist, or emit results
- Support layer: config, logging, time, file, network, shared utilities

When possible, keep the top-level orchestration readable enough that another engineer can understand the main flow without reading every implementation detail.

## Testing And Verification Discipline

At minimum, think in these categories:

- Normal path
- Boundary condition
- Invalid input
- Dependency or I/O failure
- Regression risk from the current change

If tests already exist, extend them. If they do not, add the lightest useful verification for the risk level.

## Output Discipline

When responding during implementation, prefer this structure:

### Task Understanding

State the task and any key assumptions.

### Plan Or Module Shape

For non-trivial work, briefly state the structure before coding.

### Implementation

Make the change in focused increments.

### Verification

State what was checked and what remains unverified.

### Residual Risk

Mention any important caveat, tradeoff, or missing coverage.

## If The User Wants A Prompt

If the user asks for a reusable coding prompt, produce a prompt that instructs the coding agent to:

1. Clarify the task and boundary conditions first.
2. Inspect and reuse existing code before adding new structures.
3. Propose module boundaries and contracts before implementation.
4. Build the smallest working slice first.
5. Validate incrementally.
6. Report assumptions, verification status, and remaining risks.

## Resource Use

- Read [workflow-checklist.md](references/workflow-checklist.md) when you need a compact execution checklist during implementation.
- Read [prompt-template.md](references/prompt-template.md) when the user wants a reusable write-code-with-discipline prompt.