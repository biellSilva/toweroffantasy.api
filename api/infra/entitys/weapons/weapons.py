
from pydantic import BeforeValidator, Field, AliasChoices
from typing import Annotated

from api.infra.entitys.base import EntityBase
from api.infra.entitys.banners import Banner
from api.infra.entitys.weapon_mats import WeaponMats

from api.utils import classify_rework

from .extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Assets,
    MetaData,
    BaseStats,
    # FashionWeaponInfo,
    # MatrixSuit,
    WeaponAdvancement,
    WeaponAttacks
)


class Weapon(EntityBase):
    simulacrumId: str | None = Field(validation_alias=AliasChoices('avatar', 'simulacrumId'), default=None)
    advanceId: str | None = Field(validation_alias=AliasChoices('advanceID', 'advanceId'), default=None)
    # isUpPoolWeapon: bool = False

    name: str
    version: str
    rarity: str
    assets: Assets

    # Brief: str
    category: str = Field(validation_alias=AliasChoices('wc', 'category'))
    element: str
    description: str

    shatter: Annotated[ShatterOrCharge, BeforeValidator(lambda x: x if isinstance(x, dict) else classify_rework(x))] # type: ignore
    charge: Annotated[ShatterOrCharge, BeforeValidator(lambda x: x if isinstance(x, dict) else classify_rework(x))] # type: ignore

    # FashionWeaponInfos: list[FashionWeaponInfo]
    # RecommendedMatrices: list[MatrixSuit]

    upgradeMats: WeaponMats | None

    elementEffect: WeaponEffect | None = Field(None, validation_alias=AliasChoices('elementEffects', 'elementEffect'))
    weaponEffects: list[WeaponEffect] = []

    weaponAdvancements: list[WeaponAdvancement] = Field(validation_alias=AliasChoices('advancements', 'weaponAdvancements'))
    weaponAttacks: WeaponAttacks = Field(validation_alias=AliasChoices('skills', 'weaponAttacks'))
    weaponStats: list[BaseStats] = Field(validation_alias=AliasChoices('stats', 'baseStats', 'weaponStats'))

    meta: MetaData
    banners: list[Banner] = []
