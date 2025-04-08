from typing import TYPE_CHECKING

from src.exceptions.not_found import WeaponNotFoundError
from src.modules._paginator import Pagination

if TYPE_CHECKING:
    from src.modules.weapons.dtos import GetWeapon, GetWeapons
    from src.modules.weapons.model import Weapon, WeaponSimple
    from src.modules.weapons.repository import WeaponRepository


class WeaponService:
    def __init__(self, repository: "WeaponRepository") -> None:
        self.repository = repository

    async def get(self, *, params: "GetWeapon") -> "Weapon":
        if data := await self.repository.get_weapon(params):
            return data
        raise WeaponNotFoundError(lang=params.lang, id=params.weapon_id)

    async def get_all(
        self,
        *,
        params: "GetWeapons",
    ) -> "Pagination[WeaponSimple]":
        weapons = await self.repository.get_weapons(params)
        count = await self.repository.count()
        return Pagination(
            data=weapons,
            page=params.page,
            limit=params.limit,
            max_page=count // params.limit + 1,
            total_items=count,
        )
