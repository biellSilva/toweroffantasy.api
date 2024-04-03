import strawberry
from pydantic import AliasChoices, Field

from src.domain.models.base import ModelBase

from .extra import BaseStat, GearAdvancement, Prop, StatPool, UpgradeProp


class Gear(ModelBase):
    name: str
    type: str
    slotType: str
    maxLevel: int
    description: str
    icon: str
    rarity: int
    element: str | None
    expValue: int
    statPool: list[StatPool] = []
    baseStat: list[BaseStat] = []
    props: list[Prop] = []
    advancement: list[list[GearAdvancement]] = []
    baseUpgradeProps: list[list[UpgradeProp]] = []
    advancementExp: list[int] = Field(validation_alias=AliasChoices("advancementEXP"))
    matList: list[str]
    gearUpgradeProps: list[list[float]]
    source: list[str] = []


@strawberry.experimental.pydantic.type(model=Gear, all_fields=True)
class GearType:
    pass
