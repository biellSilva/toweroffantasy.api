from api.infra.entitys.base import EntityBase
from api.infra.entitys.gear.extra import BaseStat, StatPool


class Gear(EntityBase):
    name: str
    type: str
    description: str
    source: str
    icon: str
    rarity: int
    statPool: list[StatPool] = []
    baseStat: list[BaseStat]
