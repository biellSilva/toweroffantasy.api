from typing import TypedDict


class RawWeaponUpgrade(TypedDict):
    mat_id: str
    mat_amount: None
    maxLevel: int
    id: str
    name: str | None
    type: str
    description: str | None
    icon: str | None
    rarity: int
