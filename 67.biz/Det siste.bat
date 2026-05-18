# Start alle filene i mappen
Get-ChildItem -File | ForEach-Object {
    Start-Process $_.FullName
}

# Vent i 67 sekunder
Start-Sleep -Seconds 67

# Slå av PC-en og lukk åpne programmer
Stop-Computer -Force