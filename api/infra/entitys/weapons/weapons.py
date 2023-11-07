
from pydantic import Field

from api.infra.entitys.base import EntityBase
from api.infra.entitys.weapons.extra import WeaponEffect, Advancements, Skills


class Weapon(EntityBase):
    name: str
    description: str
    icon: str
    rarity: str
    type: str = Field(alias='wc')
    element: str
    advanceID: str | None = None
    mats: dict[str, int | None]
    weaponEffects: list[WeaponEffect]
    skills: Skills
    advancements: list[Advancements] = Field(alias='stars')
