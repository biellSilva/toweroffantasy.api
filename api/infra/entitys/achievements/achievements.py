

from api.infra.entitys.base import EntityBase
from .extra import Award


class Achievement(EntityBase):
    name: str
    description: str
    icon: str
    tags: list[str] = []
    awards: list[Award]