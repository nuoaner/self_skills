param([Parameter(Mandatory = $true)][string]$ManifestPath, [string]$AppName, [switch]$AllowInstall)
$ErrorActionPreference = "Stop"
$path = (Resolve-Path -LiteralPath $ManifestPath).Path
$manifest = Get-Content -LiteralPath $path -Raw -Encoding UTF8 | ConvertFrom-Json -ErrorAction Stop
if (-not $manifest.version -or (-not $manifest.url -and -not $manifest.architecture)) { throw "Missing version or download URL." }
Write-Host "JSON and required fields OK. Static validation only; no download/hash verification."
if (-not $AllowInstall) { Write-Host "Read-only: no install or uninstall performed."; exit 0 }
$scoop = Get-Command scoop -ErrorAction Stop
Write-Warning "Explicit installation requested. Use a disposable environment; this script never uninstalls."
& $scoop.Source install $path
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
if ($AppName) { & $scoop.Source checkver $AppName; if ($LASTEXITCODE -ne 0) { Write-Warning "checkver failed" } }
