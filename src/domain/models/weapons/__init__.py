import strawberry
from pydantic import AliasChoices, Field

from src.domain.models.banner import Banner
from src.domain.models.base import ModelBase
from src.domain.models.fashion import Fashion
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

    weaponAdvancements: list[WeaponAdvancement]
    weaponAttacks: WeaponAttacks = Field(
        validation_alias=AliasChoices("skills", "weaponAttacks")
    )
    weaponStats: list[BaseStats] = Field(
        validation_alias=AliasChoices("stats_att", "baseStats", "weaponStats")
    )

    meta: MetaData = MetaData()
    banners: list[Banner] = []
    fashion: list[Fashion] = []


@strawberry.experimental.pydantic.type(model=Weapon, all_fields=True)
class WeaponType:
    pass
