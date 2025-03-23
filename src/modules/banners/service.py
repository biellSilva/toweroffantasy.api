from typing import TYPE_CHECKING

from prisma.models import Banner
from prisma.models import BannerOrderedView as BannerOrdered

from src.exceptions.not_found import BannerNotFoundError
from src.modules._paginator import Pagination

if TYPE_CHECKING:
    from src.modules.banners.dtos import CreateBanner, GetBanners
    from src.modules.banners.repository import BannerRepository


class BannerService:
    def __init__(self, banner_repository: "BannerRepository") -> None:
        self.banner_repository = banner_repository

    async def get_banners(self, params: "GetBanners") -> Pagination["BannerOrdered"]:
        count = await self.banner_repository.count(params)
        banners = await self.banner_repository.get_banners(params)

        return Pagination[BannerOrdered](
            data=banners,
            total_items=count,
            page=params.page,
            limit=params.limit,
            max_page=count // params.limit + 1,
        )

    async def get_banner_by_id(self, banner_id: str) -> "Banner":
        if data := await self.banner_repository.get_id(banner_id):
            return data
        raise BannerNotFoundError(id=banner_id)

    async def create_banner(self, *, data: "CreateBanner") -> "Banner":
        return await self.banner_repository.create(data)
