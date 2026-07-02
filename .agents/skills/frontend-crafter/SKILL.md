---
name: frontend-crafter
description: >
  Skill para diseñar y ejecutar features frontend en React + TypeScript + Vite + Tailwind v4.
  Aplica solo a frontend; no tocar backend ni BD.
trigger: "feature frontend, página, componente, estado, lib/api"
scope: frontend
---

# frontend-crafter

## Cuándo activarla
- Nueva página
- Componente reutilizable
- Cambio en `lib/api.ts`
- Estado global

## Pasos obligatorios
1. Leer `frontend/src/App.tsx` y `frontend/src/components/Layout.tsx`.
2. Leer `frontend/src/lib/api.ts`.
3. Implementar componente pequeño.
4. Incluir fallback, empty y error.
5. Agregar test unitario en `frontend/src/*.test.tsx`.

## Reglas duras
- Cero emojis.
- TypeScript estricto.
- Estado local primero; global solo si se comparte entre rutas.

## Criterio de done
- `npm run build` pasa
- test frontend verde
