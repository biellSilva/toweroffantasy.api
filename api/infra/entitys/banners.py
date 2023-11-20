
from pydantic import BaseModel, BeforeValidator
from typing import Annotated


class Banner(BaseModel):
    imitation_id: Annotated[str, BeforeValidator(lambda x: x.lower())] | None = None
    weapon_id: Annotated[str, BeforeValidator(lambda x: x.lower())] | None = None
    matrix_id: Annotated[str, BeforeValidator(lambda x: x.lower())] | None = None
    simulacrum: str | None = None
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool

