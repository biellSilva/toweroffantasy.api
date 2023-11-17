
from api.infra.entitys.base import EntityBase

from .extra import MountAsset


class Mount(EntityBase):
    name: str | None = None
    description: str
    assets: MountAsset