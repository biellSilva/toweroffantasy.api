
import strawberry


@strawberry.type
class ListKeys:
    Time: float
    Value: float

@strawberry.type
class WeaponAssets:
    ItemIcon: str | None
    ItemLargeIcon: str | None
    WeaponUPIcon: str | None
    WeaponIconForMatrix: str | None
    LotteryCardImage: str | None
    SoloLeagueBanPickBanner: str | None

@strawberry.type
class Skill:
    Name: str | None
    Description: str | None
    Values: list[list[ListKeys]]
    ShortDesc: str | None
    Icon: str | None
    Tags: list[str]
    Operations: list[str]

@strawberry.type
class WeaponSkills:
    Name: str | None
    Description: str | None
    Icon: str | None
    Attacks: list[Skill]

@strawberry.type
class WeaponAttacks:
    Melee: WeaponSkills
    Evade: WeaponSkills
    Skill: WeaponSkills
    Discharge: WeaponSkills

@strawberry.type
class WeaponAdvancement:
    Description: str | None
    GoldNeeded: int 
    Shatter: float
    Charge: float
    NeedItem: str | None
    WeaponFashionID: str | None

@strawberry.type
class FashionWeaponInfo:
    FashionName: str
    FashionImitationId: str

@strawberry.type
class MatrixSuit:
    MatrixSuitName: str
    MatrixSuitDes: str

@strawberry.type
class WeaponEffect:
    title: str
    description: str

@strawberry.type
class ShatterOrCharge:
    value: float
    tier: str

@strawberry.type
class RecoMatrix:
    id: str
    pieces: int

@strawberry.type
class MetaData:
    recommendedPairings: list[str]
    recommendedMatrices: list[RecoMatrix]
    rating: list[int]
    analyticVideoId: str | None

@strawberry.type
class BaseStats:
    id: str
    name: str
    icon: str

@strawberry.type
class UpgradeMaterial:
    id: str
    need: int