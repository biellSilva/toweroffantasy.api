from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseSearchAllDto, BaseSearchDto


class GetWeapon(BaseSearchDto):
    weapon_id: Annotated[str, Path(description="Weapon id")]


class GetWeapons(BaseSearchAllDto):
    name: str | None = None
    is_fate: bool | None = None
    is_limited: bool | None = None
    is_warehouse: bool | None = None
    shatter_value: int | None = None
    charge_value: int | None = None
    shatter_tier: str | None = None
    charge_tier: str | None = None
