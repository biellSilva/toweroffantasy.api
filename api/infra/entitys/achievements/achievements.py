
from api.infra.entitys.base import EntityBase

from .extra import Award


class Achievement(EntityBase):
    name: str
    description: str
    icon: str | None
    tags: list[str] = []
    awards: list[Award]