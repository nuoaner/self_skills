# Scoop Official Rules

Use this file for baseline Scoop manifest rules.

## Core Model

- Scoop packages are JSON manifests.
- `url` and `hash` describe the downloadable payload.
- Prefer SHA256 hashes.
- Never fabricate a hash or leave a fake hash in a final manifest.

## Common Fields

- `version`: package version string.
- `description`: short human-readable package summary.
- `homepage`: official upstream page.
- `license`: SPDX identifier or structured license object when known.
- `architecture`: separate `64bit`, `32bit`, and `arm64` URLs or hashes when needed.
- `bin`: command-line entrypoints.
- `shortcuts`: Start Menu shortcuts for GUI apps.
- `persist`: user data or config that must survive upgrades.
- `checkver`: version detection rule.
- `autoupdate`: future URL/hash template.

## Selection Rules

- Prefer upstream-hosted artifacts.
- Prefer portable archives over installers.
- Avoid bootstrap or web installers.
- Avoid GitHub source archives unless the project is really distributed as scripts.
- Do not guess hidden paths inside archives; inspect them first when uncertain.

## Architecture Guidance

- Use top-level `architecture` only when URLs, hashes, or filenames differ by CPU target.
- Keep shared fields at the top level when possible.
- Put architecture-specific `url`, `hash`, and nested `autoupdate` fields inside each architecture block.

## Versioning Guidance

- For GitHub projects, prefer `checkver.github`.
- For official sites, prefer `checkver.url` plus `regex`.
- Only add `autoupdate` when the final artifact naming pattern is stable enough to template.

## Editing Existing Manifests

- Preserve fields that are already correct and useful.
- Repair only the broken or stale parts when debugging an existing manifest.
- When replacing a source, explain why the old source was unreliable.
