import strawberry


@strawberry.type
class ListKeys:
    Time: float
    Value: float


@strawberry.type
class WeaponAssets:
    icon: str | None
    weaponIconForMatrix: str | None
    characterArtwork: str | None


@strawberry.type
class Skill:
    name: str | None
    description: str | None
    values: list[list[float]]
    icon: str | None
    tags: list[str]
    operations: list[str]


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
class AdvancMultipliers:
    statId: str
    coefficient: float


@strawberry.type
class WeaponAdvancement:
    description: str | None
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    need: str | None
    multiplier: list[AdvancMultipliers]


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
class BaseStats:
    id: str
    name: str
    icon: str
    value: float
    upgradeProp: float


@strawberry.type
class UpgradeMaterial:
    id: str
    need: int


@strawberry.type
class UpgradeMaterial:
    matId: str | None
    amount: int | None
    name: str | None
    icon: str | None
    type: str | None
    description: str | None
    rarity: int | None


@strawberry.type
class LevelUpgrade:
    requiredExp: int
    mats: list[UpgradeMaterial]


@strawberry.type
class WeaponMats:
    id: str
    items: list[LevelUpgrade]
