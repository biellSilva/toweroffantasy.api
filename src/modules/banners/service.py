from typing import TYPE_CHECKING

from src.exceptions.not_found import BannerNotFoundError

if TYPE_CHECKING:
    from src.modules.banners.dtos import CreateBanner, GetBanners
    from src.modules.banners.repository import BannerRepository

    from prisma.models import Banner  # isort:skip


class BannerService:
    def __init__(self, banner_repository: "BannerRepository") -> None:
        self.banner_repository = banner_repository

    async def get_banners(self, params: "GetBanners") -> list["Banner"]:
        return await self.banner_repository.get_banners(params)

    async def get_banner_by_id(self, banner_id: str) -> "Banner":
        if data := await self.banner_repository.get_id(banner_id):
            return data
        raise BannerNotFoundError(id=banner_id)

    async def create_banner(self, *, data: "CreateBanner") -> "Banner":
        return await self.banner_repository.create(data)
