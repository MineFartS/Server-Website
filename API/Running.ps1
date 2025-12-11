
$filePath = "$PSScriptRoot\__pycache__\PID.json"

$PIDs = (Get-Content -Path $filePath -Raw | ConvertFrom-Json)

$processes = $PIDS | ForEach-Object {
    
    try {
        Get-Process -Id $_ -ErrorAction SilentlyContinue
    } catch {
        Write-Host 'false'
        exit
    }

}

if ($processes.Length -gt 0) {
    Write-Host 'true'
} else {
    Write-Host 'false'
}
