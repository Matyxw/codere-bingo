---
name: documentation-keeper
description: >
  Skill para mantender docs del repo y Obsidian sincronizadas con el sistema.
  No cambiar código; solo documentación.
trigger: "documentación, docs, Obsidian, ADR, README, onboarding"
scope: documentación
---

# documentation-keeper

## Cuándo activarla
- Feature nueva
- Cambio de stack
- Cambio operativo
- Onboarding

## Pasos obligatorios
1. Leer `docs/02-dominio/proyecto.md`.
2. Leer `docs/04-roadmap/roadmap.md`.
3. Actualizar `docs/08-features/*.md` o crear archivo por feature.
4. Actualizar `README.md` si cambia stack/comandos.
5. Actualizar `docs/01-estado/onboarding.md` si cambian pasos.

## Reglas duras
- Una feature = una doc mínima.
- ADR obligatoria para decisiones T1/T2.
- No documentar en conversaciones; solo en archivos.

## Criterio de done
- Docs actualizadas
- README sincronizado
- Onboarding reproducible
