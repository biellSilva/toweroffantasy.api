
from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Item, EntityBase


class ItemRepo(ModelRepository[EntityBase, Item]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Item, 
                         class_base=ItemRepo,
                         repo_name='items')
    
    