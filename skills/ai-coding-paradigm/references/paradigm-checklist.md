# AI Coding Paradigm Checklist

Score each dimension from 0 to 2.

```text
0 = missing or risky
1 = partially present
2 = clear, usable, and verifiable
```

## 1. Requirement and Boundary Clarity

Look for:

- Clear target user, workflow, and expected outcome.
- Explicit in-scope and out-of-scope boundaries.
- No mixing of unrelated features.
- Clear acceptance criteria.

Red flags:

- "Optimize it while you are here."
- No owner for edge cases.
- Ambiguous terms such as "improve", "optimize", or "handle this" without target behavior.

## 2. Single Responsibility and Module Cohesion

Look for:

- Each file/module has one primary reason to change.
- UI, API, state, formatting, and persistence are not tangled.
- Shared utilities are reused instead of duplicated.

Red flags:

- Large files with many unrelated responsibilities.
- Components performing network, permission, formatting, and layout logic together.
- Copy-pasted logic across modules.

## 3. Dependency Direction and Layering

Look for:

- Clear direction between UI, service, domain, infrastructure, and config layers.
- No circular dependencies.
- External services isolated behind adapters.

Red flags:

- Low-level utilities importing page components.
- Business logic depending on UI state shape.
- Environment-specific code spread across modules.

## 4. Interface and Data Contracts

Look for:

- Request/response fields are explicit.
- Error format is stable.
- Enums and status values are documented.
- Compatibility expectations are clear.

Red flags:

- Magic strings and implicit payloads.
- Backend and frontend interpret the same field differently.
- Mock data shape differs from real API shape.

## 5. Validation and Error Handling

Look for:

- Input validation at boundaries.
- Clear failure modes.
- Useful error messages without leaking secrets.
- Recovery or fallback strategy when needed.

Red flags:

- Only happy path tested.
- Catch-all errors hide root causes.
- Permission and empty states are treated as unexpected.

## 6. Testability and Regression Protection

Look for:

- Unit, integration, or E2E checks for critical paths.
- Regression test for fixed bugs.
- Manual verification steps when automation is unavailable.

Red flags:

- "Looks fine" with no command or evidence.
- Tests require production services.
- No clear way to verify rollback safety.

## 7. Observability and Diagnosability

Look for:

- Logs identify request, module, operation, and failure reason.
- Important states can be inspected.
- Errors are traceable across frontend/backend boundaries.

Red flags:

- `print()` or console logs without context.
- Silent failures.
- No distinction between user error, network error, and server error.

## 8. Security, Permission, and Data Safety

Look for:

- Auth and permission checks at the right boundary.
- Sensitive data excluded from logs and docs.
- Environment variables handled safely.
- Dangerous operations require confirmation or dry-run.

Red flags:

- Secrets in README, examples, logs, or code.
- Frontend-only permission enforcement.
- Broad file deletion or data mutation without safeguards.

## 9. Delivery, Rollback, and Environment Readiness

Look for:

- Build/test/deploy commands documented.
- Migration and rollback path clear.
- Environment-specific config isolated.
- Joint debugging and acceptance needs identified.

Red flags:

- Works only on one developer machine.
- No rollback for schema/API changes.
- Deployment relies on undocumented manual steps.

## 10. AI Executability and Handoff Clarity

Look for:

- Another agent can identify files, scope, constraints, and verification.
- Prompt includes non-regression requirements.
- Output expectations are explicit.

Red flags:

- "Help me optimize everything."
- No target files or modules.
- No acceptance criteria.

## Score Interpretation

| Score | Meaning | Action |
|---:|---|---|
| 0-7 | High risk | Clarify boundaries and contracts before implementation |
| 8-14 | Basic but fragile | Fix top risks before delivery |
| 15-18 | Good | Improve observability, tests, and handoff |
| 19-20 | Strong | Ready for delivery or scalable iteration |
