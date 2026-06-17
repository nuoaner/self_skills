---
name: project-structure-review
description: Audit and normalize team project repositories against submission standards for project structure, folder and file naming, README completeness, dependency/version documentation, lint/tooling disclosure, and architecture diagrams. Use when Codex is asked to check whether a project follows team conventions, prepare a project for application/submission/review, generate a remediation checklist, or help standardize a repository before handoff.
---

# Project Structure Review

## Overview

Use this skill to review a team project before submission, application, handoff, or internal acceptance. Treat the project checklist as the baseline standard: simple structure, consistent naming, and a complete README.

## Review Workflow

1. Identify the project root from the user request or current workspace.
2. Run `scripts/review_project.py <project-root>` when filesystem access is available.
3. Read the script output and inspect key files when needed, especially `README*`, package/build config files, and top-level folders.
4. Report results in Chinese unless the user asks otherwise.
5. Lead with a pass/fail summary, then list issues by severity, then give concrete remediation actions.
6. Do not modify files unless the user explicitly asks for fixes.

## Baseline Standard

### Project Structure

Require:

- Folder nesting should be at most two levels below the project root, excluding common generated/vendor folders.
- The root directory should contain at least one engineering configuration file.
- The root directory should contain at least one likely program entry file.
- The root directory should contain a README file.

Common engineering configuration files include `package.json`, `vite.config.*`, `tsconfig.json`, `pyproject.toml`, `requirements.txt`, `pom.xml`, `build.gradle`, `Cargo.toml`, `go.mod`, `.eslintrc*`, `.prettierrc*`, `Dockerfile`, `docker-compose.yml`, and CI config files.

Common entry files include `main.*`, `index.*`, `app.*`, `server.*`, `manage.py`, `Application.java`, `Program.cs`, `cmd/*/main.go`, and frontend entry files under `src`.

### Naming Rules

Apply these rules:

- Folder names should be short, meaningful, and match their responsibility, such as `src`, `docs`, `config`, `assets`, `tests`, `scripts`, `public`, `server`, `client`, or domain names.
- Folder names should not use connector symbols such as `-` or `_` unless the project ecosystem strongly requires them.
- Non-document file names should use English only.
- Code file connector symbols should use underscores, for example `user_service.py`.
- Non-code file connector symbols should use hyphens, for example `project-plan.md`.

Use judgment for ecosystem conventions. Do not flag standard generated or dependency paths such as `node_modules`, `.git`, `dist`, `build`, `target`, `.venv`, `__pycache__`, `.next`, `.nuxt`, `.idea`, `.vscode`, or `coverage`.

### README Requirements

Require README content to cover:

- Project introduction: what the project does, target users/scenarios, and core value.
- Project management tools: package manager, build tool, task runner, framework CLI, or collaboration workflow.
- Syntax/lint checking tools: ESLint, Prettier, TypeScript, Ruff, Black, Checkstyle, SpotBugs, pytest, unit test/lint commands, or equivalent.
- Important dependencies and versions: key frameworks/libraries, runtime versions, database or middleware versions.
- Architecture diagram: an image reference, Mermaid diagram, PlantUML diagram, or a clear architecture section.

## Severity Guidance

- High: missing README, missing root config, missing entry point, or folder nesting beyond two levels in source-owned code.
- Medium: README missing required sections, mixed naming conventions, non-English names in non-document files, or no architecture diagram.
- Low: folder names are vague, dependency versions are incomplete, or README has weak project-management/tooling descriptions.

## Output Format

Use this structure, translated into Chinese:

```markdown
**Conclusion**
Pass / fail / mostly pass, with the main reason.

**Issues**
- [Severity] Specific issue: file or directory path. Impact. Recommendation.

**Remediation**
1. First actionable step.
2. Second actionable step.

**Optional Improvements**
- Suggestions that are helpful but not blocking for submission.
```

When the user asks for direct fixes, make targeted edits only after confirming the affected files and avoiding unrelated rewrites.

## Script

Use:

```bash
python path/to/project-structure-review/scripts/review_project.py <project-root>
```

The script performs a read-only audit and prints Markdown-style findings. Treat script results as a first pass, then apply human judgment for framework-specific conventions.
