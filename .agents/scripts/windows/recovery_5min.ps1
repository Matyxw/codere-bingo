param()
$ErrorActionPreference='SilentlyContinue'
Restart-Service -Name 'SunshineService' -Force -ErrorAction SilentlyContinue
Restart-Service -Name sshd -Force -ErrorAction SilentlyContinue
Restart-Service WinRM -Force -ErrorAction SilentlyContinue
tailscale::
if (Get-Command tailscale.exe -ErrorAction SilentlyContinue) { tailscale.exe up --accept-dns=false }
'RECOVERY_DONE'
