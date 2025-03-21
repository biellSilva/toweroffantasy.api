from json import loads
from typing import Any

import aiofiles

from src.modules._utils import rarity_to_int
from src.modules.banners.dtos import GetBanners
from src.modules.banners.repository import BannerRepository
from src.modules.base.json_repository import JsonRepository
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple


class ImitationRepository(JsonRepository[Simulacrum, SimulacrumSimple]):
    def __init__(self) -> None:
        super().__init__(
            name="simulacra",
            model=Simulacrum,
            simple_model=SimulacrumSimple,
        )
        self.banner_repo = BannerRepository()

    def _sort_data(
        self,
        data: Simulacrum,
    ) -> tuple[int, int, int, int, int, str]:
        def _bool_to_int(*, value: bool) -> int:
            return -1 if value else 0

        if not data.banners:
            return (
                0,
                0,
                -rarity_to_int(data.rarity),
                _bool_to_int(value=data.is_limited),
                _bool_to_int(value=data.no_weapon),
                data.name,
            )

        return (
            -int(data.banners[-1].start_at.timestamp()),
            -int(data.banners[-1].end_at.timestamp()),
            -rarity_to_int(data.rarity),
            _bool_to_int(value=data.is_limited),
            _bool_to_int(value=data.no_weapon),
            data.name,
        )

    async def _custom_loader(self, *, lang: str) -> None:
        """Load all items from the database."""

        async with aiofiles.open(f"src/database/{lang}/{self._name}.json") as file:
            data: dict[str, dict[str, Any]] = loads(await file.read())

        for item in data.values():
            item["banners"] = [
                item.model_dump(mode="json")
                for item in await self.banner_repo.get_banners(
                    GetBanners(include_ids=[item["id"]]),
                )
            ]

        await self._cache.set_values(lang=lang, value_dict=data)

    async def get_all(self, *, lang: str) -> list[SimulacrumSimple]:
        """Get all items."""

        cache = await self._cache.get_all(lang=lang)

        if not cache:
            await self._custom_loader(lang=lang)

        data = [
            self._model(**data)
            for data in (await self._cache.get_all(lang=lang)).values()
        ]
        data.sort(key=self._sort_data)

        return [self._list_model(**item.model_dump()) for item in data]
