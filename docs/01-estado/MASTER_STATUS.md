# MASTER_STATUS - Extreme Remote Stack
Fecha: 2026-07-06
Objetivo: Control total, seguro, desde cualquier lado.

## Estado actual
- [x] Tailscale conectado: desktop-d4lreoo
- [x] SSH Windows: servicio sshd corriendo en :22
- [x] Sunshine: proceso corriendo
- [x] Firewall Windows: deny-all + allow Tailscale + allow Sunshine/Moonlight + allow API 47990
- x] Sunshine API 47990: verified post-restart
- [ ] WinRM: configurado y conectable desde Tailnet
- x] WSL hardening: UFW + fail2ban + sudoers NOPASSWD
- [ ] BitLocker Windows
- [ ] LUKS WSL (si aplica)
- [ ] HashiCorp Vault local
- [ ] Telegram bot alertas
- [ ] Backup cifrado + imagen sistema
- [ ] Auto-login Windows
- [ ] Script recuperación 5 min
## Extreme Remote Stack — success 2026-07-06
- [x] Moonlight conecta via Tailscale usando Sunshine
- [x] Firewall Windows: deny-all inbound por defecto + allows explícitas Tailscale
## Extreme Remote Stack — vecinos de acceso
- [x] SSH Windows (puerto 22)
- [x] WinRM configurado
- [x] Tailscale direct
- [x] Sunshine+Moonlight streaming funcionando
- [x] Firewall deny-all + allows Tailscale específicos
- [x] WSL hardening (UFW/Fail2Ban/sudoers)

## Siguiente
- [ ] RustDesk instalado como servicio
- [ ] Auto-login Windows
- [ ] BitLocker + backup recovery
- [ ] Telegram bot alertas
- [ ] Script recuperación 5 min
## Estado ejecutado por usuario
- [x] PowerShell logging habilitado
- [x] Windows autologin configurado
- [x] Backup config creado en D:\backups
- [x] Canary tokens creados (Desktop, D:\temp)
- [ ] Canary token Documents pendiente por ruta faltante
