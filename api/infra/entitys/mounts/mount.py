
from api.infra.entitys.base import EntityBase

from .extra import MountAsset, UnlockItem


class Mount(EntityBase):
    name: str | None = None
    description: str
    assets: MountAsset
    version: str
    rarity: int
    unlockItems: list[UnlockItem]