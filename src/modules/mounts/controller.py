from typing import Annotated

from fastapi import Depends, Query

from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import MountNotFoundError
from src.modules._paginator import Pagination
from src.modules.mounts.dtos import GetMount, GetMounts
from src.modules.mounts.model import Mount, MountSimple
from src.modules.mounts.repository import MountRepository
from src.modules.mounts.service import MountService

router = ApiRouter(prefix="/mounts", tags=["mounts"])

SERVICE = MountService(MountRepository())


@router.get("", response_model=Pagination[MountSimple])
async def get_mounts(
    params: Annotated[GetMounts, Query()],
) -> Pagination[MountSimple]:
    return await SERVICE.get_all(params=params)


@router.get(
    "/{mount_id}",
    response_model=Mount,
    exceptions=[MountNotFoundError(lang=LangsEnum.EN, id="Mount1")],
)
async def get_mount(params: Annotated[GetMount, Depends()]) -> Mount:
    return await SERVICE.get(lang=params.lang, _id=params.mount_id)
