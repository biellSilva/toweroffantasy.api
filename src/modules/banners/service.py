from datetime import datetime
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from src.exceptions.internal_error import FailedToCreateBannerError
from src.modules._paginator import Pagination
from src.modules.banners.dtos import Banner, GetBanners

if TYPE_CHECKING:
    from src.modules.banners.dtos import CreateBanner
    from src.modules.banners.repository import BannerRepository


class BannerService:
    def __init__(self, banner_repository: "BannerRepository") -> None:
        self.banner_repository = banner_repository

    async def get_banners(self, params: "GetBanners") -> Pagination["Banner"]:
        count = await self.banner_repository.count_banners(params)
        banners = await self.banner_repository.get_banners(params)

        return Pagination[Banner](
            data=banners,
            total_items=count,
            page=params.page,
            limit=params.limit,
            max_page=count // params.limit + 1,
        )

    async def get_current_banners(self) -> list["Banner"]:
        return await self.banner_repository.get_banners(
            GetBanners(
                page=1,
                limit=100,
                end_at_after=datetime.now(tz=ZoneInfo("UTC")),
            ),
        )

    async def create_banner(self, *, data: "CreateBanner") -> "Banner":
        if resp := await self.banner_repository.create_banner(data):
            return resp
        raise FailedToCreateBannerError
