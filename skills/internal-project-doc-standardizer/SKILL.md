---
name: internal-project-doc-standardizer
description: Use when organizing, auditing, creating, or synchronizing a project's README and internal docs under a consistent documentation convention. Keep facts traceable; do not trigger on code implementation or client marketing reports.
---

# Internal Project Doc Standardizer

## Overview

Use this skill to make an internal project documentation set consistent, reviewable, and maintainable. `README.md` is the project entry. Add `docs/` and an `agent.md` collaboration log only when the project policy or actual complexity warrants them.

Keep work scoped to documentation unless the user explicitly asks for code changes. Preserve project facts; do not invent owners, dates, APIs, deployment paths, or test results.

## Operation Modes

Choose one mode before editing:

| Mode | Use When | Expected Output |
|---|---|---|
| `audit` | The user asks whether docs are complete or compliant | Findings, risk level, missing files/sections, next actions |
| `generate` | The project lacks standard docs | Create only relevant entry docs; use the full set for larger projects |
| `split` | README is too large or mixes API/database/test details | Move details into docs while keeping README as entry |
| `sync` | Features, APIs, database, deploy, or tests changed | Update README, relevant docs, changelog, and agent.md |
| `repair` | Existing docs have stale, unsafe, or inconsistent content | Fix structure, links, placeholders, status enums, and secret examples |

## Required Workflow

Choose a documentation profile based on project size and the user's stated standard:

- **Lean** (default for small, ordinary repositories): maintain a truthful README, essential usage instructions, and only needed supporting docs.
- **Full** (when the user explicitly requests the internal standard or a regulated/complex handoff): apply the complete documentation template and status vocabulary.

Read the README and only the docs relevant to the change. For auditing or repairing, run the bundled script from the installed Skill directory:

```bash
python <skill-directory>/scripts/audit_docs.py <project-root> --profile lean
python <skill-directory>/scripts/audit_docs.py <project-root> --profile full
```

The script defaults to `full` for backward compatibility; select `lean` explicitly for small repositories. Both profiles remain read-only. Edit relevant documentation only, then report concrete verification and unknown facts. Record Agent collaboration in `agent.md` only when required by project policy or when that file already exists.

## Standard File Set

These files are **available templates**, not mandatory output for every repository. Load and create only what the selected profile and real project require:

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

For small projects, a useful README explains what the software does, how to install/run it, the important limits, and where existing documentation lives. Do not create empty sections or invented owner/status fields to satisfy a template. For full-standard handoffs, include additional ownership, architecture, progress, documentation index, and issue information when grounded in real evidence. Move long API/database/deployment details into relevant docs instead of bloating the README.

## Required Status Enums

For projects using the full internal standard, prefer these status values. For an existing or lean project, preserve its documented conventions unless normalization is explicitly requested:

| Field | Values |
|---|---|
| Project status | `planned`, `in-development`, `joint-debugging`, `testing`, `online`, `maintenance`, `paused`, `archived` |
| Feature status | `pending-planning`, `pending-implementation`, `in-development`, `pending-joint-debugging`, `pending-testing`, `completed`, `deprecated` |
| API status | `pending-design`, `pending-implementation`, `implemented`, `pending-joint-debugging`, `online`, `deprecated` |
| Database status | `pending-design`, `designed`, `migrated`, `online`, `deprecated` |
| Test status | `untested`, `testing`, `passed`, `failed`, `blocked`, `not-applicable` |
| Issue status | `pending`, `in-progress`, `resolved`, `deferred`, `closed` |

## Delivery Template

Use this more detailed report format for substantial audits. For a simple edit, report only changed files, verification and remaining gaps:

```text
Documentation work:
- Mode: audit/generate/split/sync/repair
- Goal:
- Modified files:
- Verification:
- Result:
- Unconfirmed items:
- Next step:
```

## Safety Rules

- Do not write real secrets, tokens, passwords, private keys, certificates, or production connection strings into docs.
- Use `.env.example` for variable names and placeholder examples only.
- If a required field is unknown, write a clear placeholder and list it as an open issue instead of inventing facts.
- Do not leave long-lived placeholder rows without owner and planned time.
- Preserve existing project-specific facts and paths.
- Do not convert README into a full requirements, API, database, deployment, or test document.

## Quality Gate

Before claiming the docs are ready:

- Run the bundled audit script from the skill directory when auditing or repairing an existing project.
- Confirm files required by the **chosen profile** exist; never fail a lean project merely for omitting unrelated templates.
- Confirm the README explains the actual project and matches the selected profile.
- Confirm links in the documentation index point to real files.
- Confirm status labels use the required enums.
- Confirm examples do not contain real secrets.
- Update `agent.md` if required or already in use; do not force one into every repository.

## Common Mistakes

- Updating README but forgetting `docs/requirements.md`, `docs/api.md`, or `docs/changelog.md`.
- Leaving detailed API/database/deploy/test content in README.
- Using non-standard status labels such as `done`, `doing`, or `not-started`.
- Keeping real connection strings or keys in examples.
- Creating an empty `agent.md` merely to satisfy a checklist when the project has no collaboration-log policy.
