
from api.infra.entitys.base import EntityBase


class Outfit(EntityBase):
    name: str | None = None
    type: str
    description: str | None = None
    source: str | None = None
    icon: str | None


