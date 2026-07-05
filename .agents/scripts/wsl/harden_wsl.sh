#!/usr/bin/env bash
set -euo pipefail

echo '[1/5] Dependencies...'
if ! command -v ufw >/dev/null 2>&1; then
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get install -y ufw fail2ban auditd audispd-plugins
else
  echo 'ufw already installed'
fi

echo '[2/5] UFW defaults + Tailscale allow...'
ufw --force disable >/dev/null 2>&1 || true
ufw default deny incoming
ufw default allow outgoing
ufw allow in from 100.0.0.0/10 to any port 22 proto tcp
ufw --force enable >/dev/null

echo '[3/5] Fail2Ban SSH...'
mkdir -p /etc/fail2ban/jail.d
cat > /etc/fail2ban/jail.d/ssh.conf << 'JEOF'
[sshd]
enabled = true
port = 22
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
findtime = 600
bantime = 3600
JEOF

echo '[4/5] Auditd baseline...'
sed -i 's/^GRUB_CMDLINE_LINUX=.*/GRUB_CMDLINE_LINUX="audit=1"/' /etc/default/grub || true
update-grub >/dev/null 2>&1 || true

echo '[5/5] Sudoers NOPASSWD...'
cat > /etc/sudoers.d/lucas_cardozo_nopasswd << 'SEOF'
lucas_cardozo ALL=(ALL) NOPASSWD: ALL
SEOF
chmod 440 /etc/sudoers.d/lucas_cardozo_nopasswd

echo 'HARDENING_DONE'
