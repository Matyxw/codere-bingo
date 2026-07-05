$ts = Get-Date -Format 'yyyyMMdd_HHmmss'
$backup = "D:\backups\config_$ts.zip"
$srcs = @(
  'C:\Program Files\Sunshine\config'
  "$env:APPDATA\sunshine"
  'C:\ProgramData\ssh'
  "$env:USERPROFILE\.ssh"
)
if (-not (Test-Path 'D:\backups')) { New-Item 'D:\backups' -ItemType Directory -Force | Out-Null }
Compress-Archive -Path $srcs -DestinationPath $backup -Force
"BACKUP_CREATED:$backup"
