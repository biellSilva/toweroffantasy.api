
import strawberry

from api.infra.entitys.graphql.banner import Banner
from api.infra.entitys.weapons.graphql.extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    WeaponAdvancement, 
    WeaponAttacks,
    WeaponAssets,
    MetaData,
    BaseStats,
    WeaponMats,
)


@strawberry.type
class Weapon:
    id: str
    simulacrumId: str | None
    advanceId: str | None
    # isUpPoolWeapon: bool = False

    name: str
    version: str
    rarity: str
    assets: WeaponAssets

    # Brief: str
    category: str
    element: str
    description: str
    
    shatter: ShatterOrCharge
    charge: ShatterOrCharge

    # FashionWeaponInfos: list[FashionWeaponInfo]
    # RecommendedMatrices: list[MatrixSuit]

    upgradeMats: WeaponMats | None

    elementEffect: WeaponEffect | None
    weaponEffects: list[WeaponEffect]

    weaponAdvancements: list[WeaponAdvancement] 
    weaponAttacks: WeaponAttacks 
    weaponStats: list[BaseStats]

    meta: MetaData
    banners: list[Banner]

