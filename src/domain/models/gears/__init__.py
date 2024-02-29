from src.domain.models.base import ModelBase
from .extra import StatPool, BaseStat


class Gear(ModelBase):
    name: str
    type: str
    description: str
    source: str
    icon: str
    rarity: int
    statPool: list[StatPool] = []
    baseStat: list[BaseStat]
