from typing import TYPE_CHECKING

from src.exceptions.not_found import MountNotFoundError
from src.modules._paginator import paginate_items
from src.modules.mounts._utils import filter_mounts

if TYPE_CHECKING:
    from src._types import LangsEnum
    from src.modules._paginator import Pagination
    from src.modules.mounts.dtos import GetMounts
    from src.modules.mounts.model import Mount, MountSimple
    from src.modules.mounts.repository import MountRepository


class MountService:
    def __init__(self, mount_repository: "MountRepository") -> None:
        self.mount_repository = mount_repository

    async def get(self, *, lang: "LangsEnum", _id: str) -> "Mount":
        if data := await self.mount_repository.get_id(lang=lang, _id=_id):
            return data
        raise MountNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, params: "GetMounts") -> "Pagination[MountSimple]":
        mounts = await self.mount_repository.get_all(lang=params.lang)

        filtered = [data for data in mounts if filter_mounts(data, params=params)]

        return paginate_items(filtered, params.page, params.limit)
