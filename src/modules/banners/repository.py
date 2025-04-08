from typing import TYPE_CHECKING, Any

from src.common.mongo_repository import MongoRepository
from src.modules.banners.dtos import Banner, CreateBanner

if TYPE_CHECKING:
    from src.modules.banners.dtos import GetBanners


class BannerRepository(MongoRepository[Banner, Banner]):
    """Banner repository."""

    def __init__(self) -> None:
        super().__init__(
            collection_name="banners",
            simple_model=Banner,
            complex_model=Banner,
        )
        self.view = self._db.get_collection("BannersView")

    async def get_banners(self, params: "GetBanners") -> list[Banner]:
        """Get banners based on the given parameters."""

        return [
            Banner(**document)
            async for document in self.view.find(
                self._filter(params),
                skip=(params.page - 1) * params.limit,
                limit=params.limit,
            )
        ]

    async def count_banners(self, params: "GetBanners") -> int:
        """Count banners based on the given parameters."""

        return await self.view.count_documents(self._filter(params))

    async def create_banner(self, data: "CreateBanner") -> Banner | None:
        """Create a new banner."""
        await self._collection.insert_one(data.model_dump(mode="json"))
        if resp := await self.view.find_one({"imitation_id": data.imitation_id}):
            return Banner(**resp)
        return None

    def _filter(self, params: "GetBanners") -> dict[str, Any]:  # noqa: C901, PLR0912
        """Filter banners based on the given parameters."""
        query: dict[str, Any] = {}

        if params.limited_only is not None:
            query["limited_only"] = params.limited_only
        if params.is_rerun is not None:
            query["is_rerun"] = params.is_rerun
        if params.is_collab is not None:
            query["is_collab"] = params.is_collab
        if params.final_rerun is not None:
            query["final_rerun"] = params.final_rerun

        if params.start_at_after is not None:
            query["start_at"] = {"$gte": str(params.start_at_after)}
        if params.start_at_before is not None:
            if "start_at" in query:
                query["start_at"]["$lte"] = str(params.start_at_before)
            else:
                query["start_at"] = {"$lte": str(params.start_at_before)}

        if params.end_at_after is not None:
            query["end_at"] = {"$gte": str(params.end_at_after)}
        if params.end_at_before is not None:
            if "end_at" in query:
                query["end_at"]["$lte"] = str(params.end_at_before)
            else:
                query["end_at"] = {"$lte": str(params.end_at_before)}

        if params.include_ids is not None:
            query["object_id"] = {"$in": params.include_ids}

        if params.exclude_ids is not None:
            if "object_id" in query:
                query["object_id"]["$nin"] = params.exclude_ids
            else:
                query["object_id"] = {"$nin": params.exclude_ids}

        return query
