from api.infra.entitys import EntityBase
from api.infra.entitys.guidebooks import GuideBook
from api.infra.repository.base_repo import ModelRepository


class GuideBookRepo(ModelRepository[EntityBase, GuideBook]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(
            model_base=EntityBase,
            model=GuideBook,
            class_base=GuideBookRepo,
            repo_name="guidebook",
        )
        
