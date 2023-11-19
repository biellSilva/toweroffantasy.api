
from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Mount, EntityBase


class MountsRepo(ModelRepository[EntityBase, Mount]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Mount, 
                         class_base=MountsRepo,
                         repo_name='mount')
    
    