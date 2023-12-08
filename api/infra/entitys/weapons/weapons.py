
from pydantic import BeforeValidator, Field
from typing import Annotated

from api.infra.entitys.base import EntityBase
from api.infra.entitys.banners import Banner

from api.utils import classify_rework

from .extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Assets,
    MetaData,
    BaseStats,
    FashionWeaponInfo,
    MatrixSuit,
    WeaponAdvancement,
    WeaponAttacks
)


class Weapon(EntityBase):
    simulacrumId: str | None = Field(alias='avatar', default=None)
    advanceId: str | None = Field(alias='advanceID', default=None)
    # isUpPoolWeapon: bool = False

    name: str
    rarity: str
    assets: Assets

    # Brief: str
    category: str = Field(alias='wc')
    element: str
    description: str

    shatter: Annotated[ShatterOrCharge, BeforeValidator(classify_rework)]
    charge: Annotated[ShatterOrCharge, BeforeValidator(classify_rework)]

    # FashionWeaponInfos: list[FashionWeaponInfo]
    # RecommendedMatrices: list[MatrixSuit]

    weaponEffects: list[WeaponEffect]

    weaponAdvancements: list[WeaponAdvancement] = Field(alias='advancements')
    weaponAttacks: WeaponAttacks = Field(alias='skills')
    weaponStats: list[BaseStats] = Field(alias='stats')

    meta: MetaData | None = None
    banners: list[Banner] = []
