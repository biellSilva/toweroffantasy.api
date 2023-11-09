
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase
from api.infra.entitys.weapons.extra import *

from api.utils import place_weapon_icon


class Weapon(EntityBase):
    name: str
    description: str
    icon: Annotated[str, BeforeValidator(place_weapon_icon)]
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
