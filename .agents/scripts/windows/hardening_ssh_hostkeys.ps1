$homedir = 'C:\ProgramData\ssh'
$hostKeyPath = Join-Path $homedir 'ssh_host_ed25519_key'
$hostPubPath = Join-Path $homedir 'ssh_host_ed25519_key.pub'
if (-not (Test-Path $hostKeyPath)) {
  ssh-keygen -t ed25519 -f $hostKeyPath -N '' -q
}
$pub = Get-Content $hostPubPath
$sshdConfig = Join-Path $homedir '..\..\ProgramData\ssh\sshd_config'
if (-not (Test-Path $sshdConfig)) { $sshdConfig = 'C:\Program Files\OpenSSH\etc\sshd_config' }
(Get-Content $sshdConfig) -replace '^HostKey\s+.*','#HostKey __PROGRAMDATA__/ssh/ssh_host_rsa_key' | Set-Content $sshdConfig
Add-Content $sshdConfig "`nHostKey __PROGRAMDATA__/ssh/ssh_host_ed25519_key"
Restart-Service sshd -Force -ErrorAction SilentlyContinue
'ED25519_HOSTKEY_ENFORCED'
