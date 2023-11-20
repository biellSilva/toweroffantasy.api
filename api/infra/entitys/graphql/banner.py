
import strawberry


@strawberry.type
class Banner:
    imitation_id: str | None
    weapon_id: str | None
    matrix_id: str | None
    simulacrum: str | None
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool