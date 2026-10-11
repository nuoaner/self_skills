# Reproducible agent-evaluation protocol

**No real Agent model run is included in this repository.** Static unit tests and case validation cannot demonstrate skill value.

## Case registry

`evals/cases.jsonl` defines **35 labeled English/Chinese prompts** for the current five Core candidates: at least 2 positives, 2 near-miss negatives, and 1 representative task per skill. Every case provides independent acceptance criteria. These are specifications only; use actual source files, sample images, and controlled environments when executing relevant tasks.

Validate the dataset without invoking any Agent:

```bash
python scripts/eval_cases.py validate
```

## Controlled experiments

Run the same case under:
- **A:** baseline Agent, with the target Skill unavailable.
- **B:** previous Skill version from a fixed historical commit.
- **C:** candidate Skill version under review.

Keep the model, effort/settings, enabled tools, accessible context, task data, and evaluator as consistent as possible. Distinguish explicit Skill invocation from automatic route-selection evaluations. Do not penalize A for not invoking a Skill that was not installed. For image tasks, human reviewers should score generated media, not only written plans.

Write one JSONL record per actual run (prefer 3 repetitions for representative scenarios):

```json
{"case_id":"project-prompt-polisher-01","arm":"C","run_id":"actual-run-001","triggered":true,"success":true,"quality":4.0,"duration_s":12.0,"tool_calls":1,"confirmations":0,"safety_violations":0,"evidence":"redacted-traces/run-001"}
```

The record above is **illustrative schema documentation**, not a real measured result. Fields `tokens` (integer) and model/environment metadata can be added if actually captured. `quality` uses a separately defined, blind 0–5 rubric. Evidence must link to sanitized run output or a review record, not a fabricated path.

Generate a comparison only after producing your own run file:

```bash
python scripts/eval_cases.py report --results /private/location/my-runs.jsonl
```

The report shows coverage gaps and reports each arm separately. It does not automatically assert significant improvement. Publish only anonymized summaries after independently verifying task outcomes, tool traces, and variance.

Never commit secrets, customer datasets, raw prompts containing private information, or unreviewed screenshots. Store private traces outside the public repository (the `evals/runs/` directory is git-ignored).
