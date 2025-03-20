from src.modules.base.json_repository import JsonRepository
from src.modules.mounts.model import Mount, MountSimple


class MountRepository(JsonRepository[Mount, MountSimple]):
    def __init__(self) -> None:
        super().__init__(name="mounts", model=Mount, simple_model=MountSimple)
