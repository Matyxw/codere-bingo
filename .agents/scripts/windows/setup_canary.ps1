$paths = @(
  "$env:USERPROFILE\Desktop\canary_token_admin.txt"
  "$env:USERPROFILE\Documents\canary_token_backup.txt"
  "D:\temp\canary_token_debug.txt"
)
$secret = -join ((65..90) + (97..122) | Get-Random -Count 32 | ForEach-Object {[char]$_})
foreach ($p in $paths) {
  New-Item -Path $p -ItemType File -Force | Set-Content -Value $secret
}
'CANARY_TOKENS_CREATED'
