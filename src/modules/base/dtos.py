from datetime import datetime
from typing import Annotated

from fastapi import Query
from pydantic import BaseModel

from src._types import LangsEnum


class BaseDto(BaseModel):
    id: int
    created_at: datetime


class BaseDataDto(BaseModel):
    lang: Annotated[LangsEnum, Query(LangsEnum.EN, description="Language code")]
