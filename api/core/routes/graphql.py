
import strawberry

from strawberry.fastapi import GraphQLRouter
from typing import List

from api.enums import langs as LANGS
from api.infra.repository import SimulacraRepo
from api.infra.entitys import EntityBase

from api.infra.entitys.simulacra.graphql.simulacra import SimulacraType


SIMU_REPO = SimulacraRepo()


@strawberry.type
class Query:

    @strawberry.field(name='simulacrum')
    async def get_simulacrum(self, id: str, lang: str = 'en') -> SimulacraType:
        if lang not in LANGS:
            raise Exception(f'({lang}) is not a valid language {LANGS}')
        
        if simulacra := await SIMU_REPO.get(EntityBase(id=id), lang=lang):
            return simulacra # type: ignore
        
        raise Exception(f'Can\'t find {id} in {lang}')
 

    @strawberry.field(name='simulacra')
    async def get_simulacra(self, lang: str = 'en') -> List[SimulacraType]:
        if lang not in LANGS:
            raise Exception(f'({lang}) is not a valid language {LANGS}')
        
        if simulacras := await SIMU_REPO.get_all(lang=lang):
            return simulacras # type: ignore
        
        raise Exception(f'Can\'t find {lang}')


schema = strawberry.Schema(query=Query)

graphql = GraphQLRouter(schema=schema, path='/')  # type: ignore