# Skill Trigger Test Examples

These examples are used for manual or scripted review of skill trigger boundaries. Each skill should include examples that should trigger it and examples that should not trigger it. The goal is to avoid both over-triggering and missed triggers.

## wechat-article-image-planner

Should trigger:
- "This is my finalized WeChat article. Please plan the cover image and three inline illustrations."
- "The WeChat article draft is final. Please create an image plan and imagegen2 prompts."
- "Generate a WeChat article cover and inline-image prompts from this finished article."

Should not trigger:
- "Help me write a WeChat long-form article from scratch. Do not think about images yet."
- "Generate a generic product poster. It is not for a WeChat article."

## ai-coding-discipline

Should trigger:
- "Implement this feature in a maintainable way. Reuse existing code and verify the change."
- "This module needs refactoring, but first define the boundary and test strategy."
- "Write this code carefully with good error handling, reuse, and maintainability."

Should not trigger:
- "Explain what this code means. No change is needed."
- "Write a short marketing paragraph."

## ai-coding-paradigm

Should trigger:
- "Evaluate this project's engineering maturity and architecture boundaries."
- "How are the tests, observability, and security posture of this system?"
- "Analyze the module design and implementation tradeoffs."

Should not trigger:
- "Translate this README into English."
- "Generate a product promotion poster."

## app-to-scoop

Should trigger:
- "Use app-to-scoop to turn this GitHub Release into a Scoop manifest."
- "Package this official download page as bucket/app.json with checkver and autoupdate."
- "This Scoop manifest fails with Hash check failed. Help me repair it."

Should not trigger:
- "Explain what Scoop is."
- "Help me write a winget manifest."

## client-technical-reporting

Should trigger:
- "Prepare a client-facing technical report explaining what changed, how it was migrated, and where real APIs should be connected later."
- "Turn this joint-debugging progress into a delivery note the customer can understand."
- "Write a migration summary for the client, including issue diagnosis and follow-up confirmation items."

Should not trigger:
- "Write an informal internal daily report."
- "Improve the parameter validation of this login API."

## internal-project-doc-standardizer

Should trigger:
- "Standardize this project's README and move detailed content into docs."
- "Check whether the project documentation complies with our internal standard."
- "Initialize a standard README, docs folder, and agent.md for this project."

Should not trigger:
- "Fix a frontend button alignment bug."
- "Write a sales conversion analysis."

## market-commercialization-strategist

Should trigger:
- "Review this product from a market-manager perspective. How can it attract users and form a commercial loop?"
- "Evaluate whether this feature is suitable for commercialization, pricing, and promotion."
- "Improve the landing page's user attraction, retention, and conversion path."

Should not trigger:
- "Write unit tests."
- "Turn the project directory structure into a tree diagram."

## project-prompt-polisher

Should trigger:
- "Turn this rough requirement into a clearer Codex execution prompt."
- "This prompt is too loose. Polish it into a version another agent can execute."
- "Rewrite my Chinese task description into an implementation-ready prompt with acceptance criteria."

Should not trigger:
- "Implement this feature directly. No prompt rewriting is needed."
- "Explain what prompt engineering means."

## project-structure-review

Should trigger:
- "Review whether this project structure meets delivery standards."
- "Before submission, check the directory structure, README, dependency documentation, and architecture diagram."
- "Standardize this repository structure for handoff or review."

Should not trigger:
- "Write an API endpoint."
- "Design a product commercialization roadmap."
