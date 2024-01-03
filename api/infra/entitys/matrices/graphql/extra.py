
import strawberry


@strawberry.type
class MatriceSet:
    need: int | None
    description:str | None


@strawberry.type
class MatrixAssets:
    icon: str
    iconLarge: str
    characterArtwork: str | None = None

    
@strawberry.type
class MatrixMeta:
    recommendedWeapons: list[str] 