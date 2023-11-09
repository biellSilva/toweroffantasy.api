
from pydantic import Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.weapons.extra import *


class Weapon(EntityBase):
    name: str
    description: str
    icon: str
    rarity: str
    type: str = Field(alias='wc', serialization_alias='type')
    element: str
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    advanceID: str | None = None
    mats: dict[str, int | None]
    weaponEffects: list[WeaponEffect]
    skills: Skills
    advancements: list[Advancements] = Field(alias='stars', serialization_alias='advancements') 
