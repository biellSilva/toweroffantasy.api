from typing import Any, List

import strawberry
from fastapi import Request
from strawberry.fastapi import GraphQLRouter
from strawberry.http import GraphQLHTTPResponse
from strawberry.types import ExecutionResult

from src.domain.models.simulacra import SimulacraType
from src.domain.models.weapons import WeaponType
from src.main.factories.controller.simulacra.find import FindSimulacraControllerFactory
from src.main.factories.controller.simulacra.getall import (
    GetallSimulacraControllerFactory,
)
from src.main.factories.controller.weapons.find import FindWeaponsControllerFactory
from src.main.factories.controller.weapons.get_all import GetAllWeaponsControllerFactory


class TOFGraphQLRouter(GraphQLRouter[Any, Any]):
    async def process_result(
        self, request: Request, result: ExecutionResult
    ) -> GraphQLHTTPResponse:
        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors:
            data["errors"] = [
                {
                    "err_class": err.original_error.__class__.__name__,
                    "status_code": int(err.message.split(":")[0].strip()),
                    "detail": err.message.split(":")[1].strip(),
                }
                for err in result.errors
            ]

        if result.extensions:
            data["extensions"] = result.extensions

        return data


@strawberry.type
class Query:
    simulacrum: SimulacraType = strawberry.field(
        resolver=FindSimulacraControllerFactory.create().handle
    )
    simulacra: List[SimulacraType] = strawberry.field(
        resolver=GetallSimulacraControllerFactory.create().handle
    )

    weapon: WeaponType = strawberry.field(
        resolver=FindWeaponsControllerFactory.create().handle
    )
    weapons: List[WeaponType] = strawberry.field(
        resolver=GetAllWeaponsControllerFactory.create().handle
    )


router = TOFGraphQLRouter(
    schema=strawberry.Schema(query=Query), path="/graphql", allow_queries_via_get=False
)
