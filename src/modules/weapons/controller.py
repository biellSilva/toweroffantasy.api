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
    params: Annotated[GetWeapons, Depends()],
    include_ids: Annotated[
        list[str] | None,
        Query(description="ID should be one of"),
    ] = None,
    exclude_ids: Annotated[
        list[str] | None,
        Query(description="ID should not be one of"),
    ] = None,
    include_elements: Annotated[
        list[str] | None,
        Query(description="Element ID should include one of"),
    ] = None,
    exclude_elements: Annotated[
        list[str] | None,
        Query(description="Element ID should exclude one of"),
    ] = None,
    include_categories: Annotated[
        list[str] | None,
        Query(description="Category ID should include one of"),
    ] = None,
    exclude_categories: Annotated[
        list[str] | None,
        Query(description="Category ID should exclude one of"),
    ] = None,
    include_rarities: Annotated[
        list[str] | None,
        Query(description="Rarity should include one of"),
    ] = None,
    exclude_rarities: Annotated[
        list[str] | None,
        Query(description="Rarity should exclude one of"),
    ] = None,
    include_quality: Annotated[
        list[str] | None,
        Query(description="Quality should include one of"),
    ] = None,
    exclude_quality: Annotated[
        list[str] | None,
        Query(description="Quality should exclude one of"),
    ] = None,
) -> Pagination[WeaponSimple]:
    return await SERVICE.get_all(
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


@router.get(
    "/{weapon_id}",
)
async def get_weapon(params: Annotated[GetWeapon, Depends()]) -> Weapon:
    return await SERVICE.get(lang=params.lang, _id=params.weapon_id)
