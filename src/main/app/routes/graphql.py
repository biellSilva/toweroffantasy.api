from typing import Any, List

import strawberry
from fastapi import HTTPException, Request
from strawberry.fastapi import GraphQLRouter
from strawberry.http import GraphQLHTTPResponse
from strawberry.types import ExecutionResult
from src.domain.models.food import FoodType

from src.domain.models.matrices import MatrixType
from src.domain.models.mounts import MountType
from src.domain.models.relics import RelicType
from src.domain.models.simulacra import SimulacraType
from src.domain.models.simulacra_v2 import SimulacraV2Type
from src.domain.models.weapons import WeaponType
from src.main.factories.controller.food.find import FindFoodControllerFactory
from src.main.factories.controller.food.get_all import GetAllFoodControllerFactory
from src.main.factories.controller.matrices.find import FindMatricesControllerFactory
from src.main.factories.controller.matrices.get_all import (
    GetAllMatricesControllerFactory,
)
from src.main.factories.controller.mount.find import FindMountControllerFactory
from src.main.factories.controller.mount.get_all import GetAllMountControllerFactory
from src.main.factories.controller.relics.find import FindRelicsControllerFactory
from src.main.factories.controller.relics.get_all import GetAllRelicsControllerFactory
from src.main.factories.controller.simulacra.find import FindSimulacraControllerFactory
from src.main.factories.controller.simulacra.getall import (
    GetallSimulacraControllerFactory,
)
from src.main.factories.controller.simulacra_v2.find import (
    FindSimulacraV2ControllerFactory,
)
from src.main.factories.controller.simulacra_v2.get_all import (
    GetAllSimulacraV2ControllerFactory,
)
from src.main.factories.controller.weapons.find import FindWeaponsControllerFactory
from src.main.factories.controller.weapons.get_all import GetAllWeaponsControllerFactory


class TOFGraphQLRouter(GraphQLRouter[Any, Any]):
    async def process_result(
        self, request: Request, result: ExecutionResult
    ) -> GraphQLHTTPResponse:
        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors:
            data["errors"] = []
            for err in result.errors:
                if isinstance(err.original_error, HTTPException):
                    data["errors"].append(
                        {
                            "err_class": err.original_error.__class__.__name__,
                            "status_code": int(err.message.split(":")[0].strip()),
                            "detail": err.message.split(":")[1].strip(),
                        }
                    )
                else:
                    data["errors"].append(err.formatted)

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

    matrix: MatrixType = strawberry.field(
        resolver=FindMatricesControllerFactory.create().handle
    )
    matrices: List[MatrixType] = strawberry.field(
        resolver=GetAllMatricesControllerFactory.create().handle
    )

    simulacrum_v2: SimulacraV2Type = strawberry.field(
        resolver=FindSimulacraV2ControllerFactory.create().handle
    )
    simulacra_v2: List[SimulacraV2Type] = strawberry.field(
        resolver=GetAllSimulacraV2ControllerFactory.create().handle
    )

    mount: MountType = strawberry.field(
        resolver=FindMountControllerFactory.create().handle
    )
    mounts: List[MountType] = strawberry.field(
        resolver=GetAllMountControllerFactory.create().handle
    )

    relic: RelicType = strawberry.field(
        resolver=FindRelicsControllerFactory.create().handle
    )
    relics: List[RelicType] = strawberry.field(
        resolver=GetAllRelicsControllerFactory.create().handle
    )

    food: FoodType = strawberry.field(
        resolver=FindFoodControllerFactory.create().handle
    )
    foods: List[FoodType] = strawberry.field(
        resolver=GetAllFoodControllerFactory.create().handle
    )


router = TOFGraphQLRouter(
    schema=strawberry.Schema(query=Query),
    path="/graphql",
    allow_queries_via_get=False,
)
