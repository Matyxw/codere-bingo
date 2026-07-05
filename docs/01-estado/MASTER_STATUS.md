# MASTER_STATUS - Extreme Remote Stack
Fecha: 2026-07-06
Objetivo: Control total, seguro, desde cualquier lado.

## Estado actual
- [x] Tailscale conectado: desktop-d4lreoo
- [x] SSH Windows abierto (puerto 22)
- [x] Sunshine+Moonlight streaming funcionando
- [x] Firewall Windows: deny-all + allows explícitas Tailscale
- [x] WinRM configurado
- [x] WSL hardening: UFW + fail2ban + sudoers NOPASSWD
- [x] PowerShell logging habilitado
- [x] Auto-login Windows configurado
- [x] Backup config creado en D:\backups
- [x] Canary tokens creados (Desktop, Documents, D:\temp)
- [x] go.bat ejecuta stack completo
- [x] stack_status.bat para verificación rápida
- [ ] sshd_config: activar PubkeyAuthentication solo ed25519 + desactivar PasswordAuthentication
- [ ] RustDesk instalado y acceso desatendido
- [ ] BitLocker TPM+PIN
- [ ] Telegram alerts conectadas
- [ ] Script recuperación 5 min probado en producción

## Extreme Remote Stack — success 2026-07-06
- [x] Moonlight conecta via Tailscale usando Sunshine
- [x] Firewall Windows: deny-all inbound por defecto + allows explícitas Tailscale
