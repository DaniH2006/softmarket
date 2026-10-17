# SoftMarket S.A. — Gestión de clientes

Módulo de ejemplo del informe **«Refactorizando el caos»**: separa validación, persistencia y
notificaciones aplicando los principios SOLID, con un flujo de trabajo Git/GitHub.

**Versión:** 1.0.0-dev

## Requisitos
- Python 3.10 o superior
- Git

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Pruebas y calidad
```bash
pytest --cov=src
ruff check src tests
black --check src tests
```

## Flujo de trabajo
- `main`: código estable (protegida). `develop`: integración.
- Ramas `feature/*`, `fix/*`, `release/x.y.z` y `hotfix/*`; todo cambio entra por Pull Request.
- Commits con formato `tipo(alcance): descripción` (feat, fix, test, refactor, docs).

Más detalle en [`docs/arquitectura.md`](docs/arquitectura.md) y
[`docs/decisiones-tecnicas.md`](docs/decisiones-tecnicas.md).
