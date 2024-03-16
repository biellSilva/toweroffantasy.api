from typing import TypedDict

from src.infra.models.gears.extras import RawBaseStat, RawPropValue, RawStatPool


class RawGear(TypedDict):
    id: str
    name: str
    type: str
    description: str
    icon: str
    rarity: int
    baseStat: list[RawBaseStat]
    statPool: list[RawStatPool]
    props: list[dict[str, RawPropValue]]
