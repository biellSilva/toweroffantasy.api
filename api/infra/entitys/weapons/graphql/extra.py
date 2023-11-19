
import strawberry


@strawberry.type
class Skill:
    id: str
    icon: str
    name: str
    description: str


@strawberry.type
class Skills:
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]


@strawberry.type
class Stats:
    shatter: float
    charge: float


@strawberry.type
class Advancements:
    description: str | None
    stats: Stats
    need: str


@strawberry.type
class WeaponEffect:
    title: str
    description: str


@strawberry.type
class ShatterOrCharge:
    value: float
    tier: str


@strawberry.type
class WeaponAssets:
    icon: str | None 
    weaponMatrixIcon: str | None


@strawberry.type
class RecoMatrix:
    id: str
    pieces: int


@strawberry.type
class Meta:
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

