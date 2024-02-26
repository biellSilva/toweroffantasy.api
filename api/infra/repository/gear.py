from api.infra.entitys import EntityBase
from api.infra.entitys.gear import Gear
from api.infra.repository.base_repo import ModelRepository


class GearRepo(ModelRepository[EntityBase, Gear]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(
            model_base=EntityBase,
            model=Gear,
            class_base=GearRepo,
            repo_name="gear",
        )
