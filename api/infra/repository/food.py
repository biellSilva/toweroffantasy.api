
from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Food, EntityBase
from api.infra.repository.item import ItemRepo


class FoodRepo(ModelRepository[EntityBase, Food]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Food, 
                         class_base=FoodRepo,
                         repo_name='food')
        self.item_repo = ItemRepo()
