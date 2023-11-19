
from pydantic import BaseModel, Field, BeforeValidator
from typing import Annotated


class Banner(BaseModel):
    imitation_id: Annotated[str, BeforeValidator(lambda x: x.lower())] | None = Field(exclude=True, default=None)
    weapon_id: Annotated[str, BeforeValidator(lambda x: x.lower())] | None = Field(exclude=True, default=None)
    matrix_id: Annotated[str, BeforeValidator(lambda x: x.lower())] | None = Field(exclude=True, default=None)
    simulacrum: str = Field(exclude=True)
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool