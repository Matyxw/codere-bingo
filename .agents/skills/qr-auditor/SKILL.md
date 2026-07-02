---
name: qr-auditor
description: >
  Skill exclusiva para generar, firmar, validar y auditar tickets QR.
  No modificar modelos sin ADR aprobado.
trigger: "QR, ticket, validación, HMAC, sorteo"
scope: backend
---

# qr-auditor

## Cuándo activarla
- Cambio en formato QR
- Cambio en HMAC
- Validación de ticket
- Migración QR existente

## Pasos obligatorios
1. Leer `.agents/decisions/adrs.md`.
2. Leer `backend/core/services.py`.
3. Verificar unicidad y expiración.
4. Actualizar test E2E de validación.
5. Documentar cambio en `docs/02-dominio/proyecto.md`.

## Reglas duras
- QR único por compra/ticket.
- Sin datos sensibles en el payload.
- Primera validación marca `usado=True`; siguientes son idempotentes.

## Criterio de done
- E2E compra→QR→validación verde
- ADRs actualizadas
