# Modernization audit baseline (2026-10-11)

Base commit: `071a082163d942e270b82e0e89ed2b8521fc21d7`.

## Inventory and status

The main branch contained **18 directories** under `skills/`: 10 Productionized skill packages, 7 Visual Lab prototypes and 1 external reference index. The Visual Lab and index entries lack YAML frontmatter and should not be represented as install-ready packages. They must not be counted as production validation failures merely because they do not carry `agents/openai.yaml` or `VERSION`.

## Decisions by entry

| Entry | Maturity | Decision | Reason |
|---|---|---|---|
| ai-coding-discipline | Production | Simplify | Generic execution rules overlap model capabilities; retain safety and regression checks |
| ai-coding-paradigm | Production | Keep | Engineering maturity review; clarify distinction from implementation |
| project-prompt-polisher | Production | Keep | Distinct Chinese rough-requirement-to-agent-prompt capability |
| internal-project-doc-standardizer | Production | Repair | Audit exit status incorrect, costly fixed documentation scheme |
| project-structure-review | Production | Repair | Script hard-coded shallow folder structure and filename rules |
| client-technical-reporting | Production | Simplify | Seven fixed sections are excessive for smaller reports |
| market-commercialization-strategist | Production | Keep | Verified/inferred/hypothetical claim distinction is valuable |
| app-to-scoop | Production | Repair | Manifest test script performed installations and uninstalls |
| wechat-article-image-planner | Production | Simplify | Avoid double confirmation when direct generation requested |
| visual-story-image-director | Production | Keep | Scene-truth preservation and editorial art direction |
| ai-image-quality-reviewer | Lab | Keep experimental | Review utility overlaps visual skills; validate standalone demand |
| ai-poster-art-director | Lab | Keep experimental | Poster-specific layout may justify specialization |
| brand-visual-system-designer | Lab | Keep experimental | Brand system spans multiple assets |
| consistent-character-designer | Lab | Keep experimental | Character identity preservation is specialized |
| creative-reference-analyzer | Lab | Candidate for merging | Similar analysis stage in visual-story-image-director |
| image-prompt-engineer | Lab | Candidate for merging | Overlaps general visual request structuring |
| product-visual-designer | Lab | Keep experimental | Product truth and conversion require distinct evaluations |
| image-generation-collection | Reference | Keep index only | External pointers, not executable skill |

## Verified defects in baseline

- `audit_docs.py` returned exit code zero even when its JSON `ok` field was false.
- `test-manifest.ps1` automatically installed a package, and when an app name was specified, uninstalled it.
- `review_project.py` rejected directories nested more than two levels and nonconforming names without checking ecosystem conventions.
- Several `check_*.py` scripts required missing old paths/headings; a few flagged all Chinese characters as encoding errors; the WeChat validator expected obsolete imagegen2 terms.
- `TRIGGER_TESTS.md` missed one production skill and all 7 experimental entries.
- Current root auditor applied production criteria to all 18 directories.

## Evidence classes and unresolved validation

Static examination confirms source-code defects, **not improved agent performance**. A/B/C task benchmarks (no skill / old skill / revised skill) need runner access and comparable model configuration. Never claim better tokens, speed, trigger selection or task accuracy from static checks alone. Inspect official specifications afresh before changing requirements. Avoid treating repository policy (such as a VERSION file) as a universal protocol requirement.

## Migration and rollback

Preserve names, directory paths and original assets. Use a separate PR branch. Revert the PR commit to restore legacy behavior. No remote main branch is changed.
