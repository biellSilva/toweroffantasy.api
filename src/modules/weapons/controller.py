from typing import Annotated

from fastapi import APIRouter, Depends

from src.modules.base.dtos import BaseDataDto
from src.modules.weapons.dtos import GetWeapon
from src.modules.weapons.model import Weapon, WeaponSimple
from src.modules.weapons.repository import WeaponRepository
from src.modules.weapons.service import WeaponService

router = APIRouter(prefix="/weapons", tags=["weapons"])


SERVICE = WeaponService(WeaponRepository())


@router.get(
    "",
    response_model=list[WeaponSimple],
)
async def get_all_weapons(
    params: Annotated[BaseDataDto, Depends()],
) -> list[Weapon]:
    return await SERVICE.get_all(lang=params.lang)


@router.get(
    "/{weapon_id}",
)
async def get_weapon(params: Annotated[GetWeapon, Depends()]) -> Weapon:
    return await SERVICE.get(lang=params.lang, _id=params.weapon_id)
