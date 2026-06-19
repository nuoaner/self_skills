param(
    [Parameter(Mandatory = $true)]
    [string]$Url
)

$tempRoot = Join-Path $env:TEMP ("app-to-scoop-" + [guid]::NewGuid().ToString("N"))
$archivePath = Join-Path $tempRoot "payload.bin"
$extractPath = Join-Path $tempRoot "extract"

New-Item -ItemType Directory -Path $tempRoot | Out-Null
New-Item -ItemType Directory -Path $extractPath | Out-Null

try {
    Write-Host "Downloading archive to $archivePath"
    Invoke-WebRequest -Uri $Url -OutFile $archivePath

    $sevenZip = Get-Command 7z -ErrorAction SilentlyContinue
    if ($sevenZip) {
        Write-Host "Listing archive contents with 7-Zip"
        & $sevenZip.Source l $archivePath
        Write-Host ""
        Write-Host "Extracting archive to inspect file layout"
        & $sevenZip.Source x $archivePath "-o$extractPath" -y | Out-Host
    }
    else {
        Write-Warning "7z was not found on PATH. Attempting Expand-Archive for zip-like payloads."
        Expand-Archive -LiteralPath $archivePath -DestinationPath $extractPath -Force
    }

    Write-Host ""
    Write-Host "Candidate executables:"
    Get-ChildItem -Path $extractPath -Recurse -Include *.exe,*.cmd,*.bat | ForEach-Object {
        $_.FullName.Replace($extractPath + "\", "")
    }

    Write-Host ""
    Write-Host "Top-level directories:"
    Get-ChildItem -Path $extractPath -Directory | ForEach-Object {
        $_.Name
    }

    Write-Host ""
    Write-Host "Review these paths for bin, shortcuts, extract_dir, and persist."
}
catch {
    Write-Error $_
    exit 1
}
