
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
    attributeID: str
    advancements: list[str]

