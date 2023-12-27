
import strawberry


@strawberry.type
class Item:
    id: str
    name: str | None
    type: str
    description: str | None
    icon: str | None
    rarity: int