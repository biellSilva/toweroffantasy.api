
from pydantic import Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.weapons.extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Advancements, 
    Skills,
    Assets,
    Meta,
    BaseStats
)


class Weapon(EntityBase):
    name: str
    description: str
    rarity: str
    type: str = Field(alias='wc', serialization_alias='type')
    element: str
    baseStats: list[BaseStats]
    assets: Assets
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    advanceID: str | None = None
    mats: dict[str, int | None]
    weaponEffects: list[WeaponEffect]
    skills: Skills
    advancements: list[Advancements] = Field(alias='stars', serialization_alias='advancements') 
    meta: Meta | None