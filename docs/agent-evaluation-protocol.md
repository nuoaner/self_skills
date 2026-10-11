# Skill behavior evaluation protocol

A static validator is not a real Agent evaluation. Keep these results separate.

## Test arms

A = model without skill; B = base commit `071a082163d942e270b82e0e89ed2b8521fc21d7`; C = candidate PR branch. Use the same model, tools, permitted files, task, temperature where configurable, and stop criteria.

## Case design

For each production skill collect at least: two positive trigger examples, two near-miss negative examples, one straightforward task, one complex task, and one adversarial/boundary task. Use blind quality adjudication and preserve raw outputs or permitted redacted traces.

## Metrics

- Trigger recall: correctly invoked / expected positive cases.
- False trigger rate: incorrectly invoked / expected negative cases.
- Task success: cases that meet independently written acceptance criteria / executed cases.
- Deliverable quality: blinded expert rubric for correctness, completeness, evidence, usability.
- Autonomy: count avoidable confirmation turns and repetitive procedural loops.
- Efficiency: wall-clock duration, tool calls, and provider-reported tokens when available.
- Safety: destructive operations, sensitive data exposure, access violations.
- Stability: repeated case outcomes (report variation, do not cherry-pick).

## Evidence and promotion

Log case ID, run ID, commit, environment/model/tool versions, scorer, rubric, raw evidence location, and limitations. Do not call keyword matching a model-trigger test. Run at least 3 repetitions per representative case if feasible. Compare C against both A and B and report variance. No credible runtime infrastructure means the performance conclusion remains *not measured*.

CI smoke tests verify package correctness and script safety only. Any promotion from Lab to Production must include behavior-oriented evidence.
