from pydantic import Field

from src.common.dtos import BaseSearchAllDto, BaseSearchDto


class GetMount(BaseSearchDto):
    mount_id: str


class GetMounts(BaseSearchAllDto):
    name: str | None = Field(None, description="Name should be part of")
    include_ids: list[str] | None = Field(None, description="Id should be one of")
    exclude_ids: list[str] | None = Field(None, description="Id should not be one of")
    include_quality: list[str] | None = Field(
        None,
        description="Quality should include one of",
    )
    exclude_quality: list[str] | None = Field(
        None,
        description="Quality should exclude one of",
    )
    include_mount_type: list[str] | None = Field(
        None,
        description="Mount type should include one of",
    )
    exclude_mount_type: list[str] | None = Field(
        None,
        description="Mount type should exclude one of",
    )
