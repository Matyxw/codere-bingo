param()
$ErrorActionPreference='SilentlyContinue'
$token = $env:TELEGRAM_BOT_TOKEN
$chatId = $env:TELEGRAM_CHAT_ID
if (-not $token -or -not $chatId) {
  'MISSING_TELEGRAM_ENV'
  exit 1
}
function Send-Telegram($text) {
  $url = "https://api.telegram.org/bot$token/sendMessage"
  Invoke-Rest -Method Post -Uri $url -Body @{ chat_id=$chatId; text=$text } | Out-Null
}
$svc = @('SunshineService','sshd','WinRM')
$statuses = foreach ($s in $svc) {
  $st = Get-Service -Name $s -ErrorAction SilentlyContinue
  if ($st) { "$s=$($st.Status)" } else { "$s=NotFound" }
}
$ips = (Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias 'Tailscale','Ethernet','Wi-Fi' -ErrorAction SilentlyContinue | Select-Object -ExpandProperty IPAddress) -join ', '
$msg = @(
  'EXTREME_STACK_STATUS'
  "Host=$(HostName)"
  "User=$env:USERNAME"
  "IPs=$ips"
  ($statuses -join ' | ')
  'Tailscale=' + (Get-Process -Name 'tailscale*' -ErrorAction SilentlyContinue | Measure-Object | Select-Object -ExpandProperty Count)
) -join "`n"
Send-Telegram $msg
'TELEGRAM_ALERT_SENT'
