from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.modules._paginator import Pagination
from src.modules.weapons.dtos import GetWeapon, GetWeapons
from src.modules.weapons.model import Weapon, WeaponSimple
from src.modules.weapons.repository import WeaponRepository
from src.modules.weapons.service import WeaponService

router = APIRouter(prefix="/weapons", tags=["weapons"])


SERVICE = WeaponService(WeaponRepository())


@router.get("")
async def get_all_weapons(
    params: Annotated[GetWeapons, Query()],
) -> Pagination[WeaponSimple]:
    return await SERVICE.get_all(params=params)


@router.get("/{weapon_id}")
async def get_weapon(params: Annotated[GetWeapon, Depends()]) -> Weapon:
    return await SERVICE.get(params=params)
