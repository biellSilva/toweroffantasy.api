from typing import TYPE_CHECKING

from src.context.prisma_conn import PrismaContext

from prisma.types import BannerCreateInput, BannerWhereInput  # isort:skip


if TYPE_CHECKING:
    from src.modules.banners.dtos import CreateBanner, GetBanners

    from prisma.models import Banner  # isort:skip


class BannerRepository:
    """Banner repository."""

    def __init__(self) -> None:
        self._client = PrismaContext.get_client()

    async def get_id(self, banner_id: str) -> "Banner | None":
        """Get a banner by ID."""

        return await self._client.banner.find_first(where={"object_id": banner_id})

    async def get_banners(self, params: "GetBanners") -> list["Banner"]:  # noqa: C901
        """Get all banners."""

        _filter = BannerWhereInput()

        if params.include_ids:
            _filter["object_id"] = {"in": params.include_ids}

        if params.exclude_ids:
            _filter["object_id"] = {"not_in": params.exclude_ids}

        if params.final_rerun:
            _filter["final_rerun"] = params.final_rerun

        if params.is_collab:
            _filter["is_collab"] = params.is_collab

        if params.is_rerun:
            _filter["is_rerun"] = params.is_rerun

        if params.limited_only:
            _filter["limited_only"] = params.limited_only

        if params.start_at_after:
            _filter["start_at"] = {"gte": params.start_at_after}

        if params.end_at_after:
            _filter["end_at"] = {"gte": params.end_at_after}

        if params.start_at_before:
            _filter["start_at"] = {"lte": params.start_at_before}

        if params.end_at_before:
            _filter["end_at"] = {"lte": params.end_at_before}

        return await self._client.banner.find_many(
            where=_filter,
            order={"start_at": "desc"},
        )

    async def create(self, data: "CreateBanner") -> "Banner":
        """Create a banner."""

        return await self._client.banner.create(
            data=BannerCreateInput(**data.model_dump()),
        )
