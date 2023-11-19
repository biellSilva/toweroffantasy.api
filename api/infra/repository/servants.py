

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import SmartServant, EntityBase


class ServantsRepo(ModelRepository[EntityBase, SmartServant]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=SmartServant, 
                         class_base=ServantsRepo,
                         repo_name='pet')
    
    