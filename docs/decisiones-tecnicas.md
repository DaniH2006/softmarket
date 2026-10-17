# Decisiones técnicas

## 1. Contratos con `typing.Protocol`
- **Decisión:** definir `RepositorioClientes` y `Notificador` como Protocol.
- **Alternativas:** clases abstractas (ABC); depender directamente de SQL/SMTP.
- **Motivo:** contratos pequeños, sin herencia obligatoria y fáciles de reemplazar por fakes en pruebas.

## 2. Modelo de ramas ligero
- **Decisión:** `main`, `develop`, `feature/*`, `fix/*`, `release/*`, `hotfix/*`.
- **Motivo:** equipo pequeño; ramas de vida corta y revisión obligatoria por Pull Request.

## 3. Integración continua
- **Decisión:** ejecutar pruebas, análisis estático (Ruff) y formato (Black) en cada PR.
- **Motivo:** detectar regresiones antes de integrar.
