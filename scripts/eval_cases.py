#!/usr/bin/env python3
"""Validate skill evaluation cases and summarize *recorded* real runs.

This tool never simulates skill selection or manufactures model scores.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPES = {'positive', 'negative', 'task'}
ARMS = {'A', 'B', 'C'}


def read_jsonl(path: Path) -> list[dict]:
    records = []
    for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f'{path}:{i}: invalid JSON: {exc}') from exc
        if not isinstance(row, dict):
            raise ValueError(f'{path}:{i}: expected object')
        records.append(row)
    return records


def validate_cases(root: Path) -> tuple[dict[str, dict], list[str]]:
    errors = []
    catalog = json.loads((root / 'skills' / 'catalog.json').read_text(encoding='utf-8'))
    active = {entry['name'] for entry in catalog['entries'] if entry['tier'] == 'core'}
    cases_path = root / 'evals' / 'cases.jsonl'
    if not cases_path.is_file():
        return {}, ['evals/cases.jsonl missing']
    try:
        cases = read_jsonl(cases_path)
    except (ValueError, UnicodeError) as exc:
        return {}, [str(exc)]
    seen = {}
    counts = Counter()
    for row in cases:
        name, kind, identifier = row.get('skill'), row.get('kind'), row.get('id')
        if not isinstance(identifier, str) or not identifier.strip() or identifier in seen:
            errors.append(f'bad or duplicate case id: {identifier}')
            continue
        seen[identifier] = row
        if name not in active:
            errors.append(f'{identifier}: noncore or unknown skill {name}')
        if kind not in TYPES:
            errors.append(f'{identifier}: unknown kind {kind}')
        else:
            counts[name, kind] += 1
        if not isinstance(row.get('prompt'), str) or not row['prompt'].strip():
            errors.append(f'{identifier}: missing prompt')
        if not isinstance(row.get('acceptance'), str) or not row['acceptance'].strip():
            errors.append(f'{identifier}: missing independent acceptance criteria')
        if kind in {'positive', 'negative'} and row.get('should_trigger') is not (kind == 'positive'):
            errors.append(f'{identifier}: should_trigger mismatch')
        if kind == 'task' and row.get('should_trigger') is not True:
            errors.append(f'{identifier}: task must expect core skill to trigger')
    for name in sorted(active):
        for kind, count in {'positive':2, 'negative':2, 'task':1}.items():
            if counts[name,kind] < count:
                errors.append(f'{name}: at least {count} {kind} cases required')
    return seen, errors


def summarize_results(cases: dict[str, dict], results: list[dict]) -> tuple[str, list[str]]:
    errors = []
    by_arm = defaultdict(list)
    run_keys = set()
    for row in results:
        case_id, arm, run_id = row.get('case_id'), row.get('arm'), row.get('run_id')
        if case_id not in cases or arm not in ARMS or not isinstance(run_id, str) or not run_id:
            errors.append(f'invalid case_id/arm/run_id: {case_id}/{arm}/{run_id}')
            continue
        key = (case_id, arm, run_id)
        if key in run_keys:
            errors.append(f'duplicate run: {key}')
        run_keys.add(key)
        if not isinstance(row.get('triggered'), bool) or not isinstance(row.get('success'), bool):
            errors.append(f'{key}: triggered and success must be bool')
            continue
        if not isinstance(row.get('evidence'), str) or not row['evidence'].strip():
            errors.append(f'{key}: missing evidence reference')
        for field in ('duration_s', 'tool_calls', 'confirmations', 'safety_violations'):
            value = row.get(field)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
                errors.append(f'{key}: invalid nonnegative {field}')
        if 'tokens' in row and (not isinstance(row['tokens'], int) or row['tokens'] < 0):
            errors.append(f'{key}: invalid tokens')
        if 'quality' in row and (not isinstance(row['quality'], (int,float)) or not 0 <= row['quality'] <= 5):
            errors.append(f'{key}: quality must be 0..5')
        by_arm[arm].append(row)
    if errors:
        return '', errors
    output = ['# Recorded agent evaluation results', '', 'This report summarizes supplied runs only; missing arms/replicates prevent improvement claims.', '']
    for arm in sorted(ARMS):
        group = by_arm[arm]
        if not group:
            output.append(f'- {arm}: no recorded runs')
            continue
        routed = [int(row['triggered'] == cases[row['case_id']]['should_trigger']) for row in group]
        route_label = 'not_applicable_no_skill' if arm == 'A' else f'{sum(routed)}/{len(routed)}'
        tasks = [row for row in group if cases[row['case_id']]['kind'] == 'task']
        mean = lambda field: round(statistics.mean(row[field] for row in group), 2)
        output.append(f"- {arm}: runs={len(group)}, routing_correct={route_label}, "
                      f"task_success={sum(row['success'] for row in tasks)}/{len(tasks)}, "
                      f"mean_duration_s={mean('duration_s')}, mean_tool_calls={mean('tool_calls')}, "
                      f"mean_confirmations={mean('confirmations')}, mean_safety_violations={mean('safety_violations')}")
        if tasks and all('quality' in x for x in tasks):
            output.append(f"  - task_mean_quality={round(statistics.mean(x['quality'] for x in tasks), 2)} / 5")
        if all('tokens' in x for x in group):
            output.append(f"  - mean_tokens={round(statistics.mean(x['tokens'] for x in group), 2)}")
    seen_pairs = {(r['case_id'], r['arm']) for r in results}
    uncovered = [(cid, arm) for cid in cases for arm in sorted(ARMS) if (cid,arm) not in seen_pairs]
    if uncovered:
        output += ['', f'Incomplete A/B/C coverage: {len(uncovered)} missing case-arm pairs.',
                   'Do not describe this output as proof that the optimized skill is better.']
    else:
        reps = [sum(1 for r in results if r['case_id'] == case_id and r['arm'] == arm)
                for case_id in cases for arm in ARMS]
        if min(reps) < 3:
            output += ['', 'A/B/C arms present, but fewer than three runs per case/arm: treat as preliminary.']
        else:
            output += ['', 'Repeated A/B/C runs present. Human review of output quality and controls is still required.']
    return '\n'.join(output) + '\n', []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['validate', 'report'])
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--results', type=Path)
    args = parser.parse_args()
    cases, errors = validate_cases(args.root.resolve())
    if not errors and args.command == 'report':
        if not args.results:
            parser.error('--results is required for report')
        try:
            runs = read_jsonl(args.results)
            report, errors = summarize_results(cases, runs)
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
        if not errors:
            print(report)
    elif not errors:
        print(f'PASS: {len(cases)} labeled evaluation cases. Runtime evaluation NOT executed.')
    for error in errors:
        print('ERROR:', error, file=sys.stderr)
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
