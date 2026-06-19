# Autoupdate Patterns

Use this file when generating `checkver` and `autoupdate`.

## GitHub Checkver

```json
"checkver": {
  "github": "https://github.com/owner/repo"
}
```

## Official Site Checkver

```json
"checkver": {
  "url": "https://example.com/download",
  "regex": "app-([\\d.]+)-x64\\.zip"
}
```

## Single URL Autoupdate

```json
"autoupdate": {
  "url": "https://downloads.example.com/app-$version-x64.zip"
}
```

## Architecture-Specific Autoupdate

```json
"autoupdate": {
  "architecture": {
    "64bit": {
      "url": "https://downloads.example.com/app-$version-x64.zip"
    },
    "32bit": {
      "url": "https://downloads.example.com/app-$version-x86.zip"
    },
    "arm64": {
      "url": "https://downloads.example.com/app-$version-arm64.zip"
    }
  }
}
```

## Hash URL Pattern

```json
"autoupdate": {
  "url": "https://downloads.example.com/app-$version.zip",
  "hash": {
    "url": "https://downloads.example.com/app-$version.sha256"
  }
}
```

## Variables

- `$version`
- `$majorVersion`
- `$minorVersion`
- `$patchVersion`
- `$match1`
- `$match2`

## Decision Rules

- Use `autoupdate` only when the artifact path is predictable.
- Do not template `/latest` redirects.
- Do not template short links.
- Do not template signed or expiring CDN URLs.
- Use regex capture groups only when they are stable release metadata, not accidental page text.
