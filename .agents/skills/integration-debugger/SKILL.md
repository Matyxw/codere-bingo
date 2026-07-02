---
name: integration-debugger
description: >
  Skill para resolver fallos de integración: imports, rutas, configuración, tests.
  No reescribir features; reparar caminos rotos.
trigger: "import error, route not found, validation error, config error, test failure"
scope: debugging
---

# integration-debugger

## Cuándo activarla
- Import circular
- Ruta 404/422
- Configuración de `.env`
- Test roto por ruta
- CI rota por paths incorrectos

## Pasos obligatorios
1. Leer `docs/09-operaciones/testing.md`.
2. Reproducir fallo en local.
3. Marcar causa raíz en `docs/06-sesiones/YYYY-MM-DD.md`.
4. Aplicar parche mínimo en ruta/config.
5. Verificar build/test mínimo.

## Reglas duras
- No cambiar dominio sin ADR.
- No introducir dependencias nuevas sin skill `infra-operator`.

## Criterio de done
- Fallo reproducido y reparado
- Sesión documentada
