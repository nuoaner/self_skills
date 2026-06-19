# Official Site Selection

Use this file for official websites, download pages, direct CDN links, and mirror links.

## Source Priority

Prefer these sources:

1. Versioned official download URL
2. Official download page HTML
3. Official release notes page
4. Official JSON API
5. Official appcast or update XML
6. Official checksum file

## Avoid

- unofficial download aggregators
- bundleware portals
- shortened links
- opaque CDN links with no ownership signal

## Checkver

For official sites, prefer:

```json
"checkver": {
  "url": "https://example.com/download",
  "regex": "App[._ -]([\\d.]+)[._ -]win64\\.zip"
}
```

Choose a URL whose content is stable and machine-readable.

## Autoupdate

Add `autoupdate` only if the final download URL can be templated safely.

Examples:

- Good: `https://downloads.example.com/app/$version/app-$version-x64.zip`
- Good: `https://cdn.example.com/releases/$majorVersion.$minorVersion/app-$version.exe`
- Bad: `https://example.com/latest/windows`
- Bad: short-lived signed URLs with timestamps
- Bad: links that require parsing a session token

## Mirror Use

- A mirror can be used for the manifest `url` if it is trusted and stable.
- Prefer upstream pages for version detection.
- If upstream and mirror versioning diverge, call that out explicitly.

## Verification Targets

When the official site is the source, verify locally when possible:

- final redirect target
- checksum availability
- archive root folder
- portable versus installer behavior
