# Sunshine + Moonlight — Runbook probado
## Config confirmada
- Host: 100.115.185.57
- Puerto HTTPS: 47990
- Puertos datos: 47984, 47989, 48010, 47998, 47999
- Firewall: deny-all inbound por defecto + allow explícitas Tailscale
- Servicio: SunshineService
- Config: C:\Program Files\Sunshine\config\sunshine.conf
- Credenciales API: sunshine / pcdecasa3225

## Reparación rápida si Moonlight muestra OFFLINE
1. PowerShell admin: Restart-Service -Name 'SunshineService' -Force
2. Celular: cerrar Moonlight, borrar datos de app, re-agregar manual 100.115.185.57:47990
3. Si pide PIN, usar el mostrado en Sunshine UI local

## Nota
- PowerShell Invoke-WebRequest puede fallar con HTTPS local por schannel; usar curl.exe para validar.
