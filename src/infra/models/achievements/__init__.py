from typing import Any, TypedDict


class RawAchievement(TypedDict):
    id: str
    tags: list[str]
    achievementRewards: list[dict[str, Any]]
    extraRewards: list[dict[str, Any]]
    rewards: list[dict[str, Any]]
