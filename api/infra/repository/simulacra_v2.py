
from typing import Any
from api.enums import LANGS, LANGS_CN, VERSIONS

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Simulacra_v2, EntityBase
from api.infra.repository.weapon import WeaponRepo
from api.infra.repository.matrice import MatricesRepo
from api.infra.repository.simulacra import SimulacraRepo



class SimulacraV2Repo(ModelRepository[EntityBase, Simulacra_v2]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Simulacra_v2, 
                         class_base=SimulacraV2Repo,
                         repo_name='imitations')
        self.simu_repo = SimulacraRepo()
        self.weapon_repo = WeaponRepo()
        self.matrice_repo = MatricesRepo()

    async def get_all(self, lang: LANGS | LANGS_CN | str, version: VERSIONS) -> list[Simulacra_v2]:
        if version in self.cache:
            if lang in self.cache[version]:
                return list(self.cache[version][lang].values())
    
        DATA: dict[str, dict[str, Any]] = {simulacra.id: simulacra.model_dump() for simulacra in await self.simu_repo.get_all(lang=lang, version=version)}

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        for imit_id, imit_dict in DATA.items():
            if weapon_id := imit_dict.get('WeaponId', None):
                if weapon := await self.weapon_repo.get(EntityBase(id=weapon_id), lang=lang, version=version):
                    imit_dict['Weapon'] = weapon
            
            if matrice_id := imit_dict.get('MatrixId', None):
                if matrice := await self.matrice_repo.get(EntityBase(id=matrice_id), lang=lang, version=version):
                    imit_dict['Matrix'] = matrice

            self.cache[version][lang].update({imit_id.lower(): Simulacra_v2(**imit_dict)})

        return list(self.cache[version][lang].values())