# {{cookiecutter.project_name}}

> {{cookiecutter.description}}

## Project Structure

```
{{cookiecutter.project_name}}/              ← Project root (git repo)
├── pyproject.toml                           ← Package config (hatchling)
├── Makefile                                 ← Dev commands
├── tests/                                   ← pytest test suite
└── {{cookiecutter.project_name}}/           ← Python package
    ├── __init__.py                          ← Namespace package (extend_path)
    ├── cli/                                 ← CLI entry point (argklass)
    │   ├── __init__.py                      ← Command discovery + main()
    │   └── commands.py                      ← Built-in commands (serve, version)
    ├── server/                              ← FastAPI backend
    │   ├── __init__.py
    │   ├── run.py                           ← Uvicorn runner + ASGI entry
    │   ├── app.py                           ← create_app() factory, SPA serving
    │   ├── models.py                        ← SQLAlchemy base + engine
    │   ├── static/                          ← Built React app (gitignored)
    │   └── routes/                          ← API route modules
    │       ├── __init__.py                  ← Router aggregation
    │       └── health.py                    ← Example /health endpoint
    ├── plugins/                             ← Namespace package for extensions
    │   ├── __init__.py                      ← extend_path hook
    │   └── example/                         ← Example plugin
    ├── data/                                ← Bundled data files (JSON, CSV)
    ├── alembic/                             ← Database migrations
    │   ├── alembic.ini
    │   ├── env.py                           ← Migration env (imports models)
    │   ├── script.py.mako                   ← Migration template
    │   └── versions/                        ← Migration scripts
    └── ui/                                  ← React frontend (Vite + TypeScript)
        ├── package.json
        ├── vite.config.ts                   ← Dev proxy /api → :5001, build → server/static
        ├── index.html
        └── src/
            ├── main.tsx
            ├── App.tsx                      ← HashRouter, Chakra UI
            └── services/api.ts              ← API client (supports static mode)
```

## Setup

Prerequisites: Python >= {{cookiecutter.python_version}}, Node.js >= 20, uv

```bash
# Create virtual environment at project root
uv venv --python={{cookiecutter.python_version}}
source .venv/bin/activate

# Install Python package in editable mode
make install

# Install UI dependencies
cd {{cookiecutter.project_name}}/ui && npm install && cd ../..
```

## Development

```bash
# Run both frontend and backend (two terminals)
make front   # Vite dev server on :3000, proxies /api → :5001
make back    # FastAPI server on :5001 with auto-reload

# Or use the CLI directly
{{cookiecutter.project_name}} serve --port 5001
```

## Architecture

### Deployment Modes

| Mode | UI Served By | API |
|------|-------------|-----|
| Development | Vite `:3000` | FastAPI `:5001`, Vite proxies `/api` |
| Production (bundled) | FastAPI `server/static/` | Same process, `/api` prefix stripped |
| Static (GitHub Pages) | Pre-built HTML/JS | Pre-generated JSON, no server |

### Key Patterns

- **Namespace package**: `{{cookiecutter.project_name}}` uses `pkgutil.extend_path` — third-party packages can add `{{cookiecutter.project_name}}.plugins.*` modules
- **CLI plugins**: Commands discovered from `{{cookiecutter.project_name}}.cli.commands` + `{{cookiecutter.project_name}}.plugins` via argklass
- **SPA fallback**: Production build serves `index.html` for all non-API routes (HashRouter)
- **API prefix**: In dev, Vite strips `/api`; in production, `_StripApiPrefix` middleware does it

### Database

- SQLAlchemy 2.0 with declarative base
- SQLite by default (`DATABASE_URL` env var to override)
- Alembic for schema migrations (run from `{{cookiecutter.project_name}}/alembic/`)

## Build & Release

```bash
# Build UI + Python wheel
make build

# The wheel includes the built React app in server/static/
# Install and run as single process:
pip install dist/{{cookiecutter.project_name}}-*.whl
{{cookiecutter.project_name}} serve
```

## Testing

```bash
make test    # pytest
make lint    # ruff check
make format  # ruff fix + format
```
