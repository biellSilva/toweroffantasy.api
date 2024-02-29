from typing import Any, TypedDict

from src.infra.models.meta import RawMeta
from src.infra.models.weapons.extra import (
    RawAdvancement,
    RawStatBase,
    RawStatConverted,
    RawWeaponAssets,
)


class RawWeapon(TypedDict):
    id: str
    element: str
    wc: str
    assets: RawWeaponAssets
    weaponUpgradeId: str
    version: str
    shatter: dict[str, Any]
    charge: dict[str, Any]
    advancements: list[RawAdvancement]
    stats: list[RawStatBase]
    stats_att: list[RawStatConverted]
    upgradeProps: list[list[float]]
    meta: RawMeta
    upgradeMats: dict[str, Any]
    skills: dict[str, Any]
    banners: list[Any]
