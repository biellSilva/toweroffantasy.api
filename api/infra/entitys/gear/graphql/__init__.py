import strawberry


@strawberry.type
class StatPool:
    propName: str
    weitghtValue: float


@strawberry.type
class BaseStat:
    isTag: bool
    propName: str
    propValue: float
    modifierOP: str


@strawberry.type
class Gear:
    id: str
    name: str
    type: str
    description: str
    source: str
    icon: str
    rarity: int
    statPool: list[StatPool]
    baseStat: list[BaseStat]
