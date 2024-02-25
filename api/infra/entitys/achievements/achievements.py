from api.infra.entitys.base import EntityBase

from .extra import Award


class Achievement(EntityBase):
    name: str
    amount: int
    description: str
    icon: str | None
    tags: list[str]
    rewards: list[Award]
