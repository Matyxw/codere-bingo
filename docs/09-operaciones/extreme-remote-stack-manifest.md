# Extreme Remote Stack — Manifiesto ejecutable
Control total + seguridad extrema confirmada y por confirmar.
## Capa 1 — Acceso visual extremo (RustDesk)
- [ ] RustDesk instalado
- [ ] Acceso desatendido con ID fijo
- [ ] Contraseña fija 32 caracteres
- [ ] 2FA TOTP obligatorio
- [ ] Whitelist IPs solo Tailscale
- [ ] Session recording local cifrado AES-256
- [ ] Auto-lock 5 min inactividad
## Capa 2 — Transporte seguro extremo (Tailscale)
- [x] Tailscale conectado: desktop-d4lreoo / android a13-de-maty
- [ ] ACLs personalizadas por servicio
- [ ] Taildrop activo
- [ ] RBAC por servicio
- [ ] Rotación claves WireGuard cada 24h
## Capa 3 — Acceso administrativo extremo (WinRM + SSH)
- [x] WinRM HTTP basic + AllowUnencrypted configurado
- [ ] WinRM con autenticación Certificate
- [x] OpenSSH instalado como servicio
- [ ] Solo claves ed25519 (sin password)
- [ ] Certificados rotación 1 año
- [ ] Firewall allow solo Tailscale para 22/5985/21115
- [ ] IPSec rules administración
## Capa 4 — Acceso Linux extremo (WSL)
- [x] sudoers NOPASSWD
- [ ] SSH Server WSL + claves ed25519
- [ ] Disco root cifrado LUKS
- [ ] AppArmor/SELinux restrictivo
- [ ] Auditd logging root
## Capa 5 — Seguridad perimetral extrema
- [x] UFW deny incoming + allow SSH Tailscale
- [x] Firewall Windows deny-all + allows explícitas
- [x] Fail2Ban sshd
- [ ] Rate limiting RustDesk
- [ ] Canary tokens
## Capa 6 — Cifrado extremo
- [ ] BitLocker TPM + PIN
- [ ] LUKS root WSL
- [ ] VeraCrypt containers
- [ ] Vault local para secrets
## Capa 7 — Monitoreo y auditoría extrema
- [ ] PowerShell Script Block Logging
- [ ] Windows Event Forwarding
- [ ] RustDesk session logs + video cifrado
- [ ] Tripwire
- [ ] Telegram bot alertas conexiones
## Capa 8 — Persistencia y recuperación extrema
- [ ] Auto-login Windows
- [ ] Servicios críticos auto-restart
- [ ] Backup cifrado cada 6h
- [ ] Imagen sistema en disco externo cifrado
- [ ] Script recuperación 5 min
