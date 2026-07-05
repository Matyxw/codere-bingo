@echo off
powershell -NoProfile -Command "[Net.ServicePointManager]::SecurityProtocol='Tls12'; Get-Service SunshineService,sshd,WinRM | Format-Table Name,Status -AutoSize; netstat -ano | Select-String '47990|22|5985'; tailscale status"
