
from pydantic import BeforeValidator
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
<<<<<<< Updated upstream
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
=======
    SimulacrumID: str | None
    IsUpPoolWeapon: bool

    Name: str
    Rarity: str
    Assets: Assets

    Brief: str
    WeaponCategory: str
    WeaponElement: str
    Description: str

    Shatter: Annotated[ShatterOrCharge, BeforeValidator(classify_rework)]
    Charge: Annotated[ShatterOrCharge, BeforeValidator(classify_rework)]

    FashionWeaponInfos: list[FashionWeaponInfo]
    RecommendedMatrices: list[MatrixSuit]

    WeaponEffects: list[WeaponEffect]

    WeaponAdvancements: list[WeaponAdvancement]
    WeaponAttacks: WeaponAttacks

    Meta: MetaData | None = None
    Banners: list[Banner] = []
>>>>>>> Stashed changes
