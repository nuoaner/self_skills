# Engineering Discipline Prompt Template

Use this when the user wants a reusable prompt for another coding agent.

```text
Please complete the following task in the current project using disciplined engineering practices.

Task goal:
- <Describe the problem and expected result in 1-2 sentences.>

Execution requirements:
1. Read the existing project structure and related files before adding new modules or parallel flows.
2. Prefer existing components, utilities, types, configuration, styles, API conventions, and test patterns.
3. Before editing, state the smallest implementation shape: files touched, module responsibilities, inputs, outputs, failure cases, and verification method.
4. Implement one minimal working closed loop first, then expand gradually. Do not spread a large unverified diff.
5. Keep functions and files focused. Avoid mixing I/O, business logic, formatting, persistence, and configuration.
6. Handle boundary cases: empty values, invalid input, permissions, network/file/database failures, duplicate submission, and compatibility issues.
7. Do not hardcode secrets, user-specific paths, ports, model names, thresholds, or environment configuration. Use the project's existing configuration path.
8. Do not perform broad refactors, directory migrations, or style rewrites unrelated to this task.

Acceptance criteria:
1. <Observable functional result>
2. <Test, build, lint, script, screenshot, API response, or manual verification method>
3. Existing critical behavior does not regress.

After completion, report:
- What changed
- Which verification commands or checks ran, and their results
- What was not verified
- Remaining risks or recommended follow-up
```

## Short Version

```text
Inspect existing implementation and reuse existing structure first, then implement the smallest verifiable closed loop. Before editing, state the touched files, module boundaries, inputs, outputs, failure cases, and verification method. Keep responsibilities clear, avoid duplicate mechanisms, handle edge cases, and avoid unrelated refactors. After completion, provide verification evidence and residual risk.
```
