"""Health check route."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/version")
async def version():
    return {"version": "{{cookiecutter.version}}"}
