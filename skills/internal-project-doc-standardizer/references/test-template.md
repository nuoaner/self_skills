# Testing And Acceptance

## 1. Test Status Enum

Test status must use only: `untested` / `testing` / `passed` / `failed` / `blocked` / `not-applicable`.

## 2. Test Checklist

| Test ID | Test Item | Module | Method | Status | Owner | Notes |
|---|---|---|---|---|---|---|
| T-001 | Frontend page access | Frontend | manual / automated | untested | TBD | TBD |
| T-002 | Backend API response | Backend | manual / automated | untested | TBD | TBD |
| T-003 | Database read/write | Database | manual / automated | untested | TBD | TBD |
| T-004 | Login flow | User module | manual / automated | untested | TBD | TBD |
| T-005 | Core business flow | Core module | manual / automated | untested | TBD | TBD |
| T-006 | Build check | Engineering | manual / automated | untested | TBD | TBD |

## 3. Test Record Template

### Test ID: T-TBD

- Test item: TBD
- Test time: TBD
- Tester: TBD
- Environment: TBD
- Steps: TBD
- Expected result: TBD
- Actual result: TBD
- Conclusion: passed / failed / blocked
- Related issue: TBD

## 4. Project Acceptance Criteria

Before a project enters `online` or `maintenance`, it should satisfy:

- README.md is updated and can guide new contributors to run the project.
- Core feature status is `completed`.
- Required API documentation is updated.
- Required database design is updated.
- Local run flow is executable.
- Main test items are `passed`.
- Known high-priority issues are resolved or have clear handling plans.
- agent.md records the latest AI/Agent operation result.
