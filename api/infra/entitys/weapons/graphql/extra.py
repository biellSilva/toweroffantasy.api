
import strawberry


@strawberry.type
class ListKeys:
    Time: float
    Value: float

@strawberry.type
class WeaponAssets:
    icon: str | None
    # itemLargeIcon: str | None
    # WeaponUPIcon: str | None
    weaponIconForMatrix: str | None

@strawberry.type
class Skill:
    name: str | None
    description: str | None
    values: list[list[float]]
    icon: str | None
    tags: list[str] 
    operations: list[str] 

# @strawberry.type
# class WeaponSkills:
#     Name: str | None
#     Description: str | None
#     Icon: str | None
#     Attacks: list[Skill]

@strawberry.type
class WeaponAttacks:
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]

@strawberry.type
class ShatterOrCharge:
    value: float
    tier: str

@strawberry.type
class WeaponAdvancement:
    description: str | None
    # GoldNeeded: int 
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    need: str | None
    # WeaponFashionID: str | None

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
    value: float
    isTag: bool
    modifier: str

@strawberry.type
class UpgradeMaterial:
    id: str
    need: int

@strawberry.type
class WeaponMat:
    id: str | None 
    amount: int | None 
    name: str | None
    icon: str | None
    type: str | None
    description: str | None
    rarity: str | None

@strawberry.type
class WeaponMats:
    id: str
    items: list[list[WeaponMat]]