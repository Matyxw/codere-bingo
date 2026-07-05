# Extreme Remote Stack — Playbook completo
Objetivo: control total seguro desde cualquier lado.
PC: DESKTOP-D4LREOO
Usuario: lucas_cardozo

## Capa 1 — Sunshine + Moonlight (streaming extremo)
Puertos: 47984, 47989, 47990, 47998, 47999, 48010, 8080, 8443
Config: C:\Program Files\Sunshine\config\sunshine.conf
Backup: sunshine.conf.bak
Servicio: SunshineService (auto)
Log: C:\Program Files\Sunshine\config\sunshine.log

## Capa 2 — Tailscale
IP local: 192.168.100.2
IP tailscale: 100.115.185.57
Android: 100.122.138.53

## Capa 3 — WinRM
Listo y funcionando
Puerto: 5985
Protocolo: HTTP + Basic + AllowUnencrypted

## Capa 4 — SSH
Servicio: sshd
Puerto: 22
Llaves: agregar en C:\Users\...\.ssh\authorized_keys

## Checklist rápido
- [ ] SunshineService reinició y 47990 quedó LISTENING
- [ ] Moonlight muestra HTTPS Port: 47990 (no 0)
- [ ] Tailscale status muestra devices active
- [ ] Firewall: deny all inbound except Tailscale + Sunshine
- [ ] WinRM: test-winrm.ps1 pasa
- [ ] WSL: sudoers + ufw + auditd + fail2ban
