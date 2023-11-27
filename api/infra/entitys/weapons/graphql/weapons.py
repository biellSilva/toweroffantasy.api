
import strawberry

from api.infra.entitys.graphql.banner import Banner
from api.infra.entitys.weapons.graphql.extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    WeaponAdvancement, 
    WeaponAttacks,
    WeaponAssets,
    MetaData,
    FashionWeaponInfo,
    MatrixSuit,
    BaseStats,
    UpgradeMaterial,
)


@strawberry.type
class Weapon:
    id: str
    SimulacrumID: str | None
    IsUpPoolWeapon: bool

    Name: str
    Rarity: str
    Assets: WeaponAssets

    Brief: str
    WeaponCategory: str
    WeaponElement: str
    Description: str

    Shatter: ShatterOrCharge
    Charge: ShatterOrCharge

    FashionWeaponInfos: list[FashionWeaponInfo]
    RecommendedMatrices: list[MatrixSuit]

    WeaponEffects: list[WeaponEffect]

    WeaponAdvancements: list[WeaponAdvancement]
    WeaponAttacks: WeaponAttacks

    Meta: MetaData | None
    Banners: list[Banner]
