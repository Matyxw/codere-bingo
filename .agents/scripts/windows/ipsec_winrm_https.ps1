New-NetFirewallRule -Name 'Allow-WinRM-Tailscale-HTTPS' -DisplayName 'Allow WinRM HTTPS from Tailscale' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -RemoteAddress 100.0.0.0/10 -LocalPort 5986
'IPSEC_WINRM_HTTPS_READY'
