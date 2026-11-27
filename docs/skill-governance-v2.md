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

### Usage log field conventions

The private `evals/usage-log.csv` is manual evidence, not telemetry. Use the template in `evals/usage-log.template.csv` and keep the real log local (it is git-ignored).

| Field | Accepted meaning |
|---|---|
| `task_completed` | `yes`, `no`, `partial`, or `unknown` |
| `benefit_over_no_skill` | `better`, `same`, `worse`, or `unknown`; compare against a real baseline when possible |
| `quality_score` | Optional human score from 0 to 5 |
| `friction_category` | `none`, `trigger`, `quality`, `tool`, `latency`, or `other` |
| `duration_s` / `tool_calls` | Optional observed values, not estimates |
| `safety_violations` | Non-negative count; describe the incident in a sanitized evidence record |
| `redacted_evidence_ref` | Reference to sanitized output/review evidence; never paste secrets or customer data |

Directional recommendations require at least five records for that Skill. Even then, the report is a triage aid, not an automatic promotion or retirement decision. No records means usage is unknown; manual logging cannot establish that a Skill is rarely used unless the observation process is known to be complete.

### Report interpretation

- Overlap detection uses multilingual lexical TF-IDF similarity over descriptions, headings, and Skill instructions. The default candidate threshold is 0.18; scores are not semantic duplicate probabilities.
- The repository records known relationships in `docs/skill-relations.json`. For example, course-specific PPT authoring and generic PPTX engineering QA are declared complementary.
- Freshness uses `manifest.json:last_reviewed` when present. Otherwise it falls back to the latest Git change date, explicitly labeled as a proxy. Default review intervals are 180 days for Core and 365 days for Lab.
- Remote dependency checks use only allowlisted HTTPS sources in `docs/dependency-watch.json`. Missing contract phrases, changed version signals, or unreachable sources require human review; the workflow never updates dependencies.
- Scheduled reports are uploaded as GitHub Actions artifacts and retained for 30 days. They are not committed back into the repository.
