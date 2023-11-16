
import strawberry

from strawberry.fastapi import GraphQLRouter
from typing import List, Any

from api.enums import langs as LANGS
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


def check_lang(lang: str):
    if lang not in LANGS:
        raise Exception(f'({lang}) is not a valid language {LANGS}')


@strawberry.type
class Query:

    @strawberry.field(name='simulacrum')
    async def get_simulacrum(self, id: str, lang: str = 'en') -> SimulacraType:
        check_lang(lang=lang)

        if simulacra := await SIMU_REPO.get(EntityBase(id=id), lang=lang):
            return simulacra # type: ignore
        
        raise Exception(f'Can\'t find {id} in {lang}')


    @strawberry.field(name='simulacra')
    async def get_simulacra(self, lang: str = 'en') -> List[SimulacraType]:
        check_lang(lang=lang)
        
        if simulacras := await SIMU_REPO.get_all(lang=lang):
            return simulacras # type: ignore
        
        raise Exception(f'Can\'t find {lang}')


    @strawberry.field(name='simulacrumv2')
    async def get_simulacrum_v2(self, id: str, lang: str = 'en') -> SimulacraTypeV2:
        check_lang(lang=lang)

        if simulacra := await SIMU_V2_REPO.get(EntityBase(id=id), lang=lang):
            return simulacra # type: ignore
        
        raise Exception(f'Can\'t find {id} in {lang}')
 

    @strawberry.field(name='simulacrav2')
    async def get_simulacra_v2(self, lang: str = 'en') -> List[SimulacraTypeV2]:
        check_lang(lang=lang)
        
        if simulacras := await SIMU_V2_REPO.get_all(lang=lang):
            return simulacras # type: ignore
        
        raise Exception(f'Can\'t find {lang}')
    


    @strawberry.field(name='weapon')
    async def get_weapon(self, id: str, lang: str = 'en') -> WeaponType:
        check_lang(lang=lang)

        if weapon := await WEAPON_REPO.get(EntityBase(id=id), lang=lang):
            return weapon # type: ignore
        
        raise Exception(f'Can\'t find {id} in {lang}')

    @strawberry.field(name='weapons')
    async def get_weapons(self, lang: str = 'en') -> List[WeaponType]:
        check_lang(lang=lang)

        if weapons := await WEAPON_REPO.get_all(lang=lang):
            return weapons # type: ignore
        
        raise Exception(f'Can\'t find {lang}')


    @strawberry.field(name='matrice')
    async def get_matrice(self, id: str, lang: str = 'en') -> MatriceType:
        check_lang(lang=lang)

        if matrice := await MATRICE_REPO.get(EntityBase(id=id), lang=lang):
            return matrice # type: ignore
        
        raise Exception(f'Can\'t find {id} in {lang}')

    @strawberry.field(name='matrices')
    async def get_matrices(self, lang: str = 'en') -> List[MatriceType]:
        check_lang(lang=lang)

        if matrices := await MATRICE_REPO.get_all(lang=lang):
            return matrices # type: ignore
        
        raise Exception(f'Can\'t find {lang}')




graphql = GraphQLRouter[Any, Any](schema=strawberry.Schema(query=Query), path='/') 