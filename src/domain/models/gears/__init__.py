import strawberry

from src.domain.models.base import ModelBase

from .extra import BaseStat, Prop, StatPool


class Gear(ModelBase):
    name: str
    type: str
    maxLevel: int
    description: str
    icon: str
    rarity: int
    statPool: list[StatPool] = []
    baseStat: list[BaseStat] = []
    props: list[Prop] = []


@strawberry.experimental.pydantic.type(model=Gear, all_fields=True)
class GearType:
    pass
