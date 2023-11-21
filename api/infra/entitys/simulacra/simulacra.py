

from api.infra.entitys.base import EntityBase

from .extra import VoiceActors, Awakening, Assets
from ..banners import Banner


class Simulacra(EntityBase):
    Name: str
    Rarity: str
    CharacterSex: str
    AvatarId: str
    AdvanceImitations: str | None = None
    UnlockInfo: str
    WeaponId: str | None = None
    MatrixId: str | None = None
    Like: list[str]
    Dislike: list[str]
    Gender: str | None = None
    Birthday: str | None = None
    Age: str | None = None
    Title: str | None = None
    Job: str | None = None
    Height: str | None = None
    BelongTo: str | None = None
    Hometown: str | None = None
    AssetsA0: Assets
    AssetsA3: Assets | None = None
    CVMap: VoiceActors
    Awakenings: list[Awakening]
    Banners: list[Banner]

