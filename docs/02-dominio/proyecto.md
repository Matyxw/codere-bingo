# Codere Bingo — Documentación de Dominio

## Resumen del sistema
Sistema de venta de cartones de bingo en sala presencial, con emisión de ticket QR, impresión local por puesto y validación en sorteo.

## Actores
- Operador de ventanilla
- Cliente / jugador
- Supervisor de sala / sorteo
- Sistema de hosting Codere

## Flujo principal
1. El operador abre una compra desde el navegador del puesto.
2. El sistema valida rango, genera grillas y arma el QR único.
3. El sistema envía la impresión del ticket al puesto vinculado.
4. El cliente juega con el ticket impreso.
5. En el sorteo, el operador escanea el QR y el sistema valida legibilidad, unicidad y Ownership del ticket.

## Reglas duras del dominio
- QR único e irrepetible por compra/ticket.
- Rango de compra: mínimo 1 cartón, máximo 6 por transacción.
- Medio de pago: exclusivamente presencial en efectivo para este MVP.
- Trazabilidad completa de cada operación para cumplimiento regulatorio.

## Supuestos
- Una compra puede tener 1 o más cartones; el ticket puede representar la compra completa.
- El puesto ya tiene una impresora/vínculo registrado en `Puesto.impresora_url`.
- El QR incluye datos mínimos + firma HMAC + expiración.

## Preguntas abiertas
- ¿Stock precargado o generación dinámica de cartones?
- ¿QR por compra o por cartón?
- ¿Modelo exacto de impresora/local en cada puesto?
- ¿Una partida por vez o múltiples sorteos concurrentes?
