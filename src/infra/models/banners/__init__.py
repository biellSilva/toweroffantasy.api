from datetime import datetime
from typing import TypedDict


class RawBanner(TypedDict):
    bannerNumber: int
    simulacrum: str
    start: str
    end: str
    startDate: datetime
    endDate: datetime
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool
    no_weapon: bool
    imitation_id: str
    weapon_id: str
    matrix_id: str
    element: str | None
    category: str | None
