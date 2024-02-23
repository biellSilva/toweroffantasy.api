from pydantic import AliasChoices, Field

from src.domain.models.banner import Banner
from src.domain.models.base import ModelBase
from src.domain.models.meta import MetaData
from src.domain.models.weapons.extras import (
    BaseStats,
    ShatterOrCharge,
    WeaponAdvancement,
    WeaponAssets,
    WeaponAttacks,
    WeaponEffect,
    WeaponMats,
)


class Weapon(ModelBase):
    simulacrumId: str | None = Field(
        validation_alias=AliasChoices("avatar", "simulacrumId"), default=None
    )
    advanceId: str | None = Field(
        validation_alias=AliasChoices("advanceID", "advanceId"), default=None
    )

    name: str
    version: str
    rarity: int
    assets: WeaponAssets
    limited: bool

    category: str = Field(validation_alias=AliasChoices("wc", "category"))
    element: str
    description: str

    shatter: ShatterOrCharge
    charge: ShatterOrCharge

    upgradeMats: WeaponMats | None

    elementEffect: WeaponEffect | None = Field(
        None, validation_alias=AliasChoices("elementEffects", "elementEffect")
    )
    weaponEffects: list[WeaponEffect] = []

    weaponAdvancements: list[WeaponAdvancement] = Field(
        validation_alias=AliasChoices("advancements", "weaponAdvancements")
    )
    weaponAttacks: WeaponAttacks = Field(
        validation_alias=AliasChoices("skills", "weaponAttacks")
    )
    weaponStats: list[BaseStats] = Field(
        validation_alias=AliasChoices("stats", "baseStats", "weaponStats")
    )

    meta: MetaData
    banners: list[Banner] = []
