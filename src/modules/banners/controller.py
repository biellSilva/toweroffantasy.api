from typing import Annotated

from fastapi import APIRouter, Query

from src.modules._paginator import Pagination
from src.modules.banners.dtos import Banner, GetBanners
from src.modules.banners.repository import BannerRepository
from src.modules.banners.service import BannerService

router = APIRouter(prefix="/banners", tags=["banners"])

SERVICE = BannerService(BannerRepository())


@router.get("")
async def get_banners(
    params: Annotated[GetBanners, Query()],
) -> Pagination[Banner]:
    return await SERVICE.get_banners(params)


@router.get("/current")
async def get_current_banners() -> list[Banner]:
    return await SERVICE.get_current_banners()
