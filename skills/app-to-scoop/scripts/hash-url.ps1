param(
    [Parameter(Mandatory = $true)]
    [string]$Url
)

$scoop = Get-Command scoop -ErrorAction SilentlyContinue
if (-not $scoop) {
    Write-Error "Scoop is not installed or not on PATH. Install Scoop first, then rerun: https://scoop.sh/"
    exit 1
}

try {
    & $scoop.Source hash $Url
    exit $LASTEXITCODE
}
catch {
    Write-Error $_
    exit 1
}
