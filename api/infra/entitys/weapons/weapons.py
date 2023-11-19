
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.utils import classify_rework, material_rework

from api.infra.entitys.base import EntityBase
from api.infra.entitys.banners import Banner
from .extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Advancements, 
    Skills,
    Assets,
    Meta,
    BaseStats,
    UpgradeMaterial
)


class Weapon(EntityBase):
    name: str
    description: str
    rarity: str
    type: str = Field(alias='wc', serialization_alias='type')
    element: str
    baseStats: list[BaseStats] = Field(alias='stats', serialization_alias='baseStats', default=[])
    assets: Assets
    shatter: Annotated[ShatterOrCharge, BeforeValidator(classify_rework)]
    charge: Annotated[ShatterOrCharge, BeforeValidator(classify_rework)]
    advanceID: str | None = None
    upgradeMaterials: Annotated[list[UpgradeMaterial], BeforeValidator(material_rework)] = Field(alias='mats')
    weaponEffects: list[WeaponEffect]
    skills: Skills
    advancements: list[Advancements] = Field(alias='stars', serialization_alias='advancements') 
    banners: list[Banner]
    meta: Meta | None = None