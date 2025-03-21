from typing import Annotated

from fastapi import APIRouter, Body, Query, Security
from prisma.models import Banner

from src.core.docs import generate_docs
from src.exceptions.unauthorized import InvalidRoleError
from src.modules.auth.dtos import Payload
from src.modules.banners.dtos import CreateBanner, GetBanners
from src.modules.banners.repository import BannerRepository
from src.modules.banners.service import BannerService
from src.security.role import RoleSecurity

router = APIRouter(prefix="/banners", tags=["banners"])

SERVICE = BannerService(BannerRepository())


@router.get("")
async def get_versions(params: Annotated[GetBanners, Query()]) -> list[Banner]:
    return await SERVICE.get_banners(params)


@router.post("", responses=generate_docs(InvalidRoleError, auth=True))
async def create_version(
    _: Annotated[Payload, Security(RoleSecurity(role="admin"))],
    params: Annotated[CreateBanner, Body()],
) -> Banner:
    return await SERVICE.create_banner(data=params)
