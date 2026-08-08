---
name: app-to-scoop
description: Use when Codex needs to create, review, debug, or maintain Scoop manifests from GitHub repositories, GitHub releases, official app websites, download pages, direct download links, CDN links, mirror sites, existing Scoop manifests, or Scoop error messages, including generating bucket/app.json files, selecting Windows release assets, configuring architecture-specific URLs and hashes, adding checkver or autoupdate, defining bin, shortcuts, persist, and installer behavior, or troubleshooting Scoop install and update failures.
---

# App To Scoop

Turn app distribution sources into complete Scoop manifests and supporting local test steps.

## Core Behavior

Treat this skill as a packaging workflow, not a generic Scoop tutorial. Start from the user input, classify the source, choose the safest Windows asset, build a complete manifest, explain any uncertain fields, and give local verification commands.

Always:

- Prefer official sources over third-party download sites.
- Verify current upstream information before creating or repairing manifests.
- Prefer portable archives over installers.
- Avoid web installers unless no offline package exists.
- Do not use GitHub source archives unless the project is script-based.
- Do not invent hashes.
- Do not invent download URLs.
- Do not add `autoupdate` unless the URL pattern is stable.
- Do not guess nested executable paths unless the archive structure is known.
- Use GitHub `checkver` for GitHub projects.
- Use `checkver.url` plus `regex` for official websites.
- Use `architecture` for `x64`/`x86`/`arm64` differences.
- Use `bin` for CLI tools.
- Use `shortcuts` for GUI launchers.
- Use both `bin` and `shortcuts` when the app supports both CLI and GUI use.
- Use `persist` for user configuration and data.
- Preserve working fields when editing an existing manifest.
- Always output a complete manifest when creating or repairing a package.
- Always provide local test commands.

## Verification Rule

Before making claims about version, release assets, URLs, hashes, download availability, or current packaging status:

1. Check the current upstream source when available.
2. Mark unavailable information as requiring local confirmation.
3. Do not rely only on historical examples or remembered release patterns.

A generated manifest can contain placeholders for locally verified values, but it must clearly identify what still needs confirmation.

## Input Types

Classify the input first, then load the matching reference:

1. GitHub repository
2. GitHub release page
3. GitHub release asset URL
4. Official website
5. Official download page
6. Direct CDN URL
7. Mirror URL
8. Existing Scoop manifest
9. Scoop error message

Read [references/source-selection.md](references/source-selection.md) first.

Then:

- For GitHub-related sources, read [references/github-release-selection.md](references/github-release-selection.md).
- For official sites, download pages, CDN links, or mirrors, read [references/official-site-selection.md](references/official-site-selection.md).
- For field composition, read [references/manifest-patterns.md](references/manifest-patterns.md).
- For `checkver` and `autoupdate`, read [references/autoupdate-patterns.md](references/autoupdate-patterns.md).
- For error-driven repair, read [references/troubleshooting.md](references/troubleshooting.md).
- For Scoop baseline rules, read [references/scoop-official-rules.md](references/scoop-official-rules.md).
- For bucket style aligned with community CN packaging practice, read [references/extras-cn-patterns.md](references/extras-cn-patterns.md).

## Workflow

Follow this order unless the user explicitly asks for a narrower task:

1. Classify the source type.
2. Confirm the source is trustworthy and prefer official upstreams.
3. Identify the app name, app type, current version, and Windows packaging style.
4. Select the best Windows asset with this priority:
   - portable `.zip` / `.7z`
   - portable `.exe`
   - extractable `setup.exe`
   - `.msi`
   - silent-capable installer `.exe`
   - source archive only for script-based tools
5. Map architecture labels:
   - `x64` / `win64` / `amd64` -> `64bit`
   - `x86` / `win32` / `i386` / `ia32` -> `32bit`
   - `arm64` / `aarch64` -> `arm64`
6. Determine entry fields:
   - `bin` for CLI entrypoints
   - `shortcuts` for GUI launchers
   - `persist` for settings, plugins, profiles, downloads, or user data
   - `env_set` for required environment variables
   - `extract_dir`, `extract_to`, or installer blocks when unpacking needs help
   - `post_install` only for cleanup or small deterministic fixes
   - `notes` for manual caveats or dependencies
7. Generate version detection:
   - GitHub projects: `"checkver": { "github": "https://github.com/owner/repo" }`
   - Official sites: `"checkver": { "url": "...", "regex": "..." }`
8. Generate `autoupdate` only if the final downloadable URL can be templated reliably.
9. Output the full manifest, local confirmation items, and local test commands.

## Output Format

Use this structure in responses:

## Analysis Result

- Source type:
- App name:
- App type:
- Current version:
- Download source:
- Selected asset:
- Architecture:
- Entry type:
- Persist decision:
- Checkver plan:
- Autoupdate plan:

## Manifest

```json
{
  "...": "..."
}
```

## Needs Local Confirmation

- Whether the hash has been computed locally.
- Whether the executable path is correct.
- Whether `extract_dir` or `extract_to` is correct.
- Whether the `persist` paths really exist.
- Whether the license field is accurate.
- Whether the download URL redirects in a way that changes packaging behavior.

## Test Commands

```powershell
scoop install .\bucket\app.json
scoop checkver app
scoop uninstall app
```

## Add To Your Bucket

```powershell
scoop bucket add my-bucket D:\path\to\bucket
scoop install my-bucket/app
```

## Local Helper Scripts

Use the bundled scripts for deterministic local checks instead of recreating their logic:

- `scripts/hash-url.ps1`: compute or verify a download hash through the local Scoop environment.
- `scripts/inspect-release-archive.ps1`: inspect archive layout before deciding executable paths, extraction fields, shortcuts, or persistence paths.
- `scripts/test-manifest.ps1`: run a conservative local install/check/uninstall verification cycle for the manifest.

If a field cannot be verified from the source alone, say so directly and leave a clear local verification step instead of guessing.
