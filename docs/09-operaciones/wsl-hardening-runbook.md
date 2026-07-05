# WSL Hardening — Runbook
- UFW deny incoming por defecto, allow SSH desde Tailscale (100.0.0.0/10)
- Fail2Ban sshd activo con maxretry=5
- sudoers NOPASSWD configurado en /etc/sudoers.d/lucas_cardozo_nopasswd
- audit: update-grub parcheado para audit=1
