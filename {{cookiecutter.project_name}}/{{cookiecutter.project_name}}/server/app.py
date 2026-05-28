"""FastAPI application factory."""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from .models import Base, engine
from .routes import router

_BUNDLED_STATIC = Path(__file__).parent / "static"


def create_app() -> FastAPI:
    app = FastAPI(
        title="{{cookiecutter.project_name}}",
        version="{{cookiecutter.version}}",
    )

    Base.metadata.create_all(bind=engine)

    app.include_router(router)

    # ── Bundled UI static files ───────────────────────────────
    static_dir = _BUNDLED_STATIC
    index_html = static_dir / "index.html"

    if static_dir.is_dir() and index_html.is_file():
        app.mount(
            "/assets",
            StaticFiles(directory=str(static_dir / "assets")),
            name="static-assets",
        )

        @app.get("/favicon.ico")
        async def favicon():
            path = static_dir / "favicon.ico"
            if path.is_file():
                return FileResponse(str(path))
            raise HTTPException(status_code=404)

        @app.get("/{full_path:path}")
        async def serve_spa(full_path: str):
            if full_path.startswith(("api/",)):
                raise HTTPException(status_code=404)
            requested = static_dir / full_path
            if full_path and requested.is_file():
                return FileResponse(str(requested))
            return HTMLResponse(index_html.read_text())

    return app
