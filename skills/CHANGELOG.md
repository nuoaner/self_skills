# Skills Changelog

This changelog tracks repository-wide skill versions and behavior changes. Each skill keeps its current semantic version in a root-level `VERSION` file.

## 2.0.0 - 2026-08-08

### Repository-wide

- Introduced per-skill `VERSION` files with a shared `2.0.0` baseline.
- Added trigger-boundary tests that distinguish implementation, engineering review, and prompt-polishing responsibilities.
- Updated the repository audit to allow Chinese content, detect likely mojibake, support legacy and `interface.*` agent metadata, count skills, validate versions, detect unused references, and detect undocumented scripts.
- Standardized resource hygiene: references must be linked from `SKILL.md`; runtime scripts must be documented; `check_*.py` maintenance scripts follow the repository-wide self-check convention.

### ai-coding-discipline

- Narrowed the skill to direct implementation, modification, debugging, and refactoring work.
- Delegated prompt-only rewriting to `project-prompt-polisher`.
- Retained the execution checklist and pressure scenarios as explicit supporting resources.
- Removed the obsolete prompt template after prompt ownership moved to `project-prompt-polisher`.

### ai-coding-paradigm

- Narrowed the skill to engineering maturity, architecture, delivery, and risk reviews.
- Removed prompt-hardening as a primary responsibility.
- Retained the engineering review checklist as the supporting review reference.
- Removed obsolete implementation-prompt templates that duplicated `project-prompt-polisher`.

### app-to-scoop

- Added a freshness gate for current releases, download assets, version numbers, URLs, and upstream packaging facts.
- Preserved the existing source-selection, manifest, autoupdate, troubleshooting, and helper-script workflow.

### client-technical-reporting

- Adopted the v2 versioning and repository audit baseline without changing its client-report contract.

### internal-project-doc-standardizer

- Clarified that bundled audit scripts must be resolved from the skill directory rather than the target project's current working directory.
- Adopted the v2 resource and version audit baseline.

### market-commercialization-strategist

- Added an evidence gate that separates verified facts, inferences, and hypotheses.
- Required current research before material claims about competitors, pricing, market size, launches, regulation, or trends.

### project-prompt-polisher

- Established this skill as the single owner for converting rough task requests into implementation-ready Codex or agent prompts.
- Adopted the v2 resource and version audit baseline.

### project-structure-review

- Reframed repository review around ecosystem conventions instead of rigid universal nesting and naming rules.
- Kept automated structure checks as evidence rather than absolute architectural truth.

### wechat-article-image-planner

- Removed the hard dependency on a fixed local `imagegen2` path.
- Made live image generation capability-driven and retained prompt-only output as a portable fallback.
