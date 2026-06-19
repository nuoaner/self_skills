# AI Coding Paradigm Prompt Templates

Use these templates when the user wants an AI-executable engineering prompt rather than a review report.

## Feature Implementation Prompt

```text
Implement <feature> in the current project. Before editing, read the relevant README/agent.md, existing module structure, routes, APIs, state management, and component conventions. Prefer existing implementation paths and avoid duplicate mechanisms.

Goal:
<Expected user behavior or business result>

Scope:
- Change:
- Do not change:

Engineering constraints:
- Keep existing architecture, code style, permissions, routes, API contracts, and data structures compatible unless explicitly required below.
- Define module boundaries and data contracts before implementing details.
- Do not introduce broad refactors unrelated to this goal.

Implementation requirements:
1. <Concrete implementation step>
2. <Error, empty-state, permission, or boundary handling>
3. <Logging, observability, or error messaging>

Verification requirements:
- Run <test/build/check command>.
- Verify the success path and key failure paths.
- Report modified files, verification results, risks, and unconfirmed items.
```

## Refactor Prompt

```text
Refactor <module/directory/file> in small steps to reduce coupling, clarify responsibilities, and improve maintainability. External behavior, API contracts, routes, permissions, and user flows must remain unchanged.

Before editing:
1. List current responsibility mixing and dependency issues.
2. Identify reusable existing components, utilities, or services.
3. Propose the smallest split or repair plan.

Implementation requirements:
- Make only verifiable small adjustments.
- Preserve compatibility layers or migration paths.
- Do not delete entry points that may still be used.

Acceptance:
- Existing behavior does not regress.
- Module responsibilities are clearer.
- Tests, build, or manual verification pass.
```

## API Contract Prompt

```text
Clarify and strengthen the engineering contract for <API/service>, focusing on stable frontend-backend integration, diagnosable errors, and maintainability.

Requirements:
1. Specify endpoint, method, request fields, response fields, error codes, pagination, filtering, and sorting rules.
2. Specify authentication, permissions, validation, and exception scenarios.
3. Check whether mock data matches the real API shape.
4. Update related documentation or type definitions.
5. Add or describe verification.

Output:
- Contract summary
- Modified files
- Verification result
- Items still requiring client/backend/frontend confirmation
```

## Delivery Readiness Prompt

```text
Review whether the current project/module is ready for joint debugging, acceptance, or release.

Check:
1. Functional boundaries and acceptance criteria
2. API contracts and mock/real API switching points
3. Configuration, environment variables, and deployment path
4. Tests, build, and manual verification
5. Logs, issue diagnosis, and rollback plan
6. Permissions, security, and sensitive information
7. Documentation and handoff notes

Output:
- Overall conclusion
- Blockers
- Non-blocking risks
- Recommended handling order
- Delivery note
```
