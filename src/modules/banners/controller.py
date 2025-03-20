from typing import Annotated

from fastapi import Body, Query

from src.core.router import ApiRouter
from src.modules.banners.dtos import CreateBanner, GetBanners
from src.modules.banners.repository import BannerRepository
from src.modules.banners.service import BannerService

from prisma.models import Banner  # isort:skip


router = ApiRouter(prefix="/banners", tags=["banners"])

SERVICE = BannerService(BannerRepository())


@router.get("", response_model=list[Banner])
async def get_versions(params: Annotated[GetBanners, Query()]) -> list[Banner]:
    return await SERVICE.get_banners(params)


@router.post("", response_model=Banner)
async def create_version(params: Annotated[CreateBanner, Body()]) -> Banner:
    return await SERVICE.create_banner(data=params)
