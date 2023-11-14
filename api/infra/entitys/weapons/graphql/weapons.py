
import strawberry

from api.infra.entitys.weapons.graphql.extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Advancements, 
    Skills,
    WeaponAssets,
)


@strawberry.type
class WeaponType:
    id: str
    name: str
    description: str
    rarity: str
    type: str
    element: str
    assets: WeaponAssets
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    advanceID: str | None
    weaponEffects: list[WeaponEffect]
    skills: Skills
    advancements: list[Advancements]
