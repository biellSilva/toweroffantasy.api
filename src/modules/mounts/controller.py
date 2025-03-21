from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.modules._paginator import Pagination
from src.modules.mounts.dtos import GetMount, GetMounts
from src.modules.mounts.model import Mount, MountSimple
from src.modules.mounts.repository import MountRepository
from src.modules.mounts.service import MountService

router = APIRouter(prefix="/mounts", tags=["mounts"])

SERVICE = MountService(MountRepository())


@router.get("")
async def get_mounts(
    params: Annotated[GetMounts, Query()],
) -> Pagination[MountSimple]:
    return await SERVICE.get_all(params=params)


@router.get("/{mount_id}")
async def get_mount(params: Annotated[GetMount, Depends()]) -> Mount:
    return await SERVICE.get(lang=params.lang, _id=params.mount_id)
