# AI Coding Discipline Checklist

Use this checklist during implementation. It is intentionally short so it can be applied under pressure.

## Before Editing

- [ ] I can state the requested outcome in one sentence.
- [ ] I know the affected entry point, module, file, page, API, script, or workflow.
- [ ] I checked existing structure before creating new code.
- [ ] I looked for reusable helpers, components, types, schemas, utilities, configuration, and tests.
- [ ] I identified at least one verification path.
- [ ] I named the main regression risk.

## Design Shape

- [ ] Each changed unit has one clear responsibility.
- [ ] Inputs and outputs are explicit.
- [ ] Invalid input, empty state, dependency failure, and permission or security boundaries are considered when relevant.
- [ ] Configuration and environment details are not hardcoded into business logic.
- [ ] The smallest useful closed loop is clear.

## While Editing

- [ ] I am extending existing patterns unless there is a specific reason not to.
- [ ] I am not creating duplicate utilities or parallel flows.
- [ ] I am keeping unrelated refactors out of scope.
- [ ] I am verifying after meaningful changes instead of batching a large untested diff.
- [ ] I am preserving existing public contracts unless the task requires changing them.

## Before Completion

- [ ] I ran the freshest practical verification command or manual check.
- [ ] I read the verification output.
- [ ] I can describe what was verified and what was not.
- [ ] I can name residual risk, if any.
- [ ] The final response does not imply success beyond the evidence.

## If Verification Is Not Available

Say so directly and provide the best alternative evidence:

- code path inspected
- expected command that should be run later
- manual check steps
- risk level
- reason verification could not be run
