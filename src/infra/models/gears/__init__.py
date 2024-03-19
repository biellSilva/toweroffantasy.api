from typing import Any, TypedDict

from src.infra.models.gears.extras import RawBaseStat, RawStatPool


class RawGear(TypedDict):
    id: str
    name: str
    type: str
    description: str
    icon: str
    rarity: int
    baseStat: list[RawBaseStat]
    statPool: list[RawStatPool]
    props: list[Any]
    advancement: list[Any]
    baseUpgradeProps: list[Any]
