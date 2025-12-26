
Test-NetConnection `
    -ComputerName localhost `
    -Port 8000 `
    -InformationLevel Quiet `
    | ConvertTo-Json | Write-Host
