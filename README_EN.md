# self_skills

**A personal/team-first skill portfolio, published only after validation.** Keep distinct expertise, tools, assets, and reliable acceptance criteria; avoid teaching capable agents universal common sense.

## Portfolio

The [generated catalog](skills/CATALOG.md) is the canonical inventory, backed by [catalog.json](skills/catalog.json). Earlier repository documentation used a 10-production / 7-visual-lab / 1-reference baseline; this revision reclassifies entries by *actual expected use*:

- **Core:** priority-maintained, installable candidates for repeat personal/team workflows. Core does *not* mean model improvement was measured.
- **Lab:** opt-in experiments, overlap/merge candidates, and legacy packages under review. Some lab sketches lack valid frontmatter and **must not be installed**.
- **Reference:** external pointers and research notes; not a skill package.

See [portfolio governance](docs/portfolio-policy.md) for promotion, retirement, compatibility, and rollback criteria.

## Quick checks

```bash
git clone https://github.com/nuoaner/self_skills.git
cd self_skills
python scripts/catalog.py list
python scripts/catalog.py check
python scripts/catalog.py check-docs
python scripts/audit_skills.py
python scripts/eval_cases.py validate
python -m unittest discover -s tests -v
```

These commands test structural integrity and deterministic behavior only, **not agent success**. For no-skill / current-skill / revised-skill trials see the [evaluation guide](evals/README.md).

## Install and publish

Choose one individual Skill folder from the catalog. Install into your Codex environment using its supported skill directory, or create/upload a **single** Skill through ChatGPT's current Skills UI. Installation procedures and capacity limits depend on platform; see [verified compatibility notes](docs/platform-compatibility-2026-10-11.md).

Historical `skills/<name>` paths and public invocation names remain intact while usage and migration evidence are gathered. Do not bulk-install lab prototypes or package the whole repository as one ChatGPT Skill.

## Contribution policy

Require differentiated user value, accurate triggers, repeatable verification, and a clear failure/rollback boundary. Put long background references and reusable assets outside the entrypoint; use scripts for deterministic fragile tasks. Do not add folders merely to satisfy a template. Review third-party provenance and license constraints, and never publish credentials or private project data.

Modernization changes are reviewed in [draft PR #4](https://github.com/nuoaner/self_skills/pull/4); there is no direct write to `main`. See the [changelog](skills/CHANGELOG.md).
