# Source Selection

Classify the user input before building or repairing a manifest.

## Source Categories

1. GitHub repository
2. GitHub release page
3. GitHub release asset URL
4. Official website
5. Official download page
6. Direct CDN URL
7. Mirror URL
8. Existing Scoop manifest
9. Scoop error message

## Routing

- GitHub repository, release page, or asset URL:
  Read [github-release-selection.md](github-release-selection.md).
- Official website, download page, direct CDN, or mirror:
  Read [official-site-selection.md](official-site-selection.md).
- Existing manifest:
  Read [manifest-patterns.md](manifest-patterns.md), then preserve good fields.
- Scoop error message:
  Read [troubleshooting.md](troubleshooting.md), then diagnose the current manifest.

## Trust Model

Prefer these in order:

1. Official website
2. Official GitHub, GitLab, or Gitee release
3. Official CDN
4. Official mirror
5. Well-known open source mirror

Avoid:

- third-party software portals
- repack sites
- forum attachments
- cloud-drive reposts
- short links
- unidentifiable CDN endpoints

## Editing Rule

When the user already provides a manifest, treat the task as repair-first:

- keep valid fields
- replace only broken assumptions
- explain each changed field
