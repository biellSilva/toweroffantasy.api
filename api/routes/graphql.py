
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

from api.infra.entitys.graphql import *


SIMU_REPO = SimulacraRepo()
MATRICE_REPO = MatricesRepo()
WEAPON_REPO = WeaponRepo()
SIMU_V2_REPO = SimulacraV2Repo()
ACHIEV_REPO = AchievementRepo()
OUTFIT_REPO = OutfitRepo()
FOOD_REPO = FoodRepo()
ITEM_REPO = ItemRepo()
RELIC_REPO = RelicRepo()
SERVAN_REPO = ServantsRepo()
MOUNTS_REPO = MountsRepo()


def check_params(lang: str, version: str):
    if version not in ['global', 'china']:
        raise VersionNotFound(version)
    
    if lang not in LANGS_ and lang not in LANGS_CN_:
        raise LanguageNotFound(lang, version)


@strawberry.type
class Query:

    @strawberry.field(name='simulacrum')
    async def get_simulacrum(self, id: str, lang: str = 'en', version: str = 'global') -> Simulacra:
        check_params(lang=lang, version=version)

        if version == 'global':
            simulacrum = await SIMU_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return simulacrum # type: ignore
        
        elif version == 'china':
            simulacrum = await SIMU_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return simulacrum  # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='simulacra')
    async def get_simulacra(self, lang: str = 'en', version: str = 'global') -> List[Simulacra]:
        check_params(lang=lang, version=version)
        
        if version == 'global':
            simulacra = await SIMU_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return simulacra # type: ignore
        
        elif version == 'china':
            simulacra = await SIMU_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return simulacra  # type: ignore

        raise VersionNotFound(version)

    @strawberry.field(name='simulacrum_v2')
    async def get_simulacrum_v2(self, id: str, lang: str = 'en') -> SimulacraV2:
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
    async def get_simulacra_v2(self, lang: str = 'en') -> List[SimulacraV2]:
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
    async def get_weapon(self, id: str, lang: str = 'en', version: str = 'global') -> Weapon:
        check_params(lang=lang, version=version)

        if version == 'global':
            weapon = await WEAPON_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return weapon # type: ignore
        
        elif version == 'china':
            weapon = await WEAPON_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return weapon # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='weapons')
    async def get_weapons(self, lang: str = 'en', version: str = 'global') -> List[Weapon]:
        check_params(lang=lang, version=version)

        if version == 'global':
            weapons = await WEAPON_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return weapons # type: ignore
        
        elif version == 'china':
            weapons = await WEAPON_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return weapons # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='matrix')
    async def get_matrice(self, id: str, lang: str = 'en') -> Matrice:
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
    async def get_matrices(self, lang: str = 'en') -> List[Matrice]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            matrix = await MATRICE_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return matrix # type: ignore
        
        elif version == 'china':
            matrix = await MATRICE_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return matrix # type: ignore
        
        raise VersionNotFound(version)
    
    @strawberry.field(name='achievement')
    async def get_achivement(self, id: str, lang: str = 'en') -> Achievement:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            achivement = await ACHIEV_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return achivement # type: ignore
        
        elif version == 'china':
            achivement = await ACHIEV_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return achivement # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='achievements')
    async def get_achivements(self, lang: str = 'en') -> List[Achievement]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            achivements = await ACHIEV_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return achivements # type: ignore
        
        elif version == 'china':
            achivements = await ACHIEV_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return achivements # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='relic')
    async def get_relic(self, id: str, lang: str = 'en') -> Relic:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            relic = await RELIC_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return relic # type: ignore
        
        elif version == 'china':
            relic = await RELIC_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return relic # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='relics')
    async def get_relics(self, lang: str = 'en') -> List[Relic]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            relics = await RELIC_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return relics # type: ignore
        
        elif version == 'china':
            relics = await RELIC_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return relics # type: ignore
        
        raise VersionNotFound(version)
    
    @strawberry.field(name='outfit')
    async def get_outfit(self, id: str, lang: str = 'en') -> Outfit:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            outfit = await OUTFIT_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return outfit # type: ignore
        
        elif version == 'china':
            outfit = await OUTFIT_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return outfit # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='outfits')
    async def get_outfits(self, lang: str = 'en') -> List[Outfit]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            outfits = await OUTFIT_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return outfits # type: ignore
        
        elif version == 'china':
            outfits = await OUTFIT_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return outfits # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='servant')
    async def get_servant(self, id: str, lang: str = 'en') -> SmartServant:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            servant = await SERVAN_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return servant # type: ignore
        
        elif version == 'china':
            servant = await SERVAN_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return servant # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='servants')
    async def get_servants(self, lang: str = 'en') -> List[SmartServant]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            servants = await SERVAN_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return servants # type: ignore
        
        elif version == 'china':
            servants = await SERVAN_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return servants # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='mount')
    async def get_mount(self, id: str, lang: str = 'en') -> Mount:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            mount = await MOUNTS_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return mount # type: ignore
        
        elif version == 'china':
            mount = await MOUNTS_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return mount # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='mounts')
    async def get_mounts(self, lang: str = 'en') -> List[Mount]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            mounts = await MOUNTS_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return mounts # type: ignore
        
        elif version == 'china':
            mounts = await MOUNTS_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return mounts # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='food')
    async def get_food(self, id: str, lang: str = 'en') -> Food:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            food = await FOOD_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return food # type: ignore
        
        elif version == 'china':
            food = await FOOD_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return food # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='foods')
    async def get_foods(self, lang: str = 'en') -> List[Food]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            foods = await FOOD_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return foods # type: ignore
        
        elif version == 'china':
            foods = await FOOD_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return foods # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='item')
    async def get_item(self, id: str, lang: str = 'en') -> Item:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            item = await ITEM_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return item # type: ignore
        
        elif version == 'china':
            item = await ITEM_REPO.get(EntityBase(id=id), lang=LANGS_CN(lang), version=VERSIONS(version))
            return item # type: ignore
        
        raise VersionNotFound(version)

    @strawberry.field(name='items')
    async def get_items(self, lang: str = 'en') -> List[Item]:
        version = 'global'
        check_params(lang=lang, version=version)

        if version == 'global':
            items = await ITEM_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
            return items # type: ignore
        
        elif version == 'china':
            items = await ITEM_REPO.get_all(lang=LANGS_CN(lang), version=VERSIONS(version))
            return items # type: ignore
        
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