# self_skills

Personal Codex skills for practical engineering workflows, documentation hygiene, prompt hardening, product commercialization review, client-facing reporting, Scoop packaging, and WeChat article image planning.

This repository keeps only self-maintained skills. It is not a mirror of official Codex system skills or third-party plugin-cache skills.

## What This Repository Helps With

- Make AI coding work more disciplined: inspect first, reuse existing structure, define boundaries, implement small verified slices, and avoid broad unverified rewrites.
- Turn rough task requests into implementation-ready prompts for another coding agent.
- Standardize internal project documentation around `README.md`, `docs/`, and `agent.md`.
- Review repository structure before submission, handoff, or acceptance.
- Evaluate products, landing pages, READMEs, and features from a market and commercialization perspective.
- Convert migration, refactor, API replacement, and joint-debugging work into client-facing technical reports.
- Create and maintain Scoop manifests from trusted upstream sources.
- Plan cover art, inline illustrations, posters, and image-generation prompts for finalized WeChat articles.

## Skills

| Skill | Purpose | Best Use |
|---|---|---|
| `ai-coding-discipline` | Disciplined implementation gate | Feature work, bug fixes, refactors, and careful coding prompts |
| `ai-coding-paradigm` | Engineering maturity and architecture review | Code quality, module boundaries, testing, observability, security, delivery, and prompt hardening |
| `app-to-scoop` | Scoop manifest creation and repair | Turn GitHub releases, official download pages, direct URLs, or existing manifests into usable `bucket/app.json` files |
| `client-technical-reporting` | Client-facing technical reports | Summarize migration, refactor, API replacement, issue diagnosis, and joint-debugging work for customers |
| `internal-project-doc-standardizer` | Internal README/docs/agent.md standardization | Create, audit, split, sync, or repair project documentation |
| `market-commercialization-strategist` | Market and commercialization review | Evaluate positioning, user attraction, retention, pricing, landing pages, and commercial readiness |
| `project-prompt-polisher` | Implementation-ready prompt rewriting | Rewrite rough Chinese task requests into clear, executable prompts |
| `project-structure-review` | Repository submission-readiness review | Check structure, naming, README completeness, tooling, dependencies, and architecture documentation |
| `wechat-article-image-planner` | WeChat article visual planning | Plan cover images, inline images, summary posters, placement, and optional imagegen2 prompts |

## Recommended Usage

### Before Coding

Use:

```text
ai-coding-discipline
```

This skill keeps implementation work narrow, evidence-based, and compatible with existing project patterns.

### Reviewing Engineering Quality

Use:

```text
ai-coding-paradigm
```

It evaluates requirements, boundaries, contracts, tests, observability, security, delivery readiness, and AI handoff clarity.

### Standardizing Project Documentation

Use:

```text
internal-project-doc-standardizer
```

It helps maintain a short entry README, detailed `docs/` files, and an `agent.md` collaboration record.

### Creating Scoop Manifests

Use:

```text
app-to-scoop
```

It classifies the source, selects a trustworthy Windows asset, builds a complete manifest, and provides local verification commands.

### Polishing Chinese Task Prompts

Use:

```text
project-prompt-polisher
```

Example:

```text
Use project-prompt-polisher to turn this rough request into a Codex-ready implementation prompt: improve the login API.
```

### Reviewing Commercial Potential

Use:

```text
market-commercialization-strategist
```

It reviews user attraction, ethical retention, market fit, monetization, pricing, trust, support, and readiness to scale.

### Writing Client-Facing Technical Reports

Use:

```text
client-technical-reporting
```

It turns technical work into a structured report that explains what changed, where it changed, how real APIs should be connected, how to diagnose problems, and what needs client confirmation.

### Checking Repository Structure

Use:

```text
project-structure-review
```

It checks whether a project is ready for submission, handoff, review, or acceptance.

## Repository Structure

```text
self_skills/
  README.md
  scripts/
    audit_skills.py
  skills/
    README.md
    TRIGGER_TESTS.md
    ai-coding-discipline/
    ai-coding-paradigm/
    app-to-scoop/
    client-technical-reporting/
    internal-project-doc-standardizer/
    market-commercialization-strategist/
    project-prompt-polisher/
    project-structure-review/
    wechat-article-image-planner/
```

Most skills follow this layout:

```text
skill-name/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
```

## Installation

Clone the repository:

```powershell
git clone https://github.com/nuoaner/self_skills.git
```

Copy one skill into the Codex skills directory:

```powershell
Copy-Item -Recurse .\self_skills\skills\project-prompt-polisher "$env:USERPROFILE\.codex\skills\project-prompt-polisher"
```

Copy all skills:

```powershell
Copy-Item -Recurse .\self_skills\skills\* "$env:USERPROFILE\.codex\skills"
```

Restart Codex after installing or updating skills.

## Quality Checks

Run the read-only repository audit:

```powershell
python .\scripts\audit_skills.py
```

Trigger boundary examples live in:

```text
skills/TRIGGER_TESTS.md
```

When changing a skill, also run that skill's bundled `scripts/check_*.py` script when present, then run the repository audit again.

## Maintenance Boundaries

This repository does not maintain:

- Official Codex system skills, such as `.codex/skills/.system`
- Plugin-cache skills, such as `.codex/plugins/cache`
- Third-party skills copied without a clear maintenance reason

Third-party skills should retain links to their original source instead of being copied here for long-term maintenance.

## Quality Status

| Skill | Status | Notes |
|---|---|---|
| `ai-coding-discipline` | Stable | Lightweight execution gate with supporting references and a self-check script |
| `ai-coding-paradigm` | Stable | Engineering maturity review with scoring checklist, prompt templates, and a self-check script |
| `app-to-scoop` | Usable | Broad Scoop packaging workflow with helper scripts for hashing, archive inspection, and local manifest tests |
| `client-technical-reporting` | Usable | Structured client-facing reporting skill for migration, API replacement, module diagnosis, and follow-up confirmations |
| `internal-project-doc-standardizer` | Stable | Five-mode documentation workflow with templates, an audit script, and a self-check script |
| `market-commercialization-strategist` | Usable | Market-manager lens with a lightweight default mode and a deeper playbook |
| `project-prompt-polisher` | Stable | Prompt hardening workflow with reusable patterns and a self-check script |
| `project-structure-review` | Stable | Read-only repository structure audit with a bundled review script |
| `wechat-article-image-planner` | Usable | Visual planning workflow for finalized WeChat articles with imagegen2-ready prompts |

## English Summary

`self_skills` is a personal Codex skills collection focused on practical engineering workflows. It includes disciplined coding, engineering paradigm analysis, Scoop manifest packaging, client-facing technical reporting, internal documentation standardization, market commercialization strategy, Chinese prompt polishing, project structure review, and WeChat article image planning.
