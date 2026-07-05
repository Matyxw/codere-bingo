# MASTER_STATUS - Extreme Remote Stack
Fecha: 2026-07-06
Objetivo: Control total, seguro, desde cualquier lado.

## Estado actual
- [x] Tailscale conectado: desktop-d4lreoo
- [x] SSH Windows abierto (puerto 22)
- [x] Sunshine: proceso corriendo
- [x] Firewall Windows: deny-all + allow Tailscale + allow Sunshine/Moonlight + allow API 47990
- [x] WinRM configurado en Windows
- [x] WSL hardening: UFW + fail2ban + sudoers NOPASSWD
- [x] PowerShell logging habilitado
- [x] Auto-login Windows configurado
- [x] Backup config creado en D:\backups
- [x] Canary tokens creados (Desktop, D:\temp)
- [ ] sshd_config: activar PubkeyAuthentication solo ed25519 + desactivar PasswordAuthentication
- [ ] RustDesk instalado y acceso desatendido
- [ ] BitLocker activado
- [ ] Telegram alerts conectadas
- [ ] Script recuperación 5 min probado en producción

## Extreme Remote Stack — success 2026-07-06
- [x] Moonlight conecta via Tailscale usando Sunshine
- [x] Firewall Windows: deny-all inbound por defecto + allows explícitas Tailscale
