from typing import Any

import strawberry
from fastapi import HTTPException, Request
from strawberry.fastapi import GraphQLRouter
from strawberry.http import GraphQLHTTPResponse
from strawberry.types import ExecutionResult

from .query import Query


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
                            "status_code": err.original_error.status_code,
                            "detail": err.original_error.detail,
                        }
                    )
                else:
                    data["errors"].append(err.formatted)

        if result.extensions:
            data["extensions"] = result.extensions

        return data


router = TOFGraphQLRouter(
    schema=strawberry.Schema(query=Query),
    path="/graphql",
    allow_queries_via_get=False,
)
