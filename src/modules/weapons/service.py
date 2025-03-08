from typing import TYPE_CHECKING

from src._types import LangsEnum
from src.exceptions.not_found import WeaponNotFoundError
from src.modules._paginator import paginate_items
from src.modules.weapons._utils import filter_weapons
from src.modules.weapons.dtos import GetWeapons

if TYPE_CHECKING:
    from src.modules._paginator import Pagination
    from src.modules.weapons.model import Weapon, WeaponSimple
    from src.modules.weapons.repository import WeaponRepository


class WeaponService:
    def __init__(self, repository: "WeaponRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: LangsEnum, _id: str) -> "Weapon":
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return data
        raise WeaponNotFoundError(lang=lang, id=_id)

    async def get_all(
        self,
        *,
        params: GetWeapons,
        include_ids: list[str] | None,
        exclude_ids: list[str] | None,
        include_elements: list[str] | None,
        exclude_elements: list[str] | None,
        include_categories: list[str] | None,
        exclude_categories: list[str] | None,
        include_rarities: list[str] | None,
        exclude_rarities: list[str] | None,
        include_quality: list[str] | None,
        exclude_quality: list[str] | None,
    ) -> "Pagination[WeaponSimple]":
        weapons = await self.repository.get_all(lang=params.lang)

        filtered = [
            data
            for data in weapons
            if filter_weapons(
                data,
                params=params,
                include_ids=include_ids,
                exclude_ids=exclude_ids,
                include_elements=include_elements,
                exclude_elements=exclude_elements,
                include_categories=include_categories,
                exclude_categories=exclude_categories,
                include_rarities=include_rarities,
                exclude_rarities=exclude_rarities,
                include_quality=include_quality,
                exclude_quality=exclude_quality,
            )
        ]

        return paginate_items(filtered, params.page, params.limit)
