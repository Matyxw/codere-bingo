#!/usr/bin/env bash
# Hardening WSL-side: UFW + auditd + fail2ban prep
set -euo pipefail

echo '[1/5] Configuring UFW default deny...'
if ! command -v ufw >/dev/null 2>&1; then
  apt-get update
  apt-get install -y ufw
fi
mkdir -p /etc/ufw/applications.d
sed -i 's/^IPv6=.*/IPv6=no/' /etc/default/ufw || true
cat > /etc/ufw/applications.d/tailscale <<'UEOF'
[tailscale]
title=Tailscale
description=Tailscale VPN
ports=41641/udp
UEOF
ufw --force disable
ufw default deny incoming
ufw default deny outgoing
ufw allow out 41641/udp comment 'Tailscale VPN'
ufw allow out 53 comment 'DNS via Tailscale'
ufw allow out 123/udp comment 'NTP via Tailscale'
ufw --force enable
ufw status verbose

echo '[2/5] Enabling auditd...'
apt-get install -y auditd audispd-plugins 2>/dev/null || true
systemctl enable auditd || true
cat > /etc/audit/rules.d/audit.rules <<'AEOF'
-w /etc/sudoers -p wa -k sudoers
-w /etc/sudoers.d/ -p wa -k sudoers
-w /usr/bin/sudo -p x -k sudo_bins
-w /etc/ssh/ -p wa -k ssh_config
-w /etc/ufw/ -p wa -k firewall
-w /var/log/auth.log -p wa -k auth_logs
-w /root/ -p rwxa -k root_home
-w /home/lucas_cardozo/ -p rwxa -k user_home
-A always,exit -F arch=b64 -S execve -k exec_tracking
AEOF
augenrules --load || systemctl restart auditd || true
auditctl -l | grep -E 'sudoers|ssh_config|firewall|exec_tracking' || true

echo '[3/5] Fail2Ban prep...'
apt-get install -y fail2ban 2>/dev/null || true
cat > /etc/fail2ban/jail.local <<'FEOF'
[DEFAULT]
bantime = 1h
findtime = 10m
maxretry = 3
backend = auto

[sshd]
enabled = true
port = ssh
logpath = /var/log/auth.log
maxretry = 3
FEOF
systemctl enable fail2ban || true
systemctl restart fail2ban || true
fail2ban-client status sshd || true

echo '[4/5] Sudoers prep (may need your password once)...'
if [ -f /etc/sudoers.d/lucas_cardozo ]; then
  echo 'sudoers already configured'
else
  echo 'lucas_cardozo ALL=(ALL) NOPASSWD: ALL' > /tmp/lucas_cardozo_sudoers
  sudo chmod 440 /tmp/lucas_cardozo_sudoers
  sudo mv /tmp/lucas_cardozo_sudoers /etc/sudoers.d/lucas_cardozo
  echo 'sudoers configured'
fi

echo '[5/5] Summary'
echo 'Ufw status:'
ufw status verbose
echo 'Audit rules loaded'
echo 'Fail2ban status:'
fail2ban-client status || true
