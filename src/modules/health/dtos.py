from pydantic import BaseModel

from src._settings import config
from src._version import get_version


class HealthCheckResponse(BaseModel):
    """
    Health check response model.
    """

    status: str = "ok"


class PingResponse(BaseModel):
    """
    Ping response model.
    """

    status: str = "pong"


class VersionResponse(BaseModel):
    """
    Version response model.
    """

    game_version: str = get_version()
    api_version: str = config.GAME_VERSION
