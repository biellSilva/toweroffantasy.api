
import strawberry

from strawberry.fastapi import GraphQLRouter
from typing import List, Any

from api.enums import (
    langs as LANGS_,
    langs_cn as LANGS_CN_,
    VERSIONS, 
    LANGS, 
    LANGS_CN
)

from api.core.exceptions import VersionNotFound, LanguageNotFound

from api.infra.repository import *
from api.infra.entitys import EntityBase

from api.infra.entitys.simulacra.graphql.simulacra import SimulacraType
from api.infra.entitys.weapons.graphql.weapons import WeaponType
from api.infra.entitys.matrices.graphql.matrice import MatriceType
from api.infra.entitys.simulacra_v2.graphql.simulacra_v2 import SimulacraTypeV2


SIMU_REPO = SimulacraRepo()
MATRICE_REPO = MatricesRepo()
WEAPON_REPO = WeaponRepo()
SIMU_V2_REPO = SimulacraV2Repo()
ACHIEV_REPO = AchievementRepo()
OUTFIT_REPO = OutfitRepo()
FOOD_REPO = FoodRepo()
ITEM_REPO = ItemRepo()
RELIC_REPO = RelicRepo()


def check_params(lang: str, version: str):
    if version not in ['global', 'china']:
        raise VersionNotFound(version)
    
    if lang not in LANGS_ and lang not in LANGS_CN_:
        raise LanguageNotFound(lang, version)


@strawberry.type
class Query:

    @strawberry.field(name='simulacrum')
    async def get_simulacrum(self, id: str, lang: str = 'en', version: str = 'global') -> SimulacraType:
        check_params(lang=lang, version=version)

        if version == 'global':
            simulacrum = await SIMU_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return simulacrum # type: ignore
        
        elif version == 'china':
            simulacrum = await SIMU_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return simulacrum  # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='simulacra')
    async def get_simulacra(self, lang: str = 'en', version: str = 'global') -> List[SimulacraType]:
        check_params(lang=lang, version=version)
        
        if version == 'global':
            simulacra = await SIMU_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return simulacra # type: ignore
        
        elif version == 'china':
            simulacra = await SIMU_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return simulacra  # type: ignore

        raise VersionNotFound(version)



    @strawberry.field(name='simulacrum_v2')
    async def get_simulacrum_v2(self, id: str, lang: str = 'en') -> SimulacraTypeV2:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            simulacrum = await SIMU_V2_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return simulacrum # type: ignore
        
        elif version == 'china':
            simulacrum = await SIMU_V2_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return simulacrum  # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='simulacra_v2')
    async def get_simulacra_v2(self, lang: str = 'en') -> List[SimulacraTypeV2]:
        version = 'global'
        check_params(lang=lang, version=version)
        
        if version == 'global':
            simulacra = await SIMU_V2_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return simulacra # type: ignore
        
        elif version == 'china':
            simulacra = await SIMU_V2_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return simulacra  # type: ignore

        raise VersionNotFound(version)
    


    @strawberry.field(name='weapon')
    async def get_weapon(self, id: str, lang: str = 'en', version: str = 'global') -> WeaponType:
        check_params(lang=lang, version=version)

        if version == 'global':
            weapon = await WEAPON_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return weapon # type: ignore
        
        elif version == 'china':
            weapon = await WEAPON_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return weapon # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='weapons')
    async def get_weapons(self, lang: str = 'en', version: str = 'global') -> List[WeaponType]:
        check_params(lang=lang, version=version)

        if version == 'global':
            weapons = await WEAPON_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return weapons # type: ignore
        
        elif version == 'china':
            weapons = await WEAPON_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return weapons # type: ignore
        
        raise VersionNotFound(version)



    @strawberry.field(name='matrix')
    async def get_matrice(self, id: str, lang: str = 'en') -> MatriceType:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            matrix = await MATRICE_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return matrix # type: ignore
        
        elif version == 'china':
            matrix = await MATRICE_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return matrix # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='matrices')
    async def get_matrices(self, lang: str = 'en') -> List[MatriceType]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            matrix = await MATRICE_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return matrix # type: ignore
        
        elif version == 'china':
            matrix = await MATRICE_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return matrix # type: ignore
        
        raise VersionNotFound(version)



    




graphql = GraphQLRouter[Any, Any](schema=strawberry.Schema(query=Query), path='/') 
METADATA = {
    'name': 'GraphQL',
    'description': 'GraphQL provides a complete and understandable description of the data \n\n **SOME FIELDS CONTAINS CN DATA**',
    'externalDocs': {
        'description': 'GraphQL docs',
        'url': 'https://api.toweroffantasy.info/',
    }
}