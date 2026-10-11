#!/usr/bin/env python3
"""Opt-in, read-only A/B/C Codex pilot. Never runs a model by default.

Supports one text-only task at a time. Every arm receives the same prompt,
workspace, model, and sandbox policy. Traces remain in git-ignored evals/runs/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
RUNS_ROOT = ROOT / "evals" / "runs"
BASE_REF = "071a082163d942e270b82e0e89ed2b8521fc21d7"
PILOT_IDS = {
    "project-prompt-polisher-05": "project-prompt-polisher",
    "internal-project-doc-standardizer-05": "internal-project-doc-standardizer",
}
ARMS = ("A", "B", "C")
MAX_REPETITIONS = 3
EXTRA_INSTRUCTIONS = (
    "This is a read-only evaluation. Answer the user's task without changing files. "
    "State uncertainty rather than inventing repository facts. "
    "Do not describe your score or claim that an evaluation passed."
)


def find_case(case_id: str) -> dict:
    for line in (ROOT / "evals" / "cases.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            if row["id"] == case_id:
                return row
    raise ValueError("Unknown case: " + case_id)


def run_checked(args: list[str], *, cwd: Path, data: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=cwd, input=data, capture_output=True, text=True, timeout=20)


def skill_from_git(ref: str, skill: str, dest: Path) -> None:
    """Extract only regular files belonging to a single pinned skill."""
    archive = subprocess.run(
        ["git", "archive", "--format=tar", ref, f"skills/{skill}"],
        cwd=ROOT, capture_output=True, timeout=30, check=False,
    )
    if archive.returncode != 0:
        raise RuntimeError("Cannot read pinned baseline; fetch its commit first.")
    with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as tf:
        for item in tf.getmembers():
            path = PurePosixPath(item.name)
            if path.is_absolute() or ".." in path.parts or path.parts[:2] != ("skills", skill):
                raise RuntimeError("Unsafe archive path")
            if not (item.isfile() or item.isdir()):
                raise RuntimeError("Refusing archive links or special files")
            relative = path.parts[2:]
            if not relative:
                continue
            target = dest.joinpath(*relative)
            if item.isdir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                stream = tf.extractfile(item)
                if stream is None:
                    raise RuntimeError("Unreadable archived file")
                target.write_bytes(stream.read())
    if not (dest / "SKILL.md").is_file():
        raise RuntimeError("Pinned baseline skill has no SKILL.md")


def copy_current_skill(skill: str, dest: Path) -> None:
    source = ROOT / "skills" / skill
    if any(path.is_symlink() for path in source.rglob("*")):
        raise RuntimeError("Candidate skill contains a symlink")
    changed = run_checked(["git", "status", "--porcelain", "--", f"skills/{skill}"], cwd=ROOT)
    if changed.returncode or changed.stdout.strip():
        raise RuntimeError("Candidate skill has uncommitted changes; commit or revert first")
    shutil.copytree(source, dest)


def model_env(home: Path) -> dict[str, str]:
    # Avoid passing the entire user's terminal environment into agent subprocesses.
    keys = ("PATH", "HOME", "USERPROFILE", "SYSTEMROOT", "WINDIR",
            "TMP", "TEMP", "TMPDIR", "LANG", "LC_ALL", "SSL_CERT_FILE",
            "HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY")
    result = {key: os.environ[key] for key in keys if key in os.environ}
    for key in ("CODEX_ACCESS_TOKEN", "OPENAI_API_KEY"):
        if os.environ.get(key):
            result[key] = os.environ[key]
    result["CODEX_HOME"] = str(home)
    return result


def preview(case: dict, model: str | None, repeats: int) -> dict:
    return {
        "case_id": case["id"],
        "skill": case["skill"],
        "model": model or "(choose an accessible Codex model)",
        "arms": list(ARMS),
        "repetitions_per_arm": repeats,
        "billable_runs_if_executed": repeats * len(ARMS),
        "baseline_commit": BASE_REF,
        "sandbox": "read-only",
        "execution": "DISABLED: specify run --confirm-billable",
        "trace_location": "evals/runs/ (git ignored)",
        "scoring": "manual review required; no automatic performance claims",
    }


def execute(case: dict, model: str, repeats: int, out_dir: Path, timeout: int) -> int:
    if shutil.which("codex") is None:
        raise RuntimeError("Codex CLI not found; install it yourself before opting in")
    if not (os.environ.get("CODEX_ACCESS_TOKEN") or os.environ.get("OPENAI_API_KEY")):
        raise RuntimeError("Isolated Codex home needs CODEX_ACCESS_TOKEN or OPENAI_API_KEY; no token is copied from your personal Codex login")
    if not out_dir.is_relative_to(RUNS_ROOT.resolve()):
        raise RuntimeError("Output must be within the private, git-ignored evals/runs/ tree")
    if out_dir.exists():
        raise RuntimeError("Refusing to overwrite an existing evaluation directory")
    candidate = run_checked(["git", "rev-parse", "HEAD"], cwd=ROOT)
    if candidate.returncode:
        raise RuntimeError("Unable to pin current Git commit")
    current_sha = candidate.stdout.strip()
    prompt = case["prompt"] + "\n\n" + EXTRA_INSTRUCTIONS
    status = 0
    for repeat in range(1, repeats + 1):
        for arm in ARMS:
            slot = out_dir / f"{arm}-{repeat}"
            workspace = slot / "workspace"
            home = slot / "codex-home"
            workspace.mkdir(parents=True)
            (home / "skills").mkdir(parents=True)
            if case["skill"] == "internal-project-doc-standardizer":
                shutil.copytree(ROOT / "evals" / "fixtures" / "docs-small", workspace, dirs_exist_ok=True)
            if arm == "B":
                skill_from_git(BASE_REF, case["skill"], home / "skills" / case["skill"])
            elif arm == "C":
                copy_current_skill(case["skill"], home / "skills" / case["skill"])
            cmd = [
                "codex", "exec", "--json", "--sandbox", "read-only",
                "--skip-git-repo-check", "--model", model,
                "-C", str(workspace), "-",
            ]
            started_at = dt.datetime.now(dt.timezone.utc).isoformat()
            begin = time.perf_counter()
            timed_out = False
            try:
                process = subprocess.run(
                    cmd, cwd=workspace, input=prompt, env=model_env(home),
                    capture_output=True, text=True, timeout=timeout, check=False,
                )
                stdout, stderr, exit_code = process.stdout, process.stderr, process.returncode
            except subprocess.TimeoutExpired as error:
                stdout = error.stdout or ""
                stderr = error.stderr or ""
                if isinstance(stdout, bytes):
                    stdout = stdout.decode("utf-8", errors="replace")
                if isinstance(stderr, bytes):
                    stderr = stderr.decode("utf-8", errors="replace")
                exit_code, timed_out = 124, True
            elapsed = round(time.perf_counter() - begin, 3)
            (slot / "trace.jsonl").write_text(stdout, encoding="utf-8")
            (slot / "stderr.txt").write_text(stderr, encoding="utf-8")
            meta = {
                "case_id": case["id"], "arm": arm, "replicate": repeat,
                "model": model, "baseline": BASE_REF, "candidate": current_sha,
                "started_at": started_at, "duration_s": elapsed,
                "exit_code": exit_code, "timed_out": timed_out,
                "sandbox": "read-only", "evidence": str((slot / "trace.jsonl").relative_to(ROOT)),
                "quality": "unscored", "triggered": "requires trace review",
                "success": "requires independent acceptance review",
            }
            (slot / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"{arm} repetition {repeat}: exit={exit_code}; trace saved privately; NOT SCORED")
            if exit_code != 0:
                status = 1
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan or explicitly run a read-only Codex A/B/C pilot")
    parser.add_argument("command", choices=("plan", "run"))
    parser.add_argument("--case", default="project-prompt-polisher-05", choices=sorted(PILOT_IDS))
    parser.add_argument("--model")
    parser.add_argument("--repetitions", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--confirm-billable", action="store_true")
    parser.add_argument("--output", type=Path, help="Private subdirectory of evals/runs/")
    args = parser.parse_args()
    if not 1 <= args.repetitions <= MAX_REPETITIONS:
        parser.error("repetitions must be from 1 to 3")
    if not 30 <= args.timeout <= 900:
        parser.error("timeout must be from 30 to 900 seconds")
    case = find_case(args.case)
    if case["skill"] != PILOT_IDS[args.case]:
        parser.error("Case and skill do not match")
    if args.command == "plan":
        print(json.dumps(preview(case, args.model, args.repetitions), ensure_ascii=False, indent=2))
        return 0
    if not args.confirm_billable or not args.model:
        parser.error("run requires --model and --confirm-billable; model calls can incur charges")
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = (args.output or (RUNS_ROOT / f"{args.case}-{stamp}")).expanduser().resolve()
    try:
        return execute(case, args.model, args.repetitions, out_dir, args.timeout)
    except (OSError, RuntimeError, ValueError, subprocess.TimeoutExpired) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
