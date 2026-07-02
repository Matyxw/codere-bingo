---
name: security-guardian
description: >
  Skill para endurecer seguridad aplicada: headers, CORS, rate limit, secrets, QR/HMAC.
  No romper flujo operativo; priorizar cumplimiento.
trigger: "seguridad, CORS, headers, rate limit, secret, QR, HMAC, auditoría"
scope: seguridad
---

# security-guardian

## Cuándo activarla
- Cambio en CORS
- Cambio en auth/secrets
- Cambio en rate limiting
- Auditoría post-incidente

## Pasos obligatorios
1. Leer `docs/09-operaciones/security.md`.
2. Leer `backend/core/middleware.py`.
3. Validar CORS por ambiente.
4. Verificar que no haya secrets en código.
5. Actualizar checklist de seguridad.

## Reglas duras
- Nunca `*` en producción.
- Rotar `SECRET_KEY` por despliegue.
- Validar que toda ruta crítica quedé auditada.

## Criterio de done
- Security headers activos
- CORS productivo
- Documentación sincronizada
