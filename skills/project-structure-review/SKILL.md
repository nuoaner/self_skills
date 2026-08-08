---
name: project-structure-review
description: Use when reviewing whether a repository is ready for delivery, handoff, submission, or acceptance by checking project organization, README quality, dependency/tooling disclosure, naming consistency, and documentation completeness.
---

# Project Structure Review

## Overview

Use this skill to review repository readiness. Treat standards as review criteria, not absolute rules. Judge structure according to project type, technology stack, and delivery goal.

## Review Workflow

1. Identify the project type and delivery goal.
2. Inspect repository structure, README, configuration, dependencies, tooling, and entry points.
3. Apply relevant conventions for the detected ecosystem.
4. Run `scripts/review_project.py <project-root>` when filesystem access is available, then review its findings against the detected ecosystem instead of accepting them mechanically.
5. Report concrete issues with paths, impact, and remediation.
6. Do not modify files unless the user explicitly asks for fixes.

## Review Principles

- Do not reject a project only because it has nested folders; judge whether the structure remains understandable and maintainable.
- Respect ecosystem conventions such as framework routing, package layouts, monorepos, Java package structures, and domain-based organization.
- Treat naming consistency as a maintainability signal, not a universal naming law.
- Prioritize delivery risks: missing documentation, unclear startup process, missing dependencies, broken links, and undocumented architecture decisions.

## README Review

Check whether README explains:

- what the project does and who it serves
- how to install and run it
- important dependencies and versions
- development commands and checks
- architecture or major module relationships
- current status, limitations, or next steps

## Output Format

```markdown
**Conclusion**
Pass / fail / mostly pass, with the main reason.

**Issues**
- [Severity] Specific issue: file or directory path. Impact. Recommendation.

**Remediation**
1. First actionable step.
2. Second actionable step.

**Optional Improvements**
- Suggestions that are helpful but not blocking.
```

The bundled `scripts/review_project.py` script is a read-only first pass. Treat automated findings as evidence to review rather than final judgment.
