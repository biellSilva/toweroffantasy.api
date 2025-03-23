from typing import TYPE_CHECKING

from prisma.types import (
    BannerCreateInput,
    BannerOrderedViewWhereInput,
    BannerWhereInput,
)

from src.context.prisma_conn import PrismaContext

if TYPE_CHECKING:
    from prisma.models import Banner, BannerOrderedView

    from src.modules.banners.dtos import CreateBanner, GetBanners


class BannerRepository:
    """Banner repository."""

    def __init__(self) -> None:
        self._client = PrismaContext.get_client()

    def _filter(self, params: "GetBanners") -> BannerOrderedViewWhereInput:  # noqa: C901, PLR0912
        _filter = BannerOrderedViewWhereInput()

        _filter["AND"] = []

        if params.include_ids:
            _filter["AND"].append(
                {
                    "OR": [
                        {"imitation_id": {"in": params.include_ids}},
                        {"weapon_id": {"in": params.include_ids}},
                        {"suit_id": {"in": params.include_ids}},
                    ],
                },
            )

        if params.exclude_ids:
            _filter["AND"].append(
                {
                    "OR": [
                        {"imitation_id": {"not_in": params.exclude_ids}},
                        {"weapon_id": {"not_in": params.exclude_ids}},
                        {"suit_id": {"not_in": params.exclude_ids}},
                    ],
                },
            )

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
            if not params.start_at_after:
                _filter["start_at"] = {"lte": params.start_at_before}
            else:
                _filter["start_at"] = {
                    "lte": params.start_at_before,
                    "gte": params.start_at_after,
                }

        if params.end_at_before:
            if not params.end_at_after:
                _filter["end_at"] = {"lte": params.end_at_before}
            else:
                _filter["end_at"] = {
                    "lte": params.end_at_before,
                    "gte": params.end_at_after,
                }

        return _filter

    async def get_id(self, banner_id: str) -> "Banner | None":
        """Get a banner by ID."""

        return await self._client.banner.find_first(
            where=BannerWhereInput(
                OR=[
                    {"imitation_id": banner_id},
                    {"suit_id": banner_id},
                    {"weapon_id": banner_id},
                ],
            ),
        )

    async def count(self, params: "GetBanners") -> int:
        """Count all banners."""

        return await self._client.bannerorderedview.count(where=self._filter(params))

    async def get_banners(self, params: "GetBanners") -> list["BannerOrderedView"]:
        """Get all banners."""

        return await self._client.bannerorderedview.find_many(
            where=self._filter(params),
            order=[{"start_at": "desc"}, {"is_rerun": "desc"}],
            skip=(params.page - 1) * params.limit,
            take=params.limit,
        )

    async def create(self, data: "CreateBanner") -> "Banner":
        """Create a banner."""

        return await self._client.banner.create(
            data=BannerCreateInput(**data.model_dump()),
        )
