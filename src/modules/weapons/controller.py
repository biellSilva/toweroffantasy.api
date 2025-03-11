from typing import Annotated

from fastapi import Depends, Query

from src.core.router import ApiRouter
from src.modules._paginator import Pagination
from src.modules.weapons.dtos import GetWeapon, GetWeapons
from src.modules.weapons.model import Weapon, WeaponSimple
from src.modules.weapons.repository import WeaponRepository
from src.modules.weapons.service import WeaponService

router = ApiRouter(prefix="/weapons", tags=["weapons"])


SERVICE = WeaponService(WeaponRepository())


@router.get(
    "",
    response_model=Pagination[WeaponSimple],
)
async def get_all_weapons(
    params: Annotated[GetWeapons, Query()],
) -> Pagination[WeaponSimple]:
    return await SERVICE.get_all(params=params)


@router.get(
    "/{weapon_id}",
)
async def get_weapon(params: Annotated[GetWeapon, Depends()]) -> Weapon:
    return await SERVICE.get(lang=params.lang, _id=params.weapon_id)
