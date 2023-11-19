
import strawberry

@strawberry.type
class Outfit:
    id: str
    name: str | None
    type: str
    description: str | None
    source: str | None
    icon: str
