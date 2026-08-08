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
