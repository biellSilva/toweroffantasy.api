from fastapi import APIRouter

from src.modules.health.dtos import HealthCheckResponse, PingResponse, VersionResponse

router = APIRouter()


@router.get("/health")
async def health_check() -> HealthCheckResponse:
    """
    Health check endpoint.
    """
    return HealthCheckResponse()


@router.get("/ping")
async def ping() -> PingResponse:
    """
    Ping endpoint.
    """
    return PingResponse()


@router.get("/version")
async def version() -> VersionResponse:
    """
    Version endpoint.
    """
    return VersionResponse()
