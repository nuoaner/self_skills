---
name: internal-project-doc-standardizer
description: Use when standardizing an internal project README, creating or auditing project documentation, splitting README details into docs, updating agent.md, checking documentation compliance, or handling Chinese requests such as README标准化, 项目文档规范化, 初始化标准文档, 检查文档是否合规, 同步README和docs.
---

# Internal Project Doc Standardizer

## Overview

Use this skill to make project documentation follow the internal split-document standard: `README.md` is the entry point, `docs/` holds details, and `agent.md` records AI/Agent collaboration history.

Keep work scoped to documentation unless the user explicitly asks for code changes.

## Workflow

1. Read the target project's `README.md` first if it exists.
2. Read `agent.md` if it exists.
3. Read only the relevant `docs/` files for the task.
4. Run the audit script when checking an existing project:

```bash
python scripts/audit_docs.py <project-root>
```

5. Decide the operation:
   - `audit`: report missing files, missing README sections, invalid status values, unresolved placeholders, and secret risks.
   - `generate`: create the standard documentation set from templates.
   - `split`: move detailed requirements, API, database, deployment, test, or changelog content out of README into `docs/`.
   - `sync`: after feature/API/database/deploy/test changes, update README, relevant docs, changelog, and `agent.md`.
6. Before edits, state the goal, files to change, and each file's role.
7. After edits, update `agent.md` with request, changed files, actions, verification, result, open issues, and next step.

## Standard Files

Use these references as templates or source rules:

| File | Purpose |
|---|---|
| `references/readme-template.md` | Standard project entry README |
| `references/agent-template.md` | Agent collaboration record |
| `references/standard.md` | Required fields, status enums, split rules |
| `references/requirements-template.md` | Requirements, goals, roles, features, acceptance |
| `references/architecture-template.md` | Tech stack, architecture, structure, decisions |
| `references/api-template.md` | API list, details, params, examples, error codes |
| `references/database-template.md` | Tables, fields, relationships, migrations |
| `references/deploy-template.md` | Environment, variables, local run, build, deploy, rollback |
| `references/test-template.md` | Test checklist, records, acceptance conditions |
| `references/changelog-template.md` | Version changes, completed features, fixes |

## README Rules

README must remain an entry document. It should include:

- Project name and one-sentence summary
- Project basic information and owner fields
- Current project status
- Project overview, goals, and boundaries
- Quick start and local run commands
- Project structure
- Current feature progress
- Documentation index
- Known issues and next plan
- AI / Agent usage prompt

Move detailed requirements, API, database, deployment, testing, and changelog content into `docs/`.

## Required Enums

Use only these status values:

| Field | Values |
|---|---|
| Project status | `规划中`, `开发中`, `联调中`, `测试中`, `已上线`, `维护中`, `暂停`, `已归档` |
| Feature status | `待规划`, `待实现`, `开发中`, `待联调`, `待测试`, `已完成`, `已废弃` |
| API status | `待设计`, `待实现`, `已实现`, `待联调`, `已上线`, `已废弃` |
| Database status | `待设计`, `已设计`, `已迁移`, `已上线`, `已废弃` |
| Test status | `未测试`, `测试中`, `通过`, `不通过`, `阻塞`, `不适用` |
| Issue status | `待处理`, `处理中`, `已解决`, `暂不处理`, `已关闭` |

## Safety

- Do not write real secrets, tokens, passwords, private keys, or certificates into docs.
- Use `.env.example` for variable names and placeholder examples only.
- If a required field is unknown, write a clear placeholder and list it as an open issue instead of inventing facts.
- Do not leave long-lived TODO rows without owner and plan time.
- Preserve existing project-specific facts and paths; standardize structure around them.

## Common Mistakes

- Expanding README into a full requirements or API document.
- Updating README but forgetting `docs/requirements.md`, `docs/api.md`, or `docs/changelog.md`.
- Using non-standard status labels such as `完成`, `进行中`, or `未开始`.
- Keeping real connection strings or keys in examples.
- Treating `agent.md` as optional after an Agent-assisted documentation change.
