param(
    [Parameter(Mandatory = $true)]
    [string]$ManifestPath,

    [string]$AppName
)

$scoop = Get-Command scoop -ErrorAction SilentlyContinue
if (-not $scoop) {
    Write-Error "Scoop is not installed or not on PATH. Install Scoop first, then rerun: https://scoop.sh/"
    exit 1
}

$resolvedManifest = Resolve-Path -LiteralPath $ManifestPath -ErrorAction Stop

Write-Host "Installing manifest: $resolvedManifest"
& $scoop.Source install $resolvedManifest
if ($LASTEXITCODE -ne 0) {
    Write-Error "scoop install failed."
    exit $LASTEXITCODE
}

if ($AppName) {
    Write-Host "Running checkver for app: $AppName"
    & $scoop.Source checkver $AppName
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "scoop checkver failed. Verify checkver manually."
    }
}
else {
    Write-Host "Skipping scoop checkver because -AppName was not provided."
    Write-Host "Run manually if needed: scoop checkver <app>"
}

Write-Host "Uninstalling manifest package"
if ($AppName) {
    & $scoop.Source uninstall $AppName
}
else {
    Write-Host "Run manually if needed: scoop uninstall <app>"
}

if ($LASTEXITCODE -ne 0 -and $AppName) {
    Write-Warning "scoop uninstall reported a non-zero exit code."
}
