
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
