
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Simulacra_v2, EntityBase
from api.infra.repository.weapon import WeaponRepo
from api.infra.repository.matrice import MatriceRepo
from api.infra.repository.simulacra import SimulacraRepo



class SimulacraV2Repo(ModelRepository[EntityBase, Simulacra_v2]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Simulacra_v2, 
                         class_base=SimulacraV2Repo,
                         repo_name='imitations')
        self.simu_repo = SimulacraRepo()
        self.weapon_repo = WeaponRepo()
        self.matrice_repo = MatriceRepo()
    
    async def get_all(self, lang: str) -> list[Simulacra_v2]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            # PATH_IMIT = Path(f'api/database/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = {simulacra.id: simulacra.model_dump() for simulacra in await self.simu_repo.get_all(lang=lang)}
        
            if lang in self.cache:
                pass
            else:
                self.cache.update({lang: {}})

            for imit_id, imit_dict in DATA.items():
                if weapon_id := imit_dict.get('weaponID', None):
                    if weapon := await self.weapon_repo.get(EntityBase(id=weapon_id), lang=lang):
                        imit_dict['weapon'] = weapon
                
                if matrice := await self.matrice_repo.get_by_name(name=imit_dict['name'], lang=lang):
                    imit_dict['matrice'] = matrice

                self.cache[lang].update({imit_id.lower(): Simulacra_v2(**imit_dict)})

            return list(self.cache[lang].values())