#!/usr/bin/env bash
# Script para configurar OpenSSH Server en Windows
# Debe ejecutarse en PowerShell como Administrador

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "\n  Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0;\n  Start-Service sshd;\n  Set-Service -Name sshd -StartupType Automatic;\n  New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22;\n  'OpenSSH Server configurado'\n"