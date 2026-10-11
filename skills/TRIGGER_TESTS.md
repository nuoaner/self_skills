# Skill Trigger Test Examples

These examples are used to review skill trigger boundaries. Each skill should include examples that should trigger it and examples that should not trigger it.

## ai-coding-discipline

Should trigger:
- "Implement this feature in the existing project and verify the change."
- "Refactor this module carefully without breaking existing behavior."
- "Debug this API issue and improve error handling with tests."

Should not trigger:
- "Rewrite my rough requirement into a Codex prompt."
- "Evaluate whether this architecture is mature."

## ai-coding-paradigm

Should trigger:
- "Evaluate this project's engineering maturity and architecture boundaries."
- "Review the testing, observability, security, and delivery risks of this system."
- "Analyze module responsibilities and implementation tradeoffs."

Should not trigger:
- "Implement this feature directly."
- "Turn this rough Chinese request into an AI coding prompt."

## project-prompt-polisher

Should trigger:
- "Turn this rough requirement into a clearer Codex execution prompt."
- "Rewrite this Chinese task description into an implementation-ready prompt."

Should not trigger:
- "Modify the code directly."
- "Review the architecture quality of this repository."

## wechat-article-image-planner

Should trigger:
- "This is my finalized WeChat article. Plan the cover image and inline illustrations."

Should not trigger:
- "Help me write a WeChat article from scratch."

## app-to-scoop

Should trigger:
- "Create a Scoop manifest from this GitHub Release."

Should not trigger:
- "Explain what Scoop is."

## client-technical-reporting

Should trigger:
- "Prepare a client-facing migration report explaining changes and API integration points."

Should not trigger:
- "Write an internal engineering diary."

## internal-project-doc-standardizer

Should trigger:
- "Standardize this project's README and docs structure."

Should not trigger:
- "Fix a frontend bug."

## market-commercialization-strategist

Should trigger:
- "Review this product's positioning, retention, pricing, and commercialization path."

Should not trigger:
- "Write unit tests."

## project-structure-review

Should trigger:
- "Review whether this repository is ready for delivery or handoff."

Should not trigger:
- "Design a product pricing strategy."

## visual-story-image-director

Should trigger:
- "Turn this portrait photo into an editorial collage while keeping the person recognizable."
- "Create a source-grounded art direction brief for my travel photo."

Should not trigger:
- "Plan the full set of illustrations for this finished WeChat article."
- "Write a generic Codex implementation prompt."

## Experimental Visual Lab (candidate cases; NOT executed auto-trigger tests)

| Entry | Positive trigger candidate | Negative trigger candidate |
|---|---|---|
| ai-image-quality-reviewer | Evaluate defects in this generated marketing image | Render a brand-new image without review |
| ai-poster-art-director | Layout the poster information hierarchy | Explain a shell command |
| brand-visual-system-designer | Define a visual system for a brand campaign | Make a one-off code patch |
| consistent-character-designer | Preserve this mascot across ten scenes | Optimize database indexes |
| creative-reference-analyzer | Analyze why this image reference communicates clearly | Generate an unrelated product specification |
| image-prompt-engineer | Convert a vague image request to a generation brief | Audit Python tests |
| product-visual-designer | Design a product landing-page hero image | Review CI logs |

These are human-readable test specifications, not proof that model routing works. Use the A/B/C protocol for actual performance measurements.
