
$filePath = "$PSScriptRoot\__pycache__\PID.json"

$PIDs = (Get-Content -Path $filePath -Raw | ConvertFrom-Json)

$PIDS | ForEach-Object {
    Stop-Process -Id $_
}