# self_skills

Personal Codex skills for engineering workflow, project documentation, prompt polishing, and repository review.

This repository collects reusable skills I maintain for my own Codex setup. The focus is practical project work: turning vague requests into executable plans, keeping code changes disciplined, standardizing README/docs, and reviewing repositories before handoff or submission.

## Skills

| Skill | Purpose |
|---|---|
| `ai-coding-discipline` | Enforces disciplined engineering habits while planning, writing, refactoring, or reviewing code. |
| `ai-coding-paradigm` | Helps analyze engineering maturity, code quality, architecture boundaries, testing, delivery flow, and AI-friendly implementation prompts. |
| `internal-project-doc-standardizer` | Standardizes internal project documentation: `README.md`, `docs/`, `agent.md`, status enums, templates, and documentation audits. |
| `project-prompt-polisher` | Rewrites rough Chinese product/UI/frontend requests into implementation-ready prompts for the drone supervision and smart-agriculture platform direction. |
| `project-structure-review` | Audits project repositories against submission and handoff standards: structure, naming, README completeness, dependency notes, tooling disclosure, and architecture materials. |

## Repository Layout

```text
self_skills/
  README.md
  skills/
    ai-coding-discipline/
    ai-coding-paradigm/
    internal-project-doc-standardizer/
    project-prompt-polisher/
    project-structure-review/
```

Each skill follows the standard skill layout:

```text
skill-name/
  SKILL.md
  agents/openai.yaml        # optional UI metadata
  references/               # optional detailed guidance or templates
  scripts/                  # optional helper scripts
```

## Install

Install one skill manually by copying its folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\internal-project-doc-standardizer "$env:USERPROFILE\.codex\skills\internal-project-doc-standardizer"
```

Or clone this repository and copy selected folders into:

```text
C:\Users\<your-user>\.codex\skills
```

Restart Codex after installing or updating skills so the app can rediscover them.

## What Is Not Included

This repository intentionally does not vendor:

- Codex system skills from `.codex/skills/.system`
- Plugin cache skills from `.codex/plugins/cache`
- Third-party skills installed from external repositories

Those skills should stay linked to their original sources. This repository is for skills I want to maintain directly.

## Notes

- Some skills include Chinese project conventions and are intentionally tailored to my workflow.
- `internal-project-doc-standardizer` includes internal documentation templates and a read-only audit script.
- Scripts should be reviewed before running in a new environment.
