
import strawberry


@strawberry.type
class MatriceSet:
    need: int | None
    description:str | None
