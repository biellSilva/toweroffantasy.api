
import strawberry

from api.infra.entitys.graphql.banner import Banner
from api.infra.entitys.weapons.graphql.extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Advancements, 
    Skills,
    WeaponAssets,
    Meta,
    BaseStats,
    UpgradeMaterial,
)


@strawberry.type
class Weapon:
    id: str
    name: str
    description: str
    rarity: str
    type: str 
    element: str
    baseStats: list[BaseStats] 
    assets: WeaponAssets
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    advanceID: str | None 
    upgradeMaterials: list[UpgradeMaterial]
    weaponEffects: list[WeaponEffect]
    skills: Skills
    advancements: list[Advancements]
    meta: Meta | None
    banners: list[Banner]