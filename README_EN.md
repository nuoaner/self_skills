<div align="center">

# self_skills

**Give agents meaningful expertise, not longer checklists.**

A focused collection of skills for personal workflows and team delivery. We retain specialized knowledge, repeatable tools and verifiable deliverables, then publish reusable capabilities after evaluation.

[简体中文](README.md) · [English](README_EN.md) · [Find a skill](#find-the-right-skill) · [Full directory](skills/CHOOSING.md) · [Quality evidence](#what-quality-means-here)

</div>

---

## Find the right Skill

**Start with your job, not a list of technical skill names.** These five are priority-maintained **Core candidates**; Core does not mean an A/B/C model benchmark has already passed.

| What you need to do | Try this Skill | Why it helps | What you get |
|---|---|---|---|
| **Turn an unclear request into a task for Codex or another agent** | [Prompt Polisher · `project-prompt-polisher`](skills/project-prompt-polisher/SKILL.md) | Defines scope, non-regression boundaries and acceptance without quietly expanding the request | Copy-ready implementation brief |
| **Clean up project READMEs and documentation** | [Doc Standardizer · `internal-project-doc-standardizer`](skills/internal-project-doc-standardizer/SKILL.md) | Keeps real project facts, repairs gaps and uses a lightweight profile for small repositories | Documentation changes and a traceable audit |
| **Package a Windows app for Scoop** | [Scoop Packager · `app-to-scoop`](skills/app-to-scoop/SKILL.md) | Finds trustworthy release assets and configures versions, hashes and launchers | Scoop manifest, verification and open questions |
| **Turn an existing photo into a story-led visual** | [Visual Story Director · `visual-story-image-director`](skills/visual-story-image-director/SKILL.md) | Preserves subject identity and scene facts while art-directing the layout and mood | Source diagnosis, edit/generation brief and visual QA; generation when supported |
| **Plan visuals for a finished WeChat article** | [Article Image Planner · `wechat-article-image-planner`](skills/wechat-article-image-planner/SKILL.md) | Connects illustrations to article sections instead of adding generic filler images | Cover/inline plan, precise placements and prompts |

> If you're only fixing a routine bug or asking a simple question, try the base agent first. A Skill should add something the model would otherwise lack.

### Copy-and-try prompts

<details><summary>Prompt Polisher</summary>

```text
Use project-prompt-polisher. Rewrite this vague bug description as an executable Codex task.
Define scope, regression protection and acceptance criteria; do not implement it:
"Chinese input does not work in the motion editor text field."
```

</details>

<details><summary>Doc Standardizer</summary>

```text
Use internal-project-doc-standardizer to review this repo's README and docs.
Use a proportionate documentation profile and report unverified details instead of inventing facts.
```

</details>

<details><summary>Scoop Packager</summary>

```text
Use app-to-scoop to create a Windows Scoop manifest from this official release: <URL>.
Verify hashes when possible, list unresolved fields, and do not install or uninstall anything.
```

</details>

<details><summary>Visual Story Director</summary>

```text
Use visual-story-image-director to build an editorial travel-memory concept from my image.
Preserve the people and observable scene facts; explain composition and visual QA.
```

</details>

<details><summary>Article Image Planner</summary>

```text
Use wechat-article-image-planner to plan a cover and inline illustrations for this final article.
State exactly where each image belongs, why it is needed, and a distinct image prompt.
```

</details>

## More to explore

The repository also holds **12 Lab entries** for experimentation, overlap reviews and possible consolidation. Some are not install-ready.

| Area | Experiments |
|---|---|
| **Engineering** | [Architecture review](skills/ai-coding-paradigm/SKILL.md), [Coding discipline](skills/ai-coding-discipline/SKILL.md), [Repository handoff review](skills/project-structure-review/SKILL.md) |
| **Brand and visuals** | [Character consistency](skills/consistent-character-designer/SKILL.md), [Brand systems](skills/brand-visual-system-designer/SKILL.md), [Posters](skills/ai-poster-art-director/SKILL.md), [Product visuals](skills/product-visual-designer/SKILL.md) |
| **Visual analysis** | [Reference analysis](skills/creative-reference-analyzer/SKILL.md), [Image QA](skills/ai-image-quality-reviewer/SKILL.md), [Image prompts](skills/image-prompt-engineer/SKILL.md) |
| **Business and reporting** | [Commercialization](skills/market-commercialization-strategist/SKILL.md), [Client technical reports](skills/client-technical-reporting/SKILL.md) |

The [image-generation collection](skills/image-generation-collection/SKILL.md) is an external **reference index**, not an installable Skill. [See the complete directory with scope and deliverables →](skills/CHOOSING.md).

## What quality means here

We distinguish reliable packaging and checks from **actual agent improvement**.

| Layer | Verifiable current state | Evidence |
|---|---|---|
| **Engineering and safety** | Previous baseline passed structural, Python regression and read-only Windows checks; consult CI for the latest run | [GitHub Actions](https://github.com/nuoaner/self_skills/actions/workflows/skill-integrity.yml) and [test code](tests/) |
| **Cases** | **35 labeled** English/Chinese positive, negative and representative cases; not agent performance results | [Case registry](evals/cases.jsonl) and [method](evals/README.md) |
| **Real A/B/C agent outcomes** | **Not measured yet**. We do not publish invented accuracy, time or token improvements | [Evaluation limitations](evals/README.md) |
| **Portfolio** | 5 Core candidates / 12 Labs / 1 Reference; names remain compatible while evaluating consolidation | [Catalog](skills/catalog.json), [governance](docs/portfolio-policy.md) |

Core means **priority-maintained and structurally installable**, not independently certified or empirically superior.

## Getting started

### Install a single Skill in Codex (Unix example)

```bash
git clone https://github.com/nuoaner/self_skills.git
cd self_skills
mkdir -p ~/.codex/skills
cp -R skills/project-prompt-polisher ~/.codex/skills/
```

Check the appropriate installation path for your installed Codex version; do not bulk-install the whole `skills/` tree.

### Prepare a single-skill ZIP for ChatGPT

If your ChatGPT workspace supports custom Skills, package just one Core Skill and upload it through the available Skills UI.

```bash
python scripts/package_selected.py project-prompt-polisher --output ./skill.zip
```

This command **only creates the ZIP**; it does not install, upload or alter your workspace.

### Run deterministic checks

```bash
python scripts/catalog.py check
python scripts/audit_skills.py
python scripts/eval_cases.py validate
python -m unittest discover -s tests -v
```

Passing structural checks does not establish Agent benefit. See the [phase-two opt-in A/B/C pilot](evals/PILOT.md).

## Maintenance and public use

Our progression is **personal/team use → Lab exploration → Core maintenance → evidence-backed public release**. Generic advice should not be packaged as a Skill unless it adds domain-specific value. Merge/retirement candidates retain their existing names until migration is proven; see [portfolio governance](docs/portfolio-policy.md).

**Licensing:** This public repository does not currently declare a repository-wide open-source license. Do not assume its contents are freely redistributable or licensed for commercial re-use. External references retain their original licenses.

For feedback, submit a redacted use case, expected result and actual outcome to [Issues](https://github.com/nuoaner/self_skills/issues).

<div align="center">

*Keep what helps. Test what matters.*

</div>
