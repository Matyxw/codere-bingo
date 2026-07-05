# Admin Execution Playbook — Extreme Stack
Objetivo: ejecutar TODO el stack con 1 solo bloque en PowerShell (Administrador).

## Orden exacto recomendado
1. `D:\codigos\importante\Codere-Bingo\.agents\scripts\windows\hardening_ssh_hostkeys.ps1`
2. `D:\codigos\importante\Codere-Bingo\.agents\scripts\windows\hardening_ssh_enforce.ps1`
3. `D:\codigos\importante\Codere-Bingo\.agents\scripts\windows\ipsec_winrm_https.ps1`
4. `D:\codigos\importante\Codere-Bingo\.agents\scripts\windows\bitlocker_enable.ps1`
5. `D:\temp\go.bat`
6. `D:\temp\stack_status.bat`

## Notas
- Revisar credenciales y canary tokens después de ejecutar.
- Si falla alguno, repetirlo tras clic en UAC.
