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
        if data := await self.repository.get_id(lang=lang, id_=_id):
            return data
        raise WeaponNotFoundError(lang=lang, id=_id)

    async def get_all(
        self,
        *,
        params: GetWeapons,
    ) -> "Pagination[WeaponSimple]":
        weapons = await self.repository.get_all(lang=params.lang)

        filtered = [data for data in weapons if filter_weapons(data, params=params)]

        return paginate_items(filtered, params.page, params.limit)
