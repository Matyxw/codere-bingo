$sshdConfig = 'C:\ProgramData\ssh\sshd_config'
if (-not (Test-Path $sshdConfig)) { $sshdConfig = 'C:\Program Files\OpenSSH\etc\sshd_config' }
$conf = Get-Content $sshdConfig
$map = @{
  'PubkeyAuthentication' = 'yes'
  'PasswordAuthentication' = 'no'
  'AuthorizedKeysFile' = '.ssh/authorized_keys'
  'PermitEmptyPasswords' = 'no'
  'ChallengeResponseAuthentication' = 'no'
  'UsePAM' = 'yes'
  'HostKey' = '__(PROGRAMDATA__/ssh/ssh_host_ed25519_key'
}
foreach ($k in $map.Keys) {
  if ($k -eq 'HostKey') {
    $conf = $conf -replace '^#?\s*HostKey\s+.*','#HostKey __PROGRAMDATA__/ssh/ssh_host_rsa_key'
    if (-not ($conf -match 'ssh_host_ed25519_key')) { $conf += "`nHostKey __PROGRAMDATA__/ssh/ssh_host_ed25519_key" }
  } else {
    $conf = $conf -replace "^#?\s*$k\s+\w+", "$k $($map[$k])"
    if (-not ($conf -match "^$k ")) { $conf += "`n$k $($map[$k])" }
  }
}
Set-Content $sshdConfig $conf
Restart-Service sshd -Force -ErrorAction SilentlyContinue
'SSH_HARDENING_DONE'
