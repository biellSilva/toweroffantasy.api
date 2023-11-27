
import strawberry

from api.infra.entitys.graphql.banner import Banner
from .extra import Assets, VoiceActors, Awakening


@strawberry.type()
class Simulacra:
    id: str
    Name: str
    Rarity: str
    CharacterSex: str
    AvatarId: str
    AdvanceImitations: str | None
    UnlockInfo: str
    WeaponId: str | None
    MatrixId: str | None
    Like: list[str]
    Dislike: list[str]
    Gender: str | None
    Birthday: str | None
    Age: str | None
    Title: str | None
    Job: str | None
    Height: str | None
    BelongTo: str | None
    Hometown: str | None
    AssetsA0: Assets
    AssetsA3: Assets | None
    CVMap: VoiceActors
    Awakenings: list[Awakening]
    Banners: list[Banner]
