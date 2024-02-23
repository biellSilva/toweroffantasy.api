from typing import TypedDict


class RawAdvancement(TypedDict):
    description: str
    charge: float | int
    shatter: float | int


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
