
import strawberry

from strawberry.fastapi import GraphQLRouter
from typing import List

from api.infra.repository import SimulacraRepo
from api.infra.entitys import EntityBase

from api.infra.entitys.simulacra.graphql.simulacra import SimulacraType

SIMU_REPO = SimulacraRepo()



@strawberry.type
class Query:

    @strawberry.field(name='simulacrum')
    async def get_simulacrum(self, id: str, lang: str = 'en') -> SimulacraType | None:
        if simulacra := await SIMU_REPO.get(EntityBase(id=id), lang=lang):
            return simulacra # type: ignore
 

    @strawberry.field(name='simulacra')
    async def get_simulacra(self, lang: str = 'en') -> List[SimulacraType]:
        if simulacras := await SIMU_REPO.get_all(lang=lang):
            return simulacras # type: ignore
        
        return []


schema = strawberry.Schema(query=Query)

graphql = GraphQLRouter(schema=schema, path='/')  # type: ignore