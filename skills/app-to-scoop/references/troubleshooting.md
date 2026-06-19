# Troubleshooting

Use this file when the user provides a Scoop error or a broken manifest.

| Error | Common cause | Fix |
| --- | --- | --- |
| `Hash check failed` | Hash is stale, URL now points to a different file, or download redirects changed the payload | Recompute the hash and verify the final URL |
| `Can't shim` | `bin` points to the wrong executable or nested path | Inspect the archive and correct the executable path |
| `Couldn't find manifest` | Wrong filename or bucket path | Verify `bucket/app.json` and bucket registration |
| `checkver failed` | Wrong GitHub URL or regex mismatch | Fix `checkver.github` or `checkver.url` plus `regex` |
| `autoupdate failed` | URL template is wrong | Recheck `$version`, `v$version`, and filename stability |
| `Executable not found after extraction` | `extract_dir` is wrong or archive root changed | Inspect the extracted directory layout |
| `GUI app has no shortcut` | Missing `shortcuts` field | Add a verified shortcut entry |
| `Config lost after update` | Missing `persist` field | Persist the verified config or data directories |
| `Installer leaves junk behind` | Temporary directories like `$PLUGINSDIR` were not cleaned | Add deterministic cleanup in `post_install` |

## Repair Strategy

1. Keep fields that are already correct.
2. Re-verify the source URL and asset type.
3. Recompute hash locally instead of guessing.
4. Inspect the archive before changing `bin`, `shortcuts`, or `extract_dir`.
5. Re-test with local Scoop commands.
