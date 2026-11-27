#!/usr/bin/env python3
"""Read-only portfolio analysis: overlap, freshness, and recorded usage.

This tool produces review signals only. It never edits, merges, renames, or
retires a Skill, and it never claims model improvement without run evidence.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
FIELD = re.compile(r"(?m)^([a-z][a-z0-9_-]*):\s*(.*?)\s*$")
EN_TOKEN = re.compile(r"[a-z][a-z0-9_+-]{1,}", re.I)
CJK_RUN = re.compile(r"[\u3400-\u9fff]+")
STOP_EN = {
    "skill", "skills", "agent", "agents", "user", "users", "use", "using",
    "when", "where", "what", "this", "that", "with", "from", "into", "your",
    "their", "should", "must", "will", "can", "help", "helps", "create",
    "make", "build", "workflow", "output", "quality", "requirements",
    "task", "tasks", "content", "based", "provide", "support", "current",
    "the", "and", "or", "for", "of", "to", "in", "on", "is", "are", "be",
    "as", "at", "by", "not", "no", "do", "does", "more", "less", "one",
    "two", "first", "then", "other", "each", "any", "all", "also", "such",
    "per", "within", "without", "via", "same", "both", "only", "than",
    "rather", "there", "here", "their", "these", "those", "may", "might",
    "well", "most", "many", "some", "used", "using", "based", "across",
    "suitable", "scenarios", "principle", "purpose", "reusable",
    "visual", "image", "images", "design", "assets", "asset", "communication",
}
STOP_ZH = {
    "用户", "使用", "帮助", "生成", "制作", "需要", "可以", "内容", "能力",
    "工作流", "输出", "技能", "系统", "要求", "任务", "支持", "当前",
    "完成", "进行", "通过", "提供", "相关", "一个", "以及", "用于",
}
CADENCE_DAYS = {
    "monthly": 30, "quarterly": 90, "semiannual": 182,
    "annual": 365, "per-release": 180,
}
DEFAULT_CADENCE = {"core": 180, "lab": 365, "reference": 365}


def read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    lines = match.group(1).splitlines()
    result: dict[str, str] = {}
    i = 0
    while i < len(lines):
        field = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*?)\s*$", lines[i])
        if not field:
            i += 1
            continue
        key, value = field.group(1), field.group(2).strip().strip("\"'")
        if key == "description" and value in {"|", "|-", "|+", ">", ">-", ">+"}:
            parts = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                if lines[i].strip():
                    parts.append(lines[i].strip())
                i += 1
            result[key] = " ".join(parts)
            continue
        result[key] = value
        i += 1
    return result


def tokenize(text: str) -> Counter:
    text = text.lower()
    tokens = Counter()
    for token in EN_TOKEN.findall(text):
        token = token.lower()
        if token not in STOP_EN and len(token) > 1:
            tokens["en:" + token] += 1
    for run in CJK_RUN.findall(text):
        if len(run) == 1:
            continue
        if len(run) == 2 and run not in STOP_ZH:
            tokens["zh:" + run] += 1
        for i in range(len(run) - 1):
            gram = run[i:i + 2]
            if gram not in STOP_ZH:
                tokens["zh:" + gram] += 1
    return tokens


def skill_document(skill_dir: Path) -> tuple[str, str]:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8-sig")
    metadata = parse_frontmatter(text)
    body = FRONTMATTER.sub("", text, count=1)
    headings = " ".join(re.findall(r"(?m)^#{1,3}\s+(.+?)\s*$", body))
    fence = chr(96) * 3
    body = re.sub(r"(?s)" + re.escape(fence) + r".*?" + re.escape(fence), " ", body)
    tick = chr(96)
    body = re.sub(re.escape(tick) + r"[^" + re.escape(tick) + r"]+" + re.escape(tick), " ", body)
    description = metadata.get("description", "")
    return description + " " + description + " " + description + " " + description + " " + headings + " " + headings + " " + body[:2500], description


def cosine_tfidf(documents: dict[str, Counter]) -> tuple[dict[tuple[str, str], float], dict[tuple[str, str], list[str]]]:
    names = list(documents)
    n = max(len(names), 1)
    df = Counter()
    for counts in documents.values():
        df.update(counts.keys())
    vectors = {}
    for name, counts in documents.items():
        vector = {}
        for token, count in counts.items():
            tf = 1.0 + math.log(count)
            idf = math.log((n + 1) / (df[token] + 1)) + 1.0
            vector[token] = tf * idf
        norm = math.sqrt(sum(value * value for value in vector.values())) or 1.0
        vectors[name] = {key: value / norm for key, value in vector.items()}
    scores, shared = {}, {}
    for i, left in enumerate(names):
        for right in names[i + 1:]:
            common = set(vectors[left]) & set(vectors[right])
            key = (left, right)
            scores[key] = sum(vectors[left][term] * vectors[right][term] for term in common)
            shared[key] = sorted(common, key=lambda term: vectors[left][term] * vectors[right][term], reverse=True)[:8]
    return scores, shared


def load_relations(path: Path) -> list[dict]:
    data = read_json(path, {"schema_version": 1, "relations": []})
    return data.get("relations", []) if isinstance(data, dict) else []


def pair_key(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


def find_last_change(root: Path, skill_name: str) -> dt.date | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", f"skills/{skill_name}"],
            cwd=root, check=False, capture_output=True, text=True, timeout=8,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    if result.returncode != 0 or not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def review_status(root: Path, item: dict, as_of: dt.date) -> dict:
    name, tier = item["name"], item["tier"]
    manifest = read_json(root / "skills" / name / "manifest.json", {})
    explicit = manifest.get("last_reviewed") or item.get("last_reviewed")
    source = "last_reviewed" if explicit else "git_last_change"
    try:
        last_date = dt.date.fromisoformat(str(explicit)) if explicit else find_last_change(root, name)
    except ValueError:
        last_date = None
    cadence = manifest.get("review_cadence") or item.get("review_cadence")
    cadence_days = manifest.get("review_cadence_days") or item.get("review_cadence_days")
    if not isinstance(cadence_days, int) or cadence_days <= 0:
        cadence_days = CADENCE_DAYS.get(cadence, DEFAULT_CADENCE.get(tier, 365))
    if last_date is None:
        return {
            "skill": name, "status": "unknown", "last_date": None,
            "date_source": "unavailable", "age_days": None,
            "cadence_days": cadence_days,
            "note": "No review date or Git change date could be established.",
        }
    age = (as_of - last_date).days
    if age < 0:
        status = "future_date"
    elif age > cadence_days:
        status = "overdue"
    elif age > cadence_days * 0.8:
        status = "due_soon"
    else:
        status = "current"
    note = "Based on an explicit review date." if source == "last_reviewed" else (
        "Uses last Git content change as a review proxy; this is not proof that the Skill was reviewed."
    )
    return {
        "skill": name, "status": status, "last_date": last_date.isoformat(),
        "date_source": source, "age_days": age, "cadence_days": cadence_days,
        "note": note,
    }


def parse_bool(value: str) -> bool | None:
    value = (value or "").strip().lower()
    if value in {"yes", "true", "1", "completed", "complete", "是", "完成"}:
        return True
    if value in {"no", "false", "0", "failed", "否", "未完成"}:
        return False
    return None


def normalize_benefit(value: str) -> str:
    value = (value or "").strip().lower()
    if value in {"better", "improved", "yes", "有提升", "更好", "优于基线"}:
        return "better"
    if value in {"same", "equal", "unchanged", "持平", "相同"}:
        return "same"
    if value in {"worse", "no", "worse_than_baseline", "更差", "低于基线"}:
        return "worse"
    return "unknown"


def load_usage(path: Path, known_skills: set[str]) -> tuple[dict[str, dict], list[str]]:
    summaries: dict[str, dict] = {}
    warnings = []
    if not path.is_file():
        return summaries, ["No private usage log found; usage-based recommendations are unavailable."]
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error, UnicodeError) as exc:
        return summaries, [f"Could not read usage log: {exc}"]
    for row in rows:
        skill = (row.get("skill") or "").strip()
        if not skill:
            warnings.append("Ignored a usage row without a skill name.")
            continue
        if skill not in known_skills:
            warnings.append(f"Usage log references an unknown skill: {skill}")
            continue
        entry = summaries.setdefault(skill, {
            "records": 0, "completed": 0, "failed": 0, "partial_or_unknown": 0,
            "benefit": Counter(), "quality_scores": [], "friction_records": 0,
            "safety_violations": 0, "durations_s": [], "tool_calls": [],
        })
        entry["records"] += 1
        completed = parse_bool(row.get("task_completed", ""))
        if completed is True:
            entry["completed"] += 1
        elif (row.get("task_completed") or "").strip().lower() in {"no", "false", "0", "failed", "否", "未完成"}:
            entry["failed"] += 1
        else:
            entry["partial_or_unknown"] += 1
        entry["benefit"][normalize_benefit(row.get("benefit_over_no_skill", ""))] += 1
        try:
            score = float(row.get("quality_score", ""))
            if 0 <= score <= 5:
                entry["quality_scores"].append(score)
        except (TypeError, ValueError):
            pass
        friction = (row.get("friction_category") or row.get("problem_or_friction") or "").strip().lower()
        if friction and friction not in {"none", "无", "n/a", "na", "none reported"}:
            entry["friction_records"] += 1
        try:
            value = int(row.get("safety_violations", "") or 0)
            if value >= 0:
                entry["safety_violations"] += value
        except ValueError:
            warnings.append(f"{skill}: invalid safety_violations value in usage log.")
        for field, target in (("duration_s", "durations_s"), ("tool_calls", "tool_calls")):
            try:
                value = float(row.get(field, ""))
                if value >= 0:
                    entry[target].append(value)
            except (TypeError, ValueError):
                pass

    for skill, entry in summaries.items():
        n = entry["records"]
        known_outcomes = entry["completed"] + entry["failed"]
        better_known = entry["benefit"]["better"] + entry["benefit"]["same"] + entry["benefit"]["worse"]
        completion_rate = entry["completed"] / known_outcomes if known_outcomes else None
        better_rate = entry["benefit"]["better"] / better_known if better_known else None
        friction_rate = entry["friction_records"] / n if n else None
        avg_quality = sum(entry["quality_scores"]) / len(entry["quality_scores"]) if entry["quality_scores"] else None
        if entry["safety_violations"] > 0:
            recommendation = "Investigate recorded safety violations before further promotion."
        elif n < 5:
            recommendation = "Sample too small; collect more records before making a portfolio decision."
        elif (completion_rate is not None and completion_rate < 0.7) or (better_rate is not None and better_rate < 0.4):
            recommendation = "Investigate task failures or weak benefit; consider strengthening or narrowing scope."
        elif completion_rate is not None and completion_rate >= 0.9 and better_rate is not None and better_rate >= 0.7 and (friction_rate or 0) <= 0.2:
            recommendation = "Evidence is encouraging; retain and continue monitoring rather than auto-promoting."
        else:
            recommendation = "Mixed or incomplete evidence; inspect examples and keep collecting data."
        entry["completion_rate"] = round(completion_rate, 3) if completion_rate is not None else None
        entry["benefit_better_rate"] = round(better_rate, 3) if better_rate is not None else None
        entry["friction_rate"] = round(friction_rate, 3) if friction_rate is not None else None
        entry["average_quality"] = round(avg_quality, 2) if avg_quality is not None else None
        entry["benefit"] = dict(entry["benefit"])
        entry["recommendation"] = recommendation
    return summaries, warnings


def build_report(root: Path, as_of: dt.date, usage_path: Path, relations_path: Path, threshold: float = 0.18) -> dict:
    catalog = json.loads((root / "skills" / "catalog.json").read_text(encoding="utf-8"))
    entries = catalog["entries"]
    docs: dict[str, Counter] = {}
    for item in entries:
        if item["tier"] == "reference":
            continue
        try:
            text, _ = skill_document(root / "skills" / item["name"])
        except (OSError, UnicodeError):
            continue
        docs[item["name"]] = tokenize(text)

    scores, shared = cosine_tfidf(docs)
    relation_rows = load_relations(relations_path)
    overrides = {pair_key(*r.get("skills", [])): r for r in relation_rows if len(r.get("skills", [])) == 2}
    overlaps, known_relations = [], []
    emitted_relations = set()
    for pair, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        relation = overrides.get(pair_key(*pair))
        if relation:
            if score >= threshold:
                record = {
                    "skills": list(pair), "similarity": round(score, 3),
                    "shared_terms": [term.split(":", 1)[-1] for term in shared[pair]],
                    "relation": relation.get("type", "related"),
                    "reason": relation.get("reason", ""),
                }
                known_relations.append(record)
                emitted_relations.add(pair_key(*pair))
            continue
        if score < threshold:
            continue
        record = {
            "skills": list(pair), "similarity": round(score, 3),
            "shared_terms": [term.split(":", 1)[-1] for term in shared[pair]],
            "review_level": "high" if score >= 0.35 else "medium",
            "interpretation": "Potential scope overlap only; human review is required before any merge decision.",
        }
        overlaps.append(record)
    for key, relation in overrides.items():
        if key in emitted_relations:
            continue
        score = scores.get(key, 0.0)
        known_relations.append({
            "skills": list(key), "similarity": round(score, 3),
            "shared_terms": [term.split(":", 1)[-1] for term in shared.get(key, [])],
            "relation": relation.get("type", "related"),
            "reason": relation.get("reason", ""),
        })

    freshness = [review_status(root, item, as_of) for item in entries if item["tier"] != "reference"]
    usage, usage_warnings = load_usage(usage_path, {x["name"] for x in entries})
    case_count = 0
    cases_path = root / "evals" / "cases.jsonl"
    if cases_path.is_file():
        for line in cases_path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.lstrip().startswith("#"):
                case_count += 1
    tier_counts = Counter(x["tier"] for x in entries)
    return {
        "generated_at": as_of.isoformat(),
        "inventory": {
            "total": len(entries), "core": tier_counts["core"],
            "lab": tier_counts["lab"], "reference": tier_counts["reference"],
            "routing_and_task_cases": case_count,
        },
        "overlap_candidates": overlaps,
        "declared_relationships": known_relations,
        "portfolio_actions": [
            {
                "skill": item["name"], "tier": item["tier"],
                "action": item["action"], "agent_evidence": item.get("agent_evidence", "not_measured"),
                "rationale": item.get("rationale", ""),
                "successor": item.get("successor"),
            }
            for item in entries
        ],
        "freshness": freshness,
        "usage": usage,
        "usage_warnings": usage_warnings,
        "limitations": [
            "Similarity is lexical and heuristic; it detects candidates, not semantic duplicates.",
            "Last Git change is a freshness proxy, not proof of a human review.",
            "No usage record means unknown usage, not zero usage.",
            "Usage logs are manual observations, not telemetry or controlled A/B/C results.",
            "No Skill is automatically merged, renamed, downgraded, or deleted.",
        ],
    }


def render_markdown(report: dict) -> str:
    inv = report["inventory"]
    lines = [
        "# Skill Portfolio Review", "",
        f"Generated: {report['generated_at']}", "",
        f"Inventory: {inv['total']} total · Core {inv['core']} · Lab {inv['lab']} · Reference {inv['reference']} · {inv['routing_and_task_cases']} evaluation cases",
        "", "## Potential scope overlaps", "",
    ]
    if not report["overlap_candidates"]:
        lines.append("No unclassified overlap candidates crossed the configured similarity threshold.")
    else:
        lines += ["| Skills | Similarity | Shared terms | Review |", "|---|---:|---|---|"]
        for row in report["overlap_candidates"]:
            lines.append(f"| {' + '.join(row['skills'])} | {row['similarity']:.3f} | {', '.join(row['shared_terms'])} | {row['review_level']} |")
    lines += ["", "## Declared relationships", ""]
    if not report["declared_relationships"]:
        lines.append("No manually declared relationships.")
    else:
        for row in report["declared_relationships"]:
            lines.append(f"- **{' + '.join(row['skills'])}** — {row['relation']}: {row['reason']} (similarity {row['similarity']:.3f})")
    lines += ["", "## Existing portfolio decisions", "",
              "| Skill | Tier | Decision | Evidence | Reason |",
              "|---|---|---|---|---|"]
    for row in report["portfolio_actions"]:
        reason = row["rationale"].replace("|", "\\|")
        successor = f" (successor: {row['successor']})" if row.get("successor") else ""
        lines.append(f"| {row['skill']} | {row['tier']} | {row['action']} | {row['agent_evidence']} | {reason}{successor} |")
    lines += ["", "## Maintenance freshness", "",
              "| Skill | Status | Last date | Age | Cadence | Basis |",
              "|---|---|---|---:|---:|---|"]
    for row in report["freshness"]:
        age = str(row["age_days"]) if row["age_days"] is not None else "unknown"
        date_value = row["last_date"] or "unknown"
        lines.append(f"| {row['skill']} | {row['status']} | {date_value} | {age} | {row['cadence_days']}d | {row['date_source']} |")
    lines.append("")
    lines.append("Git last-change dates are only a freshness proxy when no explicit review date exists; they do not prove a human review.")
    lines += ["", "## Recorded usage evidence", ""]
    if not report["usage"]:
        lines.append("No private usage records found. Usage-based value and low-usage claims are **not measured**.")
    else:
        lines += ["| Skill | Records | Completion | Better than baseline | Avg quality | Friction | Safety violations |",
                  "|---|---:|---:|---:|---:|---:|---:|"]
        for skill, row in sorted(report["usage"].items()):
            pct = lambda v: f"{v:.0%}" if v is not None else "unknown"
            quality = f"{row['average_quality']:.2f}/5" if row["average_quality"] is not None else "unknown"
            lines.append(f"| {skill} | {row['records']} | {pct(row['completion_rate'])} | {pct(row['benefit_better_rate'])} | {quality} | {pct(row['friction_rate'])} | {row['safety_violations']} |")
        lines += ["", "### Usage-based review signals", ""]
        for skill, row in sorted(report["usage"].items()):
            lines.append(f"- **{skill}**: {row['recommendation']}")
    if report["usage_warnings"]:
        lines += ["", "Usage log warnings:"]
        lines.extend(f"- {warning}" for warning in report["usage_warnings"])
    lines += ["", "## Interpretation limits", ""]
    lines.extend(f"- {item}" for item in report["limitations"])
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Skill portfolio review")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--usage-log", type=Path, default=None)
    parser.add_argument("--relations", type=Path, default=None)
    parser.add_argument("--as-of", type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument("--threshold", type=float, default=0.18)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path, help="Optional report output path; no files are written by default.")
    args = parser.parse_args()
    root = args.root.resolve()
    usage_path = args.usage_log or (root / "evals" / "usage-log.csv")
    relations_path = args.relations or (root / "docs" / "skill-relations.json")
    report = build_report(root, args.as_of, usage_path, relations_path, args.threshold)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n" if args.format == "json" else render_markdown(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="" if rendered.endswith("\n") else "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
