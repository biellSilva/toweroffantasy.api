from typing import Annotated

from fastapi import APIRouter, Body, Query

from src.core.docs import generate_docs
from src.exceptions.unauthorized import InvalidRoleError
from src.modules._paginator import Pagination
from src.modules.banners.dtos import Banner, CreateBanner, GetBanners
from src.modules.banners.repository import BannerRepository
from src.modules.banners.service import BannerService

router = APIRouter(prefix="/banners", tags=["banners"])

SERVICE = BannerService(BannerRepository())


@router.get("")
async def get_banners(
    params: Annotated[GetBanners, Query()],
) -> Pagination[Banner]:
    return await SERVICE.get_banners(params)


@router.post(
    "",
    responses=generate_docs(InvalidRoleError, auth=True),
    # dependencies=[Security(RoleSecurity(role="admin"))],
)
async def create_banner(params: Annotated[CreateBanner, Body()]) -> Banner:
    return await SERVICE.create_banner(data=params)
