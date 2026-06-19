# Extras-CN Patterns

Use this file for community-style packaging patterns aligned with CN-oriented Scoop buckets such as `Scoopforge/Extras-CN`.

## Preferred Field Order

Use a stable, readable field order:

1. `version`
2. `description`
3. `homepage`
4. `license`
5. `architecture` or top-level `url` / `hash`
6. `extract_dir`
7. `extract_to`
8. `bin`
9. `shortcuts`
10. `persist`
11. `env_set`
12. `installer`
13. `post_install`
14. `checkver`
15. `autoupdate`
16. `notes`

## Bucket Style

- Prefer GitHub release assets instead of source archives.
- Use `architecture` for multi-arch apps.
- Use `checkver.github` for GitHub-hosted releases.
- Use `checkver.url` plus `regex` for official websites.
- Use `autoupdate.architecture` when each architecture follows a stable naming template.
- Use `shortcuts` for GUI apps.
- Use `bin` for CLI tools.
- Use both when an app exposes both experiences.

## Persist Patterns

Common candidates for `persist`:

- `config`
- `settings`
- `data`
- `plugins`
- `profiles`
- `user-data`
- `Downloads`
- app-specific workspace folders

Only persist paths that clearly represent user state.

## Extractable Installer Patterns

- Consider `#/dl.7z` when a setup executable can be unpacked by 7-Zip.
- Use `post_install` to remove `$PLUGINSDIR` or temporary installer leftovers when deterministic.
- Do not run the installer merely to discover files if archive inspection is enough.

## Mirror Strategy

- A CN bucket may use a trusted mirror for download speed.
- Version discovery should still prefer upstream official pages when possible.
- If the mirror filename is not stable, avoid `autoupdate`.
