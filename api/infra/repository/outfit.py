
from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Outfit, EntityBase


class OutfitRepo(ModelRepository[EntityBase, Outfit]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Outfit, 
                         class_base=OutfitRepo,
                         repo_name='outfits')
    
    