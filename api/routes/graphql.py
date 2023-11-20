
import strawberry

from strawberry.fastapi import GraphQLRouter
from typing import List, Any

from api.enums import (
    langs as LANGS_,
    langs_cn as LANGS_CN_,
    VERSIONS, 
    LANGS, 
)

from api.core.exceptions import VersionNotFound, LanguageNotFound, MissingArgument

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
        print('*'*50)
        raise LanguageNotFound(lang, version)
    


@strawberry.type
class Query:

    @strawberry.field(name='simulacrum')
    async def get_simulacrum(self, id: str | None = None, name: str | None = None, lang: str = 'en', version: str = 'global') -> Simulacra:
        check_params(lang=lang, version=version)

        if id:
            simulacrum = await SIMU_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return simulacrum # type: ignore

        elif name:
            simulacrum = await SIMU_REPO.get_by_name(name=name, lang=LANGS(lang), version=VERSIONS(version))
            return simulacrum # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='simulacra')
    async def get_simulacra(self, lang: str = 'en', version: str = 'global') -> List[Simulacra]:
        check_params(lang=lang, version=version)
        
        simulacra = await SIMU_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return simulacra # type: ignore
        

    @strawberry.field(name='simulacrum_v2')
    async def get_simulacrum_v2(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> SimulacraV2:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            simulacrum = await SIMU_V2_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return simulacrum # type: ignore
        
        elif name:
            simulacrum = await SIMU_V2_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return simulacrum  # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='simulacra_v2')
    async def get_simulacra_v2(self, lang: str = 'en') -> List[SimulacraV2]:
        version = 'global'
        check_params(lang=lang, version=version)
        
        simulacra = await SIMU_V2_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return simulacra # type: ignore
        
    
    @strawberry.field(name='weapon')
    async def get_weapon(self, id: str | None = None, name: str | None = None, lang: str = 'en', version: str = 'global') -> Weapon:
        check_params(lang=lang, version=version)

        if id:
            weapon = await WEAPON_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return weapon # type: ignore
        
        elif name:
            weapon = await WEAPON_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return weapon # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='weapons')
    async def get_weapons(self, lang: str = 'en', version: str = 'global') -> List[Weapon]:
        check_params(lang=lang, version=version)

        weapons = await WEAPON_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return weapons # type: ignore

    @strawberry.field(name='matrix')
    async def get_matrice(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> Matrice:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            matrix = await MATRICE_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return matrix # type: ignore
        
        elif name:
            matrix = await MATRICE_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return matrix # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='matrices')
    async def get_matrices(self, lang: str = 'en') -> List[Matrice]:
        version = 'global'
        check_params(lang=lang, version=version)

        matrix = await MATRICE_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return matrix # type: ignore
    
    @strawberry.field(name='achievement')
    async def get_achivement(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> Achievement:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            achivement = await ACHIEV_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return achivement # type: ignore
        
        elif name:
            achivement = await ACHIEV_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return achivement # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='achievements')
    async def get_achivements(self, lang: str = 'en') -> List[Achievement]:
        version = 'global'
        check_params(lang=lang, version=version)

        achivements = await ACHIEV_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return achivements # type: ignore
        

    @strawberry.field(name='relic')
    async def get_relic(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> Relic:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            relic = await RELIC_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return relic # type: ignore
        
        elif name:
            relic = await RELIC_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return relic # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='relics')
    async def get_relics(self, lang: str = 'en') -> List[Relic]:
        version = 'global'
        check_params(lang=lang, version=version)

        relics = await RELIC_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return relics # type: ignore
    
    @strawberry.field(name='outfit')
    async def get_outfit(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> Outfit:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            outfit = await OUTFIT_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return outfit # type: ignore
        
        elif name:
            outfit = await OUTFIT_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return outfit # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='outfits')
    async def get_outfits(self, lang: str = 'en') -> List[Outfit]:
        version = 'global'
        check_params(lang=lang, version=version)

        outfits = await OUTFIT_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return outfits # type: ignore

    @strawberry.field(name='servant')
    async def get_servant(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> SmartServant:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            servant = await SERVAN_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return servant # type: ignore
        
        elif name:
            servant = await SERVAN_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return servant # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='servants')
    async def get_servants(self, lang: str = 'en') -> List[SmartServant]:
        version = 'global'
        check_params(lang=lang, version=version)

        servants = await SERVAN_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return servants # type: ignore

    @strawberry.field(name='mount')
    async def get_mount(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> Mount:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            mount = await MOUNTS_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return mount # type: ignore
        
        elif name:
            mount = await MOUNTS_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return mount # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='mounts')
    async def get_mounts(self, lang: str = 'en') -> List[Mount]:
        version = 'global'
        check_params(lang=lang, version=version)

        mounts = await MOUNTS_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return mounts # type: ignore
        

    @strawberry.field(name='food')
    async def get_food(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> Food:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            food = await FOOD_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return food # type: ignore
        
        elif name:
            food = await FOOD_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return food # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='foods')
    async def get_foods(self, lang: str = 'en') -> List[Food]:
        version = 'global'
        check_params(lang=lang, version=version)

        foods = await FOOD_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return foods # type: ignore
        

    @strawberry.field(name='item')
    async def get_item(self, id: str | None = None, name: str | None = None, lang: str = 'en') -> Item:
        version = 'global'
        check_params(lang=lang, version=version)

        if id:
            item = await ITEM_REPO.get(EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version))
            return item # type: ignore
        
        elif name:
            item = await ITEM_REPO.get_by_name(name=name, lang=lang, version=VERSIONS(version))
            return item # type: ignore
        
        raise MissingArgument

    @strawberry.field(name='items')
    async def get_items(self, lang: str = 'en') -> List[Item]:
        version = 'global'
        check_params(lang=lang, version=version)

        items = await ITEM_REPO.get_all(lang=LANGS(lang), version=VERSIONS(version))
        return items # type: ignore
        
    

graphql = GraphQLRouter[Any, Any](schema=strawberry.Schema(query=Query), path='/') 
METADATA = {
    'name': 'GraphQL',
    'description': 'GraphQL provides a complete and understandable description of the data \n\n **SOME FIELDS CONTAINS CN DATA**',
    'externalDocs': {
        'description': 'GraphQL docs',
        'url': 'https://api.toweroffantasy.info/',
    }
}