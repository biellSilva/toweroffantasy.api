
import strawberry


@strawberry.type
class MatriceSet:
    need: int | None
    description:str | None


@strawberry.type
class MatrixAssets:
    icon: str
    iconLarge: str


@strawberry.type
class Banner:
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool