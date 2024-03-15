from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from src.config import GLOBAL_ASSETS_WEBP


router = APIRouter(prefix="/assets", tags=["Assets"])


@router.get("/{path:path}")
async def get_asset(path: str) -> RedirectResponse:
    """
    redirect to the asset in the webp branch
    """

    path = path if path.endswith(".webp") else f"{path}.webp"
    return RedirectResponse(url=f"{GLOBAL_ASSETS_WEBP}/{path}")
