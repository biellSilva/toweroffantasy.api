from typing import Literal

from fastapi import APIRouter

from src import __version__ as api_version
from src._settings import config

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[Literal["status"], Literal["ok"]]:
    """
    Health check endpoint.
    """
    return {"status": "ok"}


@router.get("/ping")
async def ping() -> dict[Literal["status"], Literal["pong"]]:
    """
    Ping endpoint.
    """
    return {"status": "pong"}


@router.get("/version")
async def version() -> dict[Literal["gameVersion", "apiVersion"], str]:
    """
    Version endpoint.
    """
    return {"gameVersion": config.GAME_VERSION, "apiVersion": api_version}
