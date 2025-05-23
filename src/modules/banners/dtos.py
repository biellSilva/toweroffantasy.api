from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from src._types import ObjectIdType


class CreateBanner(BaseModel):
    imitation_id: str
    weapon_id: str
    suit_id: str | None = None

    start_at: datetime
    end_at: datetime
    link: str | None = None

    limited_only: bool = False
    is_rerun: bool = False
    is_collab: bool = False
    final_rerun: bool = False


class GetBanner(BaseModel):
    object_id: str


class GetBanners(BaseModel):
    page: int = Field(1, description="Page number", ge=1)
    limit: int = Field(10, description="Items per page", ge=1)
    include_ids: Annotated[
        list[str] | None,
        Field(description="Object ID should be one of"),
    ] = None
    exclude_ids: Annotated[
        list[str] | None,
        Field(description="Object ID should not be one of"),
    ] = None

    limited_only: Annotated[
        bool | None,
        Field(description="Filter banners that are limited only"),
    ] = None
    is_rerun: Annotated[
        bool | None,
        Field(description="Filter banners that are reruns"),
    ] = None
    is_collab: Annotated[
        bool | None,
        Field(description="Filter banners that are collaborations"),
    ] = None
    final_rerun: Annotated[
        bool | None,
        Field(description="Filter banners that are final reruns"),
    ] = None

    start_at_after: Annotated[
        datetime | None,
        Field(description="Filter banners that start after this date"),
    ] = None
    start_at_before: Annotated[
        datetime | None,
        Field(description="Filter banners that start before this date"),
    ] = None

    end_at_after: Annotated[
        datetime | None,
        Field(description="Filter banners that end after this date"),
    ] = None
    end_at_before: Annotated[
        datetime | None,
        Field(description="Filter banners that end before this date"),
    ] = None


class Banner(BaseModel):
    id: ObjectIdType
    imitation_id: str
    weapon_id: str
    suit_id: str | None
    start_at: datetime
    end_at: datetime
    link: str | None
    is_collab: bool
    is_rerun: bool
    final_rerun: bool
    limited_only: bool
    position: int
