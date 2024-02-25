import strawberry


@strawberry.type
class Award:
    matId: str
    name: str
    description: str
    icon: str
    rarity: int | None
    type: str | None
    amount: int


@strawberry.type
class Achievement:
    id: str
    name: str
    description: str
    icon: str
    tags: list[str]
    awards: list[Award]
