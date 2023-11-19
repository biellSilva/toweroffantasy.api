
from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Relic, EntityBase


class RelicRepo(ModelRepository[EntityBase, Relic]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Relic, 
                         class_base=RelicRepo,
                         repo_name='relics')