from typing import Any, TypedDict


class RawAdvancement(TypedDict):
    description: str | None
    multiplier: list[Any]
    need: str | None


class RawStat(TypedDict):
    id: str
    name: str
    icon: str
    multiplier: float | int
    flat: bool


class RawStatBase(TypedDict):
    stat: RawStat
    value: float


class RawStatConverted(TypedDict):
    id: str
    name: str
    icon: str
    value: float
    upgradeProp: float


class RawWeaponAssets(TypedDict):
    icon: str
