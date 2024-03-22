from pydantic import AliasChoices, Field
import strawberry

from src.domain.models.base import ModelBase

from .extra import BaseStat, Prop, StatPool, GearAdvancement, UpgradeProp


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


@strawberry.experimental.pydantic.type(model=Gear, all_fields=True)
class GearType:
    pass
