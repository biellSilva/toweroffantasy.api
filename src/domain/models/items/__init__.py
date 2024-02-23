from src.domain.models.base import ModelBase


class Item(ModelBase):
    name: str | None = None
    type: str
    description: str | None = None
    icon: str | None = None
    rarity: int
