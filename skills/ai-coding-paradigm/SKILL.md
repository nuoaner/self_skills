---
name: ai-coding-paradigm
description: Use when analyzing code quality, architecture boundaries, delivery flow, testing strategy, observability, security posture, engineering maturity, module design, implementation tradeoffs, or when turning a rough feature idea into an AI-executable engineering prompt.
---

# AI Coding Paradigm

## Overview

Use this skill to judge whether a project, feature, module, or prompt is engineered well, not merely whether it can run. Focus on boundaries, contracts, verification, observability, safety, delivery, and AI executability.

Default to a direct conclusion first, then concrete evidence and prioritized improvements. Avoid abstract architecture vocabulary unless it is tied to actual files, modules, interfaces, tests, or delivery steps.

## Review Modes

| Mode | Use When | Output |
|---|---|---|
| `maturity-review` | Reviewing a project or feature for engineering maturity | Score, strengths, gaps, priority improvements |
| `boundary-review` | A module/component/API feels tangled or hard to change | Responsibility map, coupling risks, split recommendations |
| `delivery-review` | Preparing for handoff, release, acceptance, or joint debugging | Verification, rollback, observability, deployment risks |
| `prompt-hardening` | Turning a rough task into an AI-executable engineering prompt | Copy-ready prompt with scope, contracts, tests, and constraints |
| `risk-review` | Checking security, data, permission, environment, or operational risk | Risk list, severity, mitigation path |

## Core Workflow

1. Identify the target: repository, module, feature, API, UI flow, prompt, or delivery process.
2. Choose the review mode.
3. Inspect concrete evidence: files, responsibilities, contracts, tests, logs, config, deployment, and docs when available.
4. Score or judge the ten engineering dimensions.
5. Separate issues into:
   - must fix before delivery
   - should fix next iteration
   - can improve later
6. If the user wants implementation help, output a copy-ready prompt instead of broad advice.

## Ten Engineering Dimensions

For detailed scoring, read `references/paradigm-checklist.md`.

1. Requirement and boundary clarity
2. Single responsibility and module cohesion
3. Dependency direction and layering
4. Interface and data contracts
5. Validation and error handling
6. Testability and regression protection
7. Observability and diagnosability
8. Security, permission, and data safety
9. Delivery, rollback, and environment readiness
10. AI executability and handoff clarity

## Output Contract

Use this structure for reviews:

```text
Overall judgment:
<mature / basically usable / high risk / not recommended for further expansion>, with one sentence explaining why.

Score:
| Dimension | Score (0-2) | Evidence | Recommendation |
|---|---:|---|---|

Main strengths:
- ...

Main issues:
- ...

Priority recommendations:
- Must fix before delivery:
- Should fix in the next iteration:
- Later improvements:

If this should be handed to an AI agent for implementation:
<copy-ready prompt; read references/prompt-templates.md when needed>
```

## When to Read References

Read `references/paradigm-checklist.md` when:

- the user asks for scoring, review, audit, maturity, or architecture analysis
- the project is large or has multiple modules
- you need to produce a defensible quality judgment

Read `references/prompt-templates.md` when:

- the user wants a stronger AI coding prompt
- the output needs to guide another agent/developer
- the request involves implementation sequencing, verification, rollback, or boundaries

## Quality Gate

Before finalizing:

- Tie every major claim to concrete evidence or mark it as an inference.
- Do not recommend a rewrite when a boundary repair or adapter would solve the issue.
- Do not ignore tests, logs, permissions, environment variables, rollback, or API compatibility.
- Separate immediate delivery risks from long-term refactors.
- If writing a prompt, include scope, unchanged constraints, contracts, verification, and reporting requirements.

## Common Failure Modes

- Saying "the architecture is unclear" without naming the actual boundary problem.
- Focusing only on code style while ignoring contracts, tests, delivery, and observability.
- Treating temporary compatibility code as final design.
- Suggesting broad refactors without migration path or regression protection.
- Letting an AI prompt say "optimize everything" without scope, contract, or acceptance criteria.
