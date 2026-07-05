# SSH Windows hardening — runbook
- Config base: C:\ProgramData\ssh\sshd_config
- Llave pública WSL copiada a C:\Users\Lucas cardozo\.ssh\authorized_keys
- Cambios recomendados manuales:
  PubkeyAuthentication yes
  PasswordAuthentication no
  AuthorizedKeysFile .ssh/authorized_keys
  PermitEmptyPasswords no
  ChallengeResponseAuthentication no
