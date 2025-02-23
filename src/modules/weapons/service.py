from typing import TYPE_CHECKING

from unidecode import unidecode

from src._types import LangsEnum
from src._utils import is_str_in_list, paginate_items
from src.exceptions.not_found import WeaponNotFoundError
from src.modules.weapons.dtos import GetWeapons
from src.modules.weapons.model import Weapon, WeaponSimple

if TYPE_CHECKING:
    from src.modules.weapons.repository import WeaponRepository


class WeaponService:
    def __init__(self, repository: "WeaponRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: LangsEnum, _id: str) -> Weapon:
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return Weapon(**data)
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
    ) -> list[WeaponSimple]:
        weapons = [
            WeaponSimple(**data)
            for data in await self.repository.get_all(lang=params.lang)
        ]

        filtered = [
            data
            for data in weapons
            if self._filter(
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

    def _filter(
        self,
        data: "WeaponSimple",
        /,
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
    ) -> bool:
        if params.is_limited is not None and data.is_limited != params.is_limited:
            return False

        if params.is_fate is not None and data.is_fate != params.is_fate:
            return False

        if params.is_warehouse is not None and data.is_warehouse != params.is_warehouse:
            return False

        if (
            params.name
            and unidecode(params.name).lower() not in unidecode(data.name).lower()
        ):
            return False

        includes = [
            (include_ids, data.id, True),
            (include_elements, data.element.id, True),
            (include_categories, data.category.id, True),
            (include_rarities, data.rarity, True),
            (include_quality, data.quality, True),
        ]
        excludes = [
            (exclude_ids, data.id, True),
            (exclude_elements, data.element.id, True),
            (exclude_categories, data.category.id, True),
            (exclude_rarities, data.rarity, True),
            (exclude_quality, data.quality, True),
        ]

        for inc, param, equals in includes:
            if inc and not is_str_in_list(param, inc, equals=equals):
                return False

        for exc, param, equals in excludes:
            if exc and is_str_in_list(param, exc, equals=equals):
                return False

        return True
