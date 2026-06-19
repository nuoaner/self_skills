# Internal Project Documentation Standard

## 1. Required Files

A standard internal project should include:

```text
README.md
agent.md
docs/standard.md
docs/requirements.md
docs/architecture.md
docs/api.md
docs/database.md
docs/deploy.md
docs/test.md
docs/changelog.md
```

## 2. README Role

`README.md` is the project entrance. It should stay concise and point to detailed docs instead of becoming a full requirements, API, database, deployment, or testing document.

## 3. Document Responsibilities

| File | Responsibility |
|---|---|
| `README.md` | Entry summary, quick start, structure, progress, and doc index |
| `agent.md` | AI/Agent collaboration memory and execution log |
| `docs/requirements.md` | Goals, roles, features, and acceptance criteria |
| `docs/architecture.md` | Tech stack, architecture, structure, and decisions |
| `docs/api.md` | API list, request/response contracts, and errors |
| `docs/database.md` | Tables, fields, relationships, and migrations |
| `docs/deploy.md` | Environment, local run, build, deploy, and rollback |
| `docs/test.md` | Test checklist, test records, defects, and acceptance |
| `docs/changelog.md` | Version changes and completed work |

## 4. Required Status Enums

Use only these status values.

### 4.1 Project Status

- `planned`
- `in-development`
- `joint-debugging`
- `testing`
- `online`
- `maintenance`
- `paused`
- `archived`

### 4.2 Feature Status

- `pending-planning`
- `pending-implementation`
- `in-development`
- `pending-joint-debugging`
- `pending-testing`
- `completed`
- `deprecated`

### 4.3 API Status

- `pending-design`
- `pending-implementation`
- `implemented`
- `pending-joint-debugging`
- `online`
- `deprecated`

### 4.4 Database Status

- `pending-design`
- `designed`
- `migrated`
- `online`
- `deprecated`

### 4.5 Test Status

- `untested`
- `testing`
- `passed`
- `failed`
- `blocked`
- `not-applicable`

### 4.6 Issue Status

- `pending`
- `in-progress`
- `resolved`
- `deferred`
- `closed`

## 5. Minimum README Compliance

Every project README.md must include:

- Project name and one-sentence summary
- Project owner
- Current status
- Local run instructions
- Project structure
- Current feature progress
- Documentation index
- Known issues
- Next steps
- AI / Agent usage prompt

## 6. docs Split Rules

| Content Type | Location |
|---|---|
| Project overview, quick start, documentation index | README.md |
| Detailed requirements, roles, feature acceptance | docs/requirements.md |
| Tech stack, architecture, structure, technical decisions | docs/architecture.md |
| API list, API details, status codes | docs/api.md |
| Tables, fields, relationships, migration records | docs/database.md |
| Runtime environment, env vars, deploy, rollback | docs/deploy.md |
| Test cases, test records, defect records | docs/test.md |
| Version records, feature completion records | docs/changelog.md |
| AI/Agent execution records | agent.md |
