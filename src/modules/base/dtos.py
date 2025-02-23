from datetime import datetime
from typing import Annotated

from fastapi import Query
from pydantic import BaseModel

from src._types import LangsEnum


class BaseDto(BaseModel):
    id: int
    created_at: datetime


class BaseSearchDto(BaseModel):
    lang: Annotated[LangsEnum, Query(LangsEnum.EN, description="Language code")]


class BaseSearchAllDto(BaseSearchDto):
    page: Annotated[int, Query(1, description="Page number", ge=1)] = 1
    limit: Annotated[int, Query(10, description="Items per page", ge=1)] = 10
