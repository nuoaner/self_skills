# Project Prompt Polisher Patterns

Use this reference when the prompt needs more than the default structure.

## Universal Prompt Skeleton

```text
Please complete the following task based on the current project. First read relevant code and documentation, reuse existing structure, components, utilities, and engineering conventions, and avoid duplicate mechanisms.

Background:
<Known context. Do not invent uncertain facts.>

Goal:
<Specific expected result>

Change scope:
- <File/directory/module/page/API/document>

Requirements:
1. <Executable requirement>
2. <Executable requirement>
3. <Executable requirement>

Constraints:
- Do not modify functionality unrelated to this task.
- Do not break existing routes, permissions, APIs, data structures, style conventions, or user flows.
- If the current request conflicts with the actual project, follow the project facts and explain the mismatch.

Acceptance criteria:
1. <Observable result>
2. <Test/build/screenshot/API/docs check>

Delivery note:
- List modified files.
- Explain how to verify.
- State remaining questions.
```

## UI / Frontend Prompt

Add these dimensions when polishing UI work:

- Target page/component and user scenario.
- Layout hierarchy, spacing, alignment, overflow, and responsive behavior.
- Loading, empty, error, disabled, and permission states.
- Design-system reuse and style boundaries.
- Browser or screenshot verification.

Template:

```text
Improve <page/component> in the current project. Keep existing business logic, API calls, route navigation, and permission checks unchanged. Only adjust the interaction and display requirements explicitly listed here.

Goal:
<What improvement the user should see or feel>

Requirements:
1. Clarify primary, secondary, and dangerous actions to reduce crowding and accidental operations.
2. Handle loading, empty, error, disabled, and permission-denied states.
3. Keep desktop and mobile layouts stable without overlap, misalignment, or unexpected horizontal scrolling.
4. Reuse existing components, style variables, and interaction conventions.

Acceptance criteria:
1. The page renders correctly at target viewport sizes.
2. Existing functionality still works.
3. Screenshots or verification steps are provided.
```

## Backend / API Prompt

Add these dimensions:

- Endpoint, method, request params, response contract.
- Validation, auth, permission, error codes.
- Logging and observability.
- Backward compatibility with existing clients.
- Unit/integration tests.

Template:

```text
Improve <API/service> in the current project while keeping existing client calls compatible. Strengthen validation, error handling, permission boundaries, and verifiability.

Requirements:
1. Define request parameters, required fields, field formats, and defaults.
2. Define success and failure response structures without leaking sensitive information.
3. Cover permission denied, missing parameters, missing resources, status conflicts, and other major failure cases.
4. Preserve existing authentication, logging, and middleware conventions unless a clear defect is found.
5. Add or update tests.

Acceptance criteria:
1. Valid requests return the agreed response.
2. Major failure cases return stable error codes and messages.
3. Tests cover success and failure paths.
```

## Documentation Prompt

Add these dimensions:

- Target docs and source of truth.
- Required sections.
- Stale content removal.
- Links, commands, examples, and screenshots.
- Secret-safe examples.

Template:

```text
Organize <README/docs/documentation> for the current project. Keep project facts accurate and do not invent features, APIs, deployment methods, or owners.

Requirements:
1. Read the existing README, docs, and project structure first. Identify stale, duplicated, or missing content.
2. Add project summary, run instructions, directory structure, core features, configuration notes, documentation index, and next plan.
3. Move detailed requirements, APIs, database, deployment, testing, and changelog content into docs. Keep README as the entry point.
4. Use placeholders in example configuration. Do not write real tokens, passwords, keys, or connection strings.

Acceptance criteria:
1. README works as a project entrance.
2. docs links are valid.
3. No obviously stale statements or real secrets remain.
```

## Testing / Debugging Prompt

Add these dimensions:

- Reproduction steps.
- Expected vs actual behavior.
- Suspected scope.
- Diagnostic commands.
- Regression test and verification.

Template:

```text
Diagnose and fix the following issue in the current project. Do not rewrite broadly. First reproduce or infer the smallest reproduction, identify the root cause, then make the smallest fix.

Symptom:
<Symptom>

Expected result:
<Expected>

Requirements:
1. Inspect relevant logs, call chain, state flow, and boundary conditions.
2. Explain the root cause; do not only patch the visible symptom.
3. Fix the smallest relevant scope and avoid unrelated modules.
4. Add or update regression verification.

Acceptance criteria:
1. The original issue no longer appears.
2. Related normal flows do not regress.
3. Verification command or steps are reported.
```

## Refactor Prompt

Add these dimensions:

- Behavior preservation.
- Module boundaries.
- Migration path.
- Test coverage.
- Rollback risk.

Template:

```text
Refactor <module/file/directory> in small steps to improve maintainability and boundary clarity. External behavior, API contracts, and user flows must remain unchanged.

Requirements:
1. Explain current responsibility mixing or duplication first.
2. Split modules by single responsibility while preserving existing external calls or providing a compatibility layer.
3. Confirm reusable points before deleting duplicated logic.
4. Add or update tests to prove behavior has not changed.

Acceptance criteria:
1. External behavior is unchanged.
2. Module responsibilities are clearer.
3. Tests or build pass.
```

## Automation / Script Prompt

Add these dimensions:

- Input/output contract.
- Dry-run for risky operations.
- Idempotency.
- Logging.
- Error handling.

Template:

```text
Write or improve <script/automation flow> in the current project. Inputs and outputs must be explicit, execution must be repeatable, and errors must be diagnosable.

Requirements:
1. Define input parameters, defaults, output files, or execution results.
2. Provide dry-run or confirmation for operations that modify files, call external services, or delete data.
3. Add logs and error messages so failures identify the failing step.
4. Ensure repeated execution does not cause uncontrolled side effects.

Acceptance criteria:
1. Valid input produces expected output.
2. Invalid input has a clear error message.
3. Run command and verification method are documented.
```

## Handoff Prompt

Use when the polished prompt is for another Codex thread, another AI agent, or another developer.

```text
Take over the following task. Before starting, read the project structure, README/agent.md, and relevant module code. Do not assume missing context.

Goal:
<Goal>

Known facts:
<Facts>

Change:
- <Scope>

Do not change:
- <Boundary>

Acceptance criteria:
- <Criteria>

Delivery requirements:
- List modified files.
- List verification commands and results.
- Mark unfinished or unconfirmed items.
```

## Pressure Examples

### Vague UI

Input:

```text
The buttons on this page are messy. Help me improve it.
```

Expected polishing focus:

- Define primary/secondary/danger action hierarchy.
- Preserve original button behavior.
- Add responsive and overflow checks.

### Vague API

Input:

```text
Improve the login API.
```

Expected polishing focus:

- Define request/response.
- Add validation and failure cases.
- Preserve auth compatibility.
- Add tests.

### Vague Cleanup

Input:

```text
The project is messy. Help me organize it.
```

Expected polishing focus:

- Ask or assume a safe scope.
- Avoid broad destructive cleanup.
- Limit to structure/readme/dependency notes unless explicitly told to refactor code.
