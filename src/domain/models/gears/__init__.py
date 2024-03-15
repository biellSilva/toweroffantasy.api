import strawberry

from src.domain.models.base import ModelBase

from .extra import BaseStat, StatPool


class Gear(ModelBase):
    name: str
    type: str
    description: str
    icon: str
    rarity: int
    statPool: list[StatPool] = []
    baseStat: list[BaseStat]


@strawberry.experimental.pydantic.type(model=Gear, all_fields=True)
class GearType:
    pass
