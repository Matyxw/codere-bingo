# Operación — Agente local

## Instalación
1. Definir `IMPRESORA_URL` y `WEB_PRINT_TOKEN` en `.env` del puesto.
2. Ejecutar agente local.
3. Verificar endpoint `/health`.

## Prueba
```bash
curl -H "Authorization: Bearer $WEB_PRINT_TOKEN" http://127.0.0.1:PORT/health
```

## Troubleshooting
- Puerto ocupado: cambiar `PORT`
- Token inválido: regenerar en backend
- Sin impresión: verificar driver de impresora en el puesto
