import strawberry


@strawberry.type
class Relic:
    id: str
    name: str
    rarity: int
    description: str | None
    source: str | None
    type: str
    icon: str
    version: str
    advancements: list[str]
