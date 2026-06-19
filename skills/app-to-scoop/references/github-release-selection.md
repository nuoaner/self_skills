# GitHub Release Selection

Use this file for GitHub repositories, release pages, and asset URLs.

## Asset Priority

Choose assets in this order:

1. Windows portable `.zip` or `.7z`
2. Windows portable `.exe`
3. Extractable `setup.exe`
4. `.msi`
5. Silent-capable installer `.exe`
6. Source archive only for script-based projects

## Avoid

- `Source code (zip)`
- `Source code (tar.gz)`

Do not use GitHub auto-generated source archives unless the project is actually delivered as source scripts.

## Architecture Mapping

- `x64`, `win64`, `amd64` -> `64bit`
- `x86`, `win32`, `i386`, `ia32` -> `32bit`
- `arm64`, `aarch64` -> `arm64`

## Checkver

Prefer:

```json
"checkver": {
  "github": "https://github.com/owner/repo"
}
```

Use the canonical repository URL, not the release asset URL.

## Autoupdate Conditions

Add `autoupdate` only when:

- release asset names are stable
- each architecture has a predictable filename
- the repo does not rename artifacts arbitrarily per release

Good pattern:

```json
"autoupdate": {
  "architecture": {
    "64bit": {
      "url": "https://github.com/owner/repo/releases/download/v$version/app-$version-win-x64.zip"
    }
  }
}
```

Bad candidates:

- `/latest` redirect URLs
- filenames that depend on release titles
- assets with manually changing suffixes

## Inspection Rule

If the archive layout is unclear, inspect it locally before deciding:

- `bin`
- `shortcuts`
- `extract_dir`
- `persist`
