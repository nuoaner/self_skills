# Skills Changelog

This changelog tracks changes in this repository. Version files are a repository convention for previously formalized packages; experimental drafts and reference indexes do not require them.

## 2.0.0 - 2026-08-08

### Repository-wide

- Introduced per-skill `VERSION` files with a shared `2.0.0` baseline.
- Added trigger-boundary tests that distinguish implementation, engineering review, and prompt-polishing responsibilities.
- Updated the repository audit to allow Chinese content, detect likely mojibake, support legacy and `interface.*` agent metadata, count skills, validate versions, detect unused references, and detect undocumented scripts.
- Standardized resource hygiene: references must be linked from `SKILL.md`; runtime scripts must be documented; `check_*.py` maintenance scripts follow the repository-wide self-check convention.

### visual-story-image-director

- Added an original visual art direction workflow inspired by external image-generation patterns.
- Focused on scene understanding, identity anchors, communication goals, and visual QA instead of direct style copying.
- Added reusable visual analysis guidance and editorial transformation examples.


## Unreleased - 2026-10-11 (draft PR #4)

- Separated formal, experimental, and reference entries in repository auditing.
- Fixed documentation audit failure exit code.
- Changed Scoop manifest tests to read-only by default and removed automatic uninstall.
- Removed hard-coded shallow nesting and naming bans from project structure review.
- Replaced seven outdated specialized validators with lightweight resource/metadata integrity checks.
- Added repeatable regression tests, CI syntax checks, per-entry audit decisions and an A/B/C agent evaluation protocol.
- **No behavior improvement is claimed until runtime comparisons are measured.**

### Core/Lab/Reference portfolio upgrade

- Adopted an explicit Core (5 provisional candidates) / Lab (12 opt-in entries) / Reference (1 non-installable index) taxonomy driven by `skills/catalog.json`.
- Generated `skills/CATALOG.md`; README files now point to the catalog instead of duplicating mutable skill counts.
- Added 25 labeled positive/negative/task cases for core skills and a score reporter that requires actual run evidence; no fabricated Agent benchmark results.
- Added catalog and evaluation validators with unit tests, and a read-only PowerShell smoke test in CI.
- Clarified ChatGPT-specific metadata for two core skills and tightened key trigger descriptions; aligned Scoop guidance with safe-by-default validation.
- Recorded candidate consolidations without removing any public skill names or files.
