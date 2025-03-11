from datetime import datetime
from typing import Annotated

from fastapi import Query
from pydantic import BaseModel, Field

from src._types import LangsEnum


class BaseDto(BaseModel):
    id: int
    created_at: datetime


class BaseSearchDto(BaseModel):
    lang: Annotated[LangsEnum, Query(LangsEnum.EN, description="Language code")]


class BaseSearchAllDto(BaseModel):
    lang: LangsEnum = Field(LangsEnum.EN, description="Language code")
    page: int = Field(1, description="Page number", ge=1)
    limit: int = Field(10, description="Items per page", ge=1)
