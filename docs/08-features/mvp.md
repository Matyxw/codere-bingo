# MVP — Mínimo viable ejecutable
Objetivo: vender cartones, imprimir ticket con QR, escanear QR en sorteo, evitar duplicados y dejar trazabilidad.
No incluye: pasarela de pago online, app móvil, reportes avanzados, multi-casino avanzado.

## Backend
- API FastAPI.
- SQLAlchemy async + Alembic.
- Modelos mínimos: Compra, Carton, Sorteo, Operador, Puesto, TicketQr.
- QR firmado + expiración.
- Validación idempotente.

## Frontend
- React + Vite + Tailwind v4.
- Flujo: nueva compra → resumen → imprimir → validar.

## Impresión local
- Impresora térmica por puesto activada por servicio local/webhook local.

## Trazabilidad
- Auditoría mínima: fecha, puesto, operador, cartones, importe, ticket/QR.
