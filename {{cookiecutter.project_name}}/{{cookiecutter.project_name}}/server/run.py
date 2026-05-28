"""Server runner — starts the FastAPI server with uvicorn."""

import os
import sys


class _StripApiPrefix:
    """ASGI middleware that strips /api prefix for production single-process mode."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] in ("http", "websocket"):
            path = scope.get("path", "")
            if path.startswith("/api"):
                scope = dict(scope)
                scope["path"] = path[4:] or "/"
        await self.app(scope, receive, send)


def entry():
    """ASGI entry point (used by uvicorn okaasan.server.run:entry)."""
    app = create_app()
    return _StripApiPrefix(app)


def create_app():
    from .app import create_app as _create
    return _create()


def main():
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5001"))
    reload = os.getenv("ENV", "development") == "development"

    print(f"\nStarting {{cookiecutter.project_name}} server...")
    print(f"  Host: {host}")
    print(f"  Port: {port}")
    print(f"  Reload: {reload}")
    print(f"  Access at: http://localhost:{port}")
    print("=" * 50)

    try:
        uvicorn.run(
            "{{cookiecutter.project_name}}.server.run:entry",
            host=host,
            port=port,
            reload=reload,
        )
    except KeyboardInterrupt:
        print("\nServer stopped")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
