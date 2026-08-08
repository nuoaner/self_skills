---
name: ai-coding-paradigm
description: Use when reviewing engineering maturity, architecture boundaries, module design, testing strategy, observability, security posture, delivery readiness, implementation tradeoffs, or technical risk in an existing project, feature, module, API, or system design.
---

# AI Coding Paradigm

## Overview

Use this skill to evaluate whether engineering work is designed and delivered well, not merely whether it runs. Focus on boundaries, contracts, verification, observability, safety, delivery readiness, and maintainability.

If the user's primary request is to rewrite a rough task into a Codex-ready implementation prompt, use `project-prompt-polisher` instead.

## Review Modes

| Mode | Use When | Output |
|---|---|---|
| `maturity-review` | Reviewing a project or feature for engineering maturity | Score, strengths, gaps, priority improvements |
| `boundary-review` | A module/component/API feels tangled or hard to change | Responsibility map, coupling risks, split recommendations |
| `delivery-review` | Preparing for handoff, release, acceptance, or joint debugging | Verification, rollback, observability, deployment risks |
| `risk-review` | Checking security, data, permission, environment, or operational risk | Risk list, severity, mitigation path |

## Core Workflow

1. Identify the target: repository, module, feature, API, UI flow, or delivery process.
2. Choose the review mode.
3. Inspect concrete evidence: files, responsibilities, contracts, tests, logs, config, deployment, and docs when available.
4. Judge the engineering quality with evidence.
5. Separate issues into:
   - must fix before delivery
   - should fix next iteration
   - can improve later

## Quality Rules

- Tie major claims to concrete evidence or mark them as inference.
- Do not recommend rewrites when a boundary repair or adapter is enough.
- Consider tests, logs, permissions, environment variables, rollback, and API compatibility.
- Separate immediate delivery risks from long-term improvements.

## Common Failure Modes

- Saying "the architecture is unclear" without identifying the boundary problem.
- Focusing only on code style while ignoring contracts, tests, delivery, and observability.
- Suggesting broad refactors without migration path or regression protection.
