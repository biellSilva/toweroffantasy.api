from typing import TypedDict


class _RawAward(TypedDict):
    name: str
    icon: str


class _RawUnlockable(TypedDict):
    text: str
    stage: int
    award: _RawAward
    trait: str


class RawUnlockables(TypedDict):
    unlockables: list[_RawUnlockable]
