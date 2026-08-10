# Skills Changelog

This changelog tracks repository-wide skill versions and behavior changes. Each skill keeps its current semantic version in a root-level `VERSION` file.

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

