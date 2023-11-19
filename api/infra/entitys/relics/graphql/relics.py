
import strawberry


@strawberry.type
class RelicType:
    id: str
    name: str
    rarity: str
    description: str | None
    source: str | None
    type: str
    icon: str
    attributeID: str
    advancements: list[str]

