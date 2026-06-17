#!/usr/bin/env python3
"""Read-only audit for the internal project documentation standard."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "agent.md",
    "docs/standard.md",
    "docs/requirements.md",
    "docs/architecture.md",
    "docs/api.md",
    "docs/database.md",
    "docs/deploy.md",
    "docs/test.md",
    "docs/changelog.md",
]

README_SECTIONS = [
    "项目基本信息",
    "项目概述",
    "快速开始",
    "工程结构",
    "当前进度",
    "文档索引",
    "已知问题",
    "下一步",
    "AI / Agent 使用提示",
]

ENUMS = {
    "project_status": ["规划中", "开发中", "联调中", "测试中", "已上线", "维护中", "暂停", "已归档"],
    "feature_status": ["待规划", "待实现", "开发中", "待联调", "待测试", "已完成", "已废弃"],
    "api_status": ["待设计", "待实现", "已实现", "待联调", "已上线", "已废弃"],
    "database_status": ["待设计", "已设计", "已迁移", "已上线", "已废弃"],
    "test_status": ["未测试", "测试中", "通过", "不通过", "阻塞", "不适用"],
    "issue_status": ["待处理", "处理中", "已解决", "暂不处理", "已关闭"],
}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password|passwd|private[_-]?key)\s*[:=]\s*['\"]?[^\\s'\"<>]+"),
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"),
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig", errors="replace")


def find_status_values(text: str) -> list[str]:
    values: list[str] = []
    for line in text.splitlines():
        if "|" not in line or "---" in line:
            continue
        for cell in [part.strip(" `") for part in line.strip().strip("|").split("|")]:
            if cell:
                values.append(cell)
    return values


def audit(root: Path) -> dict:
    result: dict = {
        "root": str(root),
        "missing_files": [],
        "readme_missing_sections": [],
        "placeholder_counts": {},
        "secret_risks": [],
        "status_notes": [],
    }

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            result["missing_files"].append(rel)

    readme = root / "README.md"
    if readme.exists():
        text = read_text(readme)
        for section in README_SECTIONS:
            if section not in text:
                result["readme_missing_sections"].append(section)

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists() or path.is_dir():
            continue
        text = read_text(path)
        count = text.count("待填写")
        if count:
            result["placeholder_counts"][rel] = count
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                result["secret_risks"].append(rel)
                break

    allowed = set().union(*ENUMS.values())
    for rel in ["README.md", "docs/requirements.md", "docs/api.md", "docs/database.md", "docs/test.md"]:
        path = root / rel
        if not path.exists():
            continue
        suspicious = []
        for value in find_status_values(read_text(path)):
            if value in ("状态", "当前状态", "测试状态", "数据库状态", "接口状态"):
                continue
            if value in ["完成", "进行中", "未开始", "已完成 / 未完成", "TODO"]:
                suspicious.append(value)
        if suspicious:
            result["status_notes"].append({"file": rel, "values": sorted(set(suspicious))})

    result["ok"] = not any(
        result[key]
        for key in ["missing_files", "readme_missing_sections", "secret_risks", "status_notes"]
    )
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: audit_docs.py <project-root>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Project root not found: {root}", file=sys.stderr)
        return 2
    print(json.dumps(audit(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
