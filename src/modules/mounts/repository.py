from src.common.json_repository import JsonRepository
from src.modules.mounts.model import Mount, MountSimple


class MountRepository(JsonRepository[MountSimple, Mount]):
    def __init__(self) -> None:
        super().__init__(filename="mounts", model=Mount, simple_model=MountSimple)
