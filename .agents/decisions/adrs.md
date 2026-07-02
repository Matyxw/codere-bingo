# ADR-001 — QR por compra firmado y con expiración
Se adopta un único `qr_payload` por compra, con cuerpo JSON mínimo + HMAC + expiración.

# ADR-002 — Sin precarga forzada en backend
Se permite generación dinámica de grillas en el momento de la compra hasta confirmar stock precargado.

# ADR-003 — Validación idempotente
La validación del ticket marca el primer escaneo como válido; escaneos repetidos retornan el mismo ticket marcado.

# ADR-004 — Trazabilidad antes que performance
Se prioriza registro durable sobre optimización extrema; cache solo después de confirmar cuellos de botella.

# ADR-005 — Frontend navegador primero
No se agrega app nativa ni agente local obligatorio en MVP; el flujo se resuelve desde el navegador del puesto.
