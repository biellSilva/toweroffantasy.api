
from api.infra.entitys.base import EntityBase


class Item(EntityBase):
    id: str
    name: str | None = None
    type: str
    description: str | None = None
    icon: str | None = None
    rarity: int
    