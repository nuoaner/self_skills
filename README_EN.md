<div align="center">

# 🧰 self_skills

**A personal Skills toolbox for Codex / AI Agents**

Turn repeated engineering habits, delivery standards, and workflows into reusable, auditable, versioned Skills.

Engineering · Prompt polishing · Documentation · Repository review · Commercialization · Client delivery · Scoop · WeChat visuals

<p>
  <img src="https://img.shields.io/badge/Skills-9-2563eb?style=flat-square" alt="9 Skills" />
  <img src="https://img.shields.io/badge/Version-v2.0.0-0ea5e9?style=flat-square" alt="Version v2.0.0" />
  <img src="https://img.shields.io/github/last-commit/nuoaner/self_skills?style=flat-square" alt="Last commit" />
  <img src="https://img.shields.io/github/stars/nuoaner/self_skills?style=flat-square" alt="GitHub stars" />
</p>

**[简体中文](README.md) · [English](README_EN.md)**

[Quick Start](#-quick-start) · [Skill Catalog](#-skill-catalog) · [Choose a Skill](#-how-to-choose-a-skill) · [Examples](#-usage-examples) · [Quality System](#-quality-system) · [Repository Structure](#-repository-structure)

<sub>Self-maintained · Chinese-first · Codex-oriented</sub>

</div>

---

## ✨ What is this?

`self_skills` is not a prompt collection. It is a personal Skill repository built around repeatable workflows for real project work.

It captures behaviors that I want AI systems to execute **consistently over time**, including:

- Read the existing implementation before coding, reuse current structures, and avoid creating parallel mechanisms without reason.
- Turn rough task descriptions into implementation-ready instructions for another Agent.
- Review architecture, testing, observability, security, and delivery risk using concrete evidence.
- Keep README, `docs/`, `agent.md`, and project status aligned.
- Check repository structure, documentation, dependencies, and run instructions before delivery.
- Verify time-sensitive market, competitor, and pricing facts before making commercial judgments.
- Convert technical changes into client-facing delivery reports that are understandable and traceable.
- Turn GitHub Releases or official download sources into maintainable Scoop manifests.
- Plan covers, inline illustrations, posters, and generation prompts after a WeChat article is finalized.

> **Core principle:** one Skill should own one clearly defined class of problems. Reuse rules instead of duplicating them, verify instead of guessing, and use scripts when deterministic execution is more reliable than improvisation.

---

## 🧩 Skill Catalog

| Category | Skill | Purpose | Best for | Version | Status |
|---|---|---|---|---|---|
| Engineering | [`ai-coding-discipline`](skills/ai-coding-discipline/SKILL.md) | Disciplined implementation | Features, bug fixes, refactors, and debugging with reuse and incremental verification | `2.0.0` | Stable |
| Engineering | [`ai-coding-paradigm`](skills/ai-coding-paradigm/SKILL.md) | Engineering maturity / architecture review | Module boundaries, testing, observability, security, delivery, and technical risk | `2.0.0` | Stable |
| Prompt | [`project-prompt-polisher`](skills/project-prompt-polisher/SKILL.md) | Implementation-ready prompt polishing | Turning rough requests into executable Codex / Agent tasks | `2.0.0` | Stable |
| Documentation | [`internal-project-doc-standardizer`](skills/internal-project-doc-standardizer/SKILL.md) | Internal documentation standardization | Creating, auditing, splitting, syncing, or repairing README / docs / agent.md | `2.0.0` | Stable |
| Review | [`project-structure-review`](skills/project-structure-review/SKILL.md) | Delivery-readiness repository review | Checking repository structure, README, dependencies, and engineering documentation before handoff | `2.0.0` | Stable |
| Delivery | [`client-technical-reporting`](skills/client-technical-reporting/SKILL.md) | Client-facing technical reporting | Migration, refactor, API replacement, issue diagnosis, and joint-debugging reports | `2.0.0` | Usable |
| Business | [`market-commercialization-strategist`](skills/market-commercialization-strategist/SKILL.md) | Market and commercialization review | Positioning, attraction, retention, competitors, pricing, commercial loops, and maturity | `2.0.0` | Usable |
| Packaging | [`app-to-scoop`](skills/app-to-scoop/SKILL.md) | Scoop manifest creation and maintenance | GitHub Releases, official sites, direct URLs, or existing manifest generation / repair | `2.0.0` | Usable |
| Content | [`wechat-article-image-planner`](skills/wechat-article-image-planner/SKILL.md) | WeChat article visual planning | Covers, inline visuals, posters, placement, and image-generation prompts for finalized articles | `2.0.0` | Usable |

> Trigger conditions and execution rules are defined by each Skill's `SKILL.md`.

---

## 🧭 How to choose a Skill

If you are not sure which Skill should handle a task, use this decision path:

```text
What am I trying to do?
│
├─ Directly modify / debug / refactor code
│  └─ ai-coding-discipline
│
├─ Review engineering quality / architecture / risk without coding
│  └─ ai-coding-paradigm
│
├─ Turn a rough requirement into an executable Codex prompt
│  └─ project-prompt-polisher
│
├─ Create, sync, or govern README / docs / agent.md
│  └─ internal-project-doc-standardizer
│
├─ Check whether a repository is ready for delivery / handoff / acceptance
│  └─ project-structure-review
│
├─ Turn completed technical work into a client-facing report
│  └─ client-technical-reporting
│
├─ Evaluate positioning, user attraction, competitors, pricing, or commercialization
│  └─ market-commercialization-strategist
│
├─ Package a Windows application as a Scoop manifest
│  └─ app-to-scoop
│
└─ Plan visuals for a finalized WeChat article
   └─ wechat-article-image-planner
```

### The three Engineering Skills that are easiest to confuse

```text
project-prompt-polisher
    ↓ owns "make the task clear"

ai-coding-discipline
    ↓ owns "implement the change well and verify it"

ai-coding-paradigm
    ↓ owns "judge engineering design and delivery quality"
```

These responsibilities were explicitly separated in v2 to reduce overlapping triggers.

---

## 🚀 Quick Start

### 1. Clone the repository

```powershell
git clone https://github.com/nuoaner/self_skills.git
cd self_skills
```

### 2. Install one Skill

For example, install `project-prompt-polisher`:

```powershell
Copy-Item -Recurse .\skills\project-prompt-polisher "$env:USERPROFILE\.codex\skills\project-prompt-polisher"
```

### 3. Install all Skills

```powershell
Copy-Item -Recurse .\skills\* "$env:USERPROFILE\.codex\skills"
```

### 4. Update

Pull the latest repository changes:

```powershell
git pull
```

Then copy the Skills you want to update into the Codex Skills directory again.

> Restart Codex after installing or updating Skills so metadata and instructions are reloaded.

---

## 💬 Usage Examples

Skills can be explicitly named or selected automatically from their descriptions. Explicit invocation is useful when you want to guarantee that a specific workflow is used.

### Engineering implementation

```text
Use ai-coding-discipline to implement this feature in the existing project.
Reuse existing structures, keep the change narrow, and verify the result.
```

### Engineering review

```text
Use ai-coding-paradigm to review this repository's architecture boundaries,
testing, observability, security, and delivery risks.
```

### Prompt polishing

```text
Use project-prompt-polisher to rewrite this rough request into a Codex-ready prompt:
Improve the login API without changing the current permission behavior.
```

### Project documentation governance

```text
Use internal-project-doc-standardizer to audit this project's README, docs,
and agent.md, then tell me what is missing or inconsistent.
```

### Scoop packaging

```text
Use app-to-scoop to turn this GitHub Release into a Scoop manifest.
Verify the current release assets first and do not guess hashes or URLs.
```

### Commercialization review

```text
Use market-commercialization-strategist to evaluate the target users, core attraction,
competitor differentiation, pricing logic, and commercial maturity of this product.
Verify current market evidence before making time-sensitive claims.
```

<details>
<summary><strong>More common use cases</strong></summary>

<br />

**Client-facing delivery report**

```text
Use client-technical-reporting to turn this migration and API replacement work
into a client-facing delivery report with follow-up confirmation items.
```

**Pre-handoff repository review**

```text
Use project-structure-review to check whether this repository is ready for
handoff, including README, dependencies, tooling, structure, and run instructions.
```

**WeChat article visual planning**

```text
Use wechat-article-image-planner to plan the cover, three inline illustrations,
and a closing poster for this finalized WeChat article, including placement and prompts.
```

</details>

---

## 🛡️ Quality System

This repository maintains not only Skill content, but also the engineering quality of the Skills themselves.

### Versioning

Each Skill has its own root-level `VERSION` file:

```text
skills/<skill-name>/VERSION
```

Current shared baseline: **`2.0.0`**.

Repository-wide changes are recorded in [`skills/CHANGELOG.md`](skills/CHANGELOG.md).

### Trigger boundary tests

[`skills/TRIGGER_TESTS.md`](skills/TRIGGER_TESTS.md) maintains examples for every Skill:

- `Should trigger`
- `Should not trigger`

The goal is not to test wording quality. It is to reduce **over-triggering, missed triggers, and responsibility overlap** between Skills.

### Repository audit

Run the read-only audit:

```powershell
python .\scripts\audit_skills.py
```

The audit currently checks:

- Skill count and directory naming
- `SKILL.md` frontmatter
- `agents/openai.yaml`
- `VERSION` files and semantic-version format
- `skills/CHANGELOG.md`
- Trigger-test completeness
- References that are not linked from `SKILL.md`
- Runtime scripts that are not documented
- UTF-8 / common mojibake patterns
- Possible real secrets or sensitive fields
- Excessively long `SKILL.md` files

A healthy repository should produce output similar to:

```text
Skills discovered: 9
Version baseline: 2.0.0 (9 skills)
Skill audit passed
```

### Skill self-check scripts

Some Skills include dedicated maintenance checks:

```text
scripts/check_*.py
```

After changing a Skill, run its `scripts/check_*.py` when available, then run the repository-level `scripts/audit_skills.py`.

> `agents/openai.yaml` currently keeps the legacy top-level metadata used by the existing Codex setup. The repository audit accepts both legacy metadata and `interface.*`, allowing a separate future migration without breaking the current environment.

---

## 🗂️ Repository Structure

```text
self_skills/
├─ README.md
├─ README_EN.md
├─ scripts/
│  └─ audit_skills.py
└─ skills/
   ├─ README.md
   ├─ CHANGELOG.md
   ├─ TRIGGER_TESTS.md
   │
   ├─ ai-coding-discipline/
   ├─ ai-coding-paradigm/
   ├─ app-to-scoop/
   ├─ client-technical-reporting/
   ├─ internal-project-doc-standardizer/
   ├─ market-commercialization-strategist/
   ├─ project-prompt-polisher/
   ├─ project-structure-review/
   └─ wechat-article-image-planner/
```

Most Skills follow this layout:

```text
skill-name/
├─ SKILL.md
├─ VERSION
├─ agents/
│  └─ openai.yaml
├─ references/     # optional: knowledge, templates, rules loaded when needed
├─ scripts/        # optional: deterministic checks or helper scripts
└─ assets/         # optional: static assets used in final outputs
```

### File responsibilities

| File / directory | Responsibility |
|---|---|
| `SKILL.md` | Skill entrypoint defining triggers, core workflow, constraints, and resource navigation |
| `VERSION` | Current semantic version of the Skill |
| `agents/openai.yaml` | Agent / UI metadata |
| `references/` | Detailed rules, templates, checklists, and domain knowledge loaded when relevant |
| `scripts/` | Stable, repeatable checks or helper operations suitable for deterministic execution |
| `assets/` | Templates, images, or other final-output resources that are not primary reasoning context |

---

## 🧠 Maintenance Principles

### 1. One Skill should own one clear class of problems

If two Skills repeatedly try to handle the same request, redefine their trigger boundaries instead of adding more keywords to their descriptions.

### 2. `SKILL.md` is a control plane, not a knowledge dump

Keep the core workflow in `SKILL.md`; move large rule sets, templates, and background material into `references/`; use `scripts/` for deterministic operations when possible.

### 3. Do not guess time-sensitive facts

Release versions, download URLs, market prices, competitor status, regulations, and product capabilities can change. When a conclusion depends on current evidence, verify it first.

### 4. Do not copy third-party Skills just for completeness

This repository only maintains Skills that are intentionally owned for long-term use. It is not a mirror of official Skills or third-party plugin caches.

### 5. Every change should leave a verification path

A Skill change should be re-checkable through trigger tests, a self-check script, or the repository audit.

---

## 🚧 Maintenance Boundaries

This repository does **not** aim to maintain:

- Official Codex system Skills such as `.codex/skills/.system`
- Plugin caches such as `.codex/plugins/cache`
- Third-party Skill copies without a clear maintenance reason

Third-party Skills are better referenced at their original source than copied here into an untracked fork.

---

## 📦 Current Version

**v2.0.0** is the current shared Skill baseline. Its main changes include:

- Clear ownership split between coding execution, engineering review, and prompt polishing
- Chinese-content audit compatibility
- Trigger-boundary test cleanup
- Current-evidence gate for market analysis
- Upstream freshness gate for Scoop packaging
- Portable script resolution for the documentation Skill
- Image-tool decoupling for the WeChat visual-planning Skill
- Per-Skill `VERSION` files
- Repository-level `CHANGELOG.md`
- References / scripts resource-hygiene checks

See [`skills/CHANGELOG.md`](skills/CHANGELOG.md) for the complete change history.

---

<div align="center">

**Make repeated good decisions reusable.**

<sub>Built for real project work, not prompt collecting.</sub>

</div>
