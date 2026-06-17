---
name: internal-project-doc-standardizer
description: Use when standardizing an internal project README, creating or auditing project documentation, splitting README details into docs, updating agent.md, checking documentation compliance, or handling Chinese requests such as README标准化, 项目文档规范化, 初始化标准文档, 检查文档是否合规, 同步README和docs.
---

# Internal Project Doc Standardizer

## Overview

Use this skill to make an internal project documentation set consistent, reviewable, and maintainable. `README.md` is the entry document, `docs/` contains detailed documents, and `agent.md` records AI/Agent collaboration history.

Keep work scoped to documentation unless the user explicitly asks for code changes. Preserve project facts; do not invent owners, dates, APIs, deployment paths, or test results.

## Operation Modes

Choose one mode before editing:

| Mode | Use When | Expected Output |
|---|---|---|
| `audit` | The user asks whether docs are complete or compliant | Findings, risk level, missing files/sections, next actions |
| `generate` | The project lacks standard docs | Create README, agent.md, and docs templates from references |
| `split` | README is too large or mixes API/database/test details | Move details into docs while keeping README as entry |
| `sync` | Features, APIs, database, deploy, or tests changed | Update README, relevant docs, changelog, and agent.md |
| `repair` | Existing docs have stale, unsafe, or inconsistent content | Fix structure, links, placeholders, status enums, and secret examples |

## Required Workflow

1. Read the target project's `README.md` first if it exists.
2. Read `agent.md` if it exists.
3. Read only the relevant `docs/` files for the selected mode.
4. For audit or repair, run:

```bash
python scripts/audit_docs.py <project-root>
```

5. State the documentation goal and files to change before editing.
6. Edit only the required docs.
7. Update `agent.md` after Agent-assisted documentation work.
8. Report verification evidence, remaining gaps, and next action.

## Standard File Set

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

## README Entry Rules

README must stay short enough to act as a project entrance. It should include:

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

## Required Status Enums

Use only these status values:

| Field | Values |
|---|---|
| Project status | `规划中`, `开发中`, `联调中`, `测试中`, `已上线`, `维护中`, `暂停`, `已归档` |
| Feature status | `待规划`, `待实现`, `开发中`, `待联调`, `待测试`, `已完成`, `已废弃` |
| API status | `待设计`, `待实现`, `已实现`, `待联调`, `已上线`, `已废弃` |
| Database status | `待设计`, `已设计`, `已迁移`, `已上线`, `已废弃` |
| Test status | `未测试`, `测试中`, `通过`, `不通过`, `阻塞`, `不适用` |
| Issue status | `待处理`, `处理中`, `已解决`, `暂不处理`, `已关闭` |

## Delivery Template

Use this response structure after documentation work:

```text
本次文档处理：
- 模式：audit/generate/split/sync/repair
- 目标：
- 修改文件：
- 验证方式：
- 结果：
- 未确认事项：
- 下一步：
```

## Safety Rules

- Do not write real secrets, tokens, passwords, private keys, certificates, or production connection strings into docs.
- Use `.env.example` for variable names and placeholder examples only.
- If a required field is unknown, write a clear placeholder and list it as an open issue instead of inventing facts.
- Do not leave long-lived TODO rows without owner and planned time.
- Preserve existing project-specific facts and paths.
- Do not convert README into a full requirements, API, database, deployment, or test document.

## Quality Gate

Before claiming the docs are ready:

- Run `scripts/audit_docs.py` when auditing or repairing an existing project.
- Confirm required files exist or clearly explain why a file is not applicable.
- Confirm README has the required entry sections.
- Confirm links in the documentation index point to real files.
- Confirm status labels use the required enums.
- Confirm examples do not contain real secrets.
- Confirm `agent.md` records the documentation change.

## Common Mistakes

- Updating README but forgetting `docs/requirements.md`, `docs/api.md`, or `docs/changelog.md`.
- Leaving detailed API/database/deploy/test content in README.
- Using non-standard status labels such as `完成`, `进行中`, or `未开始`.
- Keeping real connection strings or keys in examples.
- Treating `agent.md` as optional after Agent-assisted documentation changes.
