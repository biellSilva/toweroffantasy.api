from src.domain.models.base import ModelBase

from .extras import MountAsset, UnlockItem


class Mount(ModelBase):
    name: str
    description: str
    assets: MountAsset
    version: str
    rarity: int
    unlockItems: list[UnlockItem]
