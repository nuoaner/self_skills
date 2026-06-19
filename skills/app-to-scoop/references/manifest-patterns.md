# Manifest Patterns

Use these as starting shapes. Replace placeholders with verified values and never ship placeholder hashes in a final manifest.

## 1. GitHub GUI App

```json
{
  "version": "1.2.3",
  "description": "Example GUI app.",
  "homepage": "https://github.com/owner/repo",
  "license": "MIT",
  "url": "https://github.com/owner/repo/releases/download/v1.2.3/app-1.2.3-win-x64.zip",
  "hash": "sha256-placeholder",
  "shortcuts": [
    [
      "App.exe",
      "App"
    ]
  ],
  "checkver": {
    "github": "https://github.com/owner/repo"
  },
  "autoupdate": {
    "url": "https://github.com/owner/repo/releases/download/v$version/app-$version-win-x64.zip"
  }
}
```

## 2. GitHub CLI App

```json
{
  "version": "1.2.3",
  "description": "Example CLI app.",
  "homepage": "https://github.com/owner/repo",
  "license": "Apache-2.0",
  "url": "https://github.com/owner/repo/releases/download/v1.2.3/app-1.2.3-windows-x64.zip",
  "hash": "sha256-placeholder",
  "bin": "app.exe",
  "checkver": {
    "github": "https://github.com/owner/repo"
  }
}
```

## 3. Official Portable Zip

```json
{
  "version": "1.2.3",
  "description": "Example portable app.",
  "homepage": "https://example.com",
  "license": "Freeware",
  "url": "https://downloads.example.com/app-1.2.3-win64.zip",
  "hash": "sha256-placeholder",
  "shortcuts": [
    [
      "app.exe",
      "App"
    ]
  ],
  "checkver": {
    "url": "https://example.com/download",
    "regex": "app-([\\d.]+)-win64\\.zip"
  }
}
```

## 4. Official Multi-Architecture App

```json
{
  "version": "1.2.3",
  "description": "Example multi-arch app.",
  "homepage": "https://example.com",
  "license": "MIT",
  "architecture": {
    "64bit": {
      "url": "https://downloads.example.com/app-1.2.3-x64.zip",
      "hash": "sha256-placeholder"
    },
    "32bit": {
      "url": "https://downloads.example.com/app-1.2.3-x86.zip",
      "hash": "sha256-placeholder"
    },
    "arm64": {
      "url": "https://downloads.example.com/app-1.2.3-arm64.zip",
      "hash": "sha256-placeholder"
    }
  }
}
```

## 5. Extractable Setup.exe

```json
{
  "version": "1.2.3",
  "description": "Example extractable installer.",
  "homepage": "https://example.com",
  "license": "Freeware",
  "url": "https://downloads.example.com/app-setup-1.2.3.exe#/dl.7z",
  "hash": "sha256-placeholder",
  "extract_dir": "app",
  "shortcuts": [
    [
      "app.exe",
      "App"
    ]
  ],
  "post_install": [
    "Remove-Item \"$dir\\$PLUGINSDIR\\*\" -Force -ErrorAction SilentlyContinue"
  ]
}
```

## 6. Mirror-Based Download

```json
{
  "version": "1.2.3",
  "description": "Example app from a trusted mirror.",
  "homepage": "https://example.com",
  "license": "MIT",
  "url": "https://mirror.example.cn/app/app-1.2.3-x64.zip",
  "hash": "sha256-placeholder",
  "checkver": {
    "url": "https://example.com/releases",
    "regex": "Version[ :]*([\\d.]+)"
  }
}
```

## 7. CLI + GUI

```json
{
  "version": "1.2.3",
  "description": "Example app with CLI and GUI.",
  "homepage": "https://example.com",
  "license": "MIT",
  "url": "https://downloads.example.com/app-1.2.3.zip",
  "hash": "sha256-placeholder",
  "bin": "app-cli.exe",
  "shortcuts": [
    [
      "app-gui.exe",
      "App"
    ]
  ]
}
```

## 8. With Persist

```json
{
  "version": "1.2.3",
  "description": "Example app with user data.",
  "homepage": "https://example.com",
  "license": "MIT",
  "url": "https://downloads.example.com/app-1.2.3.zip",
  "hash": "sha256-placeholder",
  "persist": [
    "config",
    "data"
  ]
}
```

## 9. With env_set

```json
{
  "version": "1.2.3",
  "description": "Example app requiring env vars.",
  "homepage": "https://example.com",
  "license": "MIT",
  "url": "https://downloads.example.com/app-1.2.3.zip",
  "hash": "sha256-placeholder",
  "env_set": {
    "APP_HOME": "$dir"
  }
}
```
