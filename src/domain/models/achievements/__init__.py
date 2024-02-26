from src.domain.models.achievements.extra import Reward
from src.domain.models.base import ModelBase


class Achievement(ModelBase):
    name: str
    amount: int
    description: str
    icon: str
    tags: list[str]
    rewards: list[Reward]
