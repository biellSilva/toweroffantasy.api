
import strawberry


@strawberry.type
class Award:
    type: str
    amount: int

@strawberry.type
class Achievement:
    id: str
    name: str
    description: str
    icon: str
    tags: list[str]
    awards: list[Award]