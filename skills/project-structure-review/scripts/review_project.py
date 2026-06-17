#!/usr/bin/env python3
"""Read-only project structure review for team submission standards."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".next",
    ".nuxt",
    ".svelte-kit",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    "target",
    "out",
    "coverage",
}

CONFIG_NAMES = {
    "package.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "package-lock.json",
    "vite.config.js",
    "vite.config.ts",
    "webpack.config.js",
    "tsconfig.json",
    "jsconfig.json",
    "pyproject.toml",
    "requirements.txt",
    "setup.py",
    "pom.xml",
    "build.gradle",
    "settings.gradle",
    "Cargo.toml",
    "go.mod",
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    ".eslintrc",
    ".prettierrc",
}

CONFIG_PREFIXES = (
    ".eslintrc",
    ".prettierrc",
    "vite.config.",
    "webpack.config.",
    "rollup.config.",
    "next.config.",
    "nuxt.config.",
    "tailwind.config.",
)

ENTRY_NAMES = {
    "main.py",
    "app.py",
    "server.py",
    "manage.py",
    "index.js",
    "index.ts",
    "index.jsx",
    "index.tsx",
    "main.js",
    "main.ts",
    "main.jsx",
    "main.tsx",
    "app.js",
    "app.ts",
    "Program.cs",
}

CODE_EXTS = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".go",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".mjs",
    ".php",
    ".py",
    ".rs",
    ".swift",
    ".ts",
    ".tsx",
    ".vue",
}

DOC_EXTS = {
    ".md",
    ".markdown",
    ".txt",
    ".doc",
    ".docx",
    ".pdf",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
}

README_NAMES = {"readme", "readme.md", "readme.txt", "readme.markdown"}


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def list_paths(root: Path) -> tuple[list[Path], list[Path]]:
    dirs: list[Path] = []
    files: list[Path] = []
    for current, dirnames, filenames in os.walk(root):
        current_path = Path(current)
        rel_current = current_path.relative_to(root)
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        if is_ignored(rel_current):
            continue
        for dirname in dirnames:
            dirs.append((current_path / dirname).relative_to(root))
        for filename in filenames:
            rel = (current_path / filename).relative_to(root)
            if not is_ignored(rel):
                files.append(rel)
    return dirs, files


def has_non_ascii(text: str) -> bool:
    return any(ord(ch) > 127 for ch in text)


def has_connector(name: str) -> bool:
    return "-" in name or "_" in name


def is_config_file(path: Path) -> bool:
    name = path.name
    return name in CONFIG_NAMES or any(name.startswith(prefix) for prefix in CONFIG_PREFIXES)


def is_entry_file(path: Path) -> bool:
    name = path.name
    if name in ENTRY_NAMES:
        return True
    if path.suffix in CODE_EXTS and path.stem.lower() in {"main", "index", "app", "server"}:
        return True
    normalized = "/".join(part.lower() for part in path.parts)
    return normalized.endswith("/cmd/main.go") or normalized.endswith("/src/main/java/application.java")


def find_readme(root: Path, files: list[Path]) -> Path | None:
    for path in files:
        if len(path.parts) == 1 and path.name.lower() in README_NAMES:
            return root / path
    return None


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "utf-8-sig", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return ""


def section_present(text: str, patterns: list[str]) -> bool:
    lower = text.lower()
    return any(re.search(pattern, lower, re.IGNORECASE) for pattern in patterns)


def review_readme(readme: Path | None) -> list[tuple[str, str]]:
    if readme is None:
        return [("HIGH", "根目录缺少 README 文件。")]

    text = read_text(readme)
    findings: list[tuple[str, str]] = []
    checks = [
        (
            "项目介绍",
            [r"项目介绍", r"简介", r"overview", r"introduction", r"about"],
        ),
        (
            "项目管理工具",
            [r"项目管理", r"package manager", r"npm", r"pnpm", r"yarn", r"maven", r"gradle", r"cargo", r"make"],
        ),
        (
            "语法检查工具",
            [r"语法检查", r"lint", r"eslint", r"prettier", r"ruff", r"black", r"checkstyle", r"type-check", r"test"],
        ),
        (
            "重要依赖及其版本",
            [r"依赖", r"dependencies", r"版本", r"version", r"node\s*\d+", r"python\s*\d+", r"java\s*\d+"],
        ),
        (
            "架构图",
            [r"架构图", r"architecture", r"mermaid", r"plantuml", r"!\[.*\]\(.*\)", r"```mermaid"],
        ),
    ]
    for label, patterns in checks:
        if not section_present(text, patterns):
            findings.append(("MEDIUM", f"README 缺少或未清晰说明：{label}。"))
    return findings


def review(root: Path) -> list[tuple[str, str]]:
    dirs, files = list_paths(root)
    findings: list[tuple[str, str]] = []

    too_deep = [path for path in dirs if len(path.parts) > 2]
    for path in too_deep[:20]:
        findings.append(("HIGH", f"文件夹嵌套超过两层：{path.as_posix()}。"))
    if len(too_deep) > 20:
        findings.append(("HIGH", f"还有 {len(too_deep) - 20} 个目录超过两层，建议继续排查。"))

    root_files = [path for path in files if len(path.parts) == 1]
    if not any(is_config_file(path) for path in root_files):
        findings.append(("HIGH", "根目录未发现常见工程配置文件。"))
    if not any(is_entry_file(path) for path in files):
        findings.append(("HIGH", "未发现明显程序入口文件。"))

    readme = find_readme(root, files)
    findings.extend(review_readme(readme))

    for path in dirs:
        if has_connector(path.name):
            findings.append(("MEDIUM", f"文件夹名不应使用连接符号：{path.as_posix()}。"))

    for path in files:
        name = path.name
        if path.suffix.lower() not in DOC_EXTS and has_non_ascii(name):
            findings.append(("MEDIUM", f"非文档文件名应只使用英文：{path.as_posix()}。"))
        if path.suffix.lower() in CODE_EXTS and "-" in path.stem:
            findings.append(("MEDIUM", f"代码文件连接符建议使用下划线：{path.as_posix()}。"))
        if path.suffix.lower() not in CODE_EXTS and path.suffix.lower() not in DOC_EXTS and "_" in path.stem:
            findings.append(("LOW", f"非代码文件连接符建议使用减号：{path.as_posix()}。"))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Review a project against team submission standards.")
    parser.add_argument("project_root", help="Path to the project root to review.")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"ERROR: project root does not exist or is not a directory: {root}")
        return 2

    findings = review(root)
    print(f"# Project Structure Review\n\nProject: `{root}`\n")
    if not findings:
        print("**结论**\n\n通过。未发现违反团队项目结构、命名和 README 基线规范的问题。")
        return 0

    severity_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    findings.sort(key=lambda item: (severity_order[item[0]], item[1]))
    print("**结论**\n\n不通过或需要整改。请优先处理 High 和 Medium 项。\n")
    print("**问题清单**")
    for severity, message in findings:
        print(f"- [{severity}] {message}")
    print("\n**整改建议**")
    print("1. 先补齐根目录 README、工程配置文件和入口文件。")
    print("2. 将源代码目录嵌套控制在两层以内，生成目录和依赖目录可忽略。")
    print("3. 统一命名：文件夹不用连接符，代码文件用下划线，非代码文件用减号。")
    print("4. 在 README 中补充项目介绍、管理工具、语法检查工具、关键依赖版本和架构图。")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
