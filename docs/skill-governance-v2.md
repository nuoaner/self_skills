# Skill Governance v2

## Purpose

This repository already has a portfolio catalog, Core/Lab/Reference tiers, deterministic audits, routing cases, and an A/B/C evaluation protocol. Governance v2 extends those mechanisms; it does not replace them with a second registry or force every prototype to look production-ready.

## Sources of truth

| Concern | Source of truth |
|---|---|
| Skill inventory and tier | `skills/catalog.json` |
| Human-readable inventory | Generated `skills/CATALOG.md` |
| Skill instructions | Each package's `SKILL.md` |
| Core release version | Each Core package's `VERSION` |
| Agent UI metadata | Each Core package's `agents/openai.yaml` |
| Routing/task cases | `evals/cases.jsonl` |
| Actual A/B/C runs | Private, sanitized run records; never invent evidence |
| Structural health | `python scripts/skill_health.py` |

Do not add a second inventory file that duplicates tier, action, or rationale from `catalog.json`.

## Lifecycle

- **scaffold**: early draft; not installable.
- **library**: reusable reference material; not necessarily a callable Skill.
- **lab**: experimental package; opt-in only.
- **production**: Core candidate with required package structure and checks.
- **deprecated**: retained temporarily for migration; never removed automatically.

The existing Core/Lab/Reference portfolio tiers remain authoritative. Lifecycle labels describe package readiness, not measured model uplift.

## Required contract for new Core skills

1. A concise YAML frontmatter with `name` and a task-specific `description`.
2. A clear activation boundary: when to use and when not to use.
3. Explicit input assumptions and output contract.
4. A workflow with decision points, not generic advice.
5. Constraints, failure handling, and human-confirmation boundaries.
6. References loaded only when needed; every local link must resolve.
7. `VERSION`, `agents/openai.yaml`, and at least two positive, two negative, and one representative task case.
8. A deterministic checker or a documented reason why quality cannot be mechanically checked.
9. Known limitations and manual-review requirements.

Do not retrofit all Lab prototypes merely to satisfy the Core contract. Promote only after evidence and review.

## Evaluation layers

1. **Static integrity**: catalog, metadata, local references, versions, syntax, packaging.
2. **Routing**: positive, negative, and near-neighbor cases; cases are specifications, not scores.
3. **Output contract**: check deliverable shape and required fields with deterministic validators where possible.
4. **Task quality**: blind human rubric against independently written acceptance criteria.
5. **A/B/C evidence**: baseline / previous / candidate with fixed model, tools, context, task data, and repeated runs.

A pass at one layer must not be reported as a pass at a higher layer. Static checks cannot establish that a Skill improves model behavior.

## Maintenance and change policy

- Review Core Skills at least every six months or when a dependency/platform contract changes.
- Review Lab Skills when they are used in a real task or considered for promotion.
- Before changing a Skill, capture its current version and run the existing regression cases.
- A breaking output-contract change requires a major version bump; backward-compatible capability additions use a minor bump; wording or non-behavioral corrections use a patch bump.
- Never auto-delete, merge, rename, or publish a Skill. Prepare a migration map and obtain human approval.
- Store customer data, secrets, raw private traces, and credentials outside the public repository.

## Commands

```bash
python scripts/catalog.py check
python scripts/catalog.py check-docs
python scripts/audit_skills.py
python scripts/eval_cases.py validate
python scripts/skill_health.py
python -m unittest discover -s tests -v
```

Use `python scripts/skill_health.py --json` for machine-readable output and `--strict` when warnings should fail a release gate.

## Phase 2: portfolio intelligence and dependency watch

Phase 2 adds three read-only workflows:

- `python scripts/skill_portfolio_report.py`: lexical scope-overlap candidates, declared complementary relationships, Git-history freshness signals, and summaries from the private usage log.
- `python scripts/dependency_watch.py inventory`: offline inventory of external URLs and imported/runtime packages found in Skill files.
- `python scripts/dependency_watch.py check`: bounded, unauthenticated HTTPS checks against the allowlisted public contracts in `docs/dependency-watch.json`.

The report uses Git last-change dates as a proxy only when no explicit `last_reviewed` metadata exists. Usage evidence is read from the git-ignored `evals/usage-log.csv`; do not commit private logs or raw customer traces. The scheduled workflow stores generated reports as workflow artifacts, not repository commits.

Run locally:

```bash
python scripts/skill_portfolio_report.py
python scripts/skill_portfolio_report.py --format json
python scripts/dependency_watch.py inventory
python scripts/dependency_watch.py validate
python scripts/dependency_watch.py check --strict
```

A changed public contract or unreachable source triggers human review. The watcher does not install packages, update versions, modify Skill instructions, or treat a documentation edit as proof of a breaking change.
