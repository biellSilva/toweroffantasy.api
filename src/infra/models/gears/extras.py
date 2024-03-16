from typing import TypedDict


class RawBaseStat(TypedDict):
    IsTag: bool
    PropName: str
    PropValue: float
    ModifierOp: str


class RawStatPool(TypedDict):
    PropName: str
    WeightValue: float


class RawPropValue(TypedDict):
    Quality: str
    PropInitValue: float
    PropMinValue: float
    PropMaxValue: float
