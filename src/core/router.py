from collections.abc import Awaitable, Callable, Mapping, MutableMapping, Sequence
from contextlib import AbstractAsyncContextManager
from enum import Enum
from typing import Any

from fastapi import APIRouter, Response, Security
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from fastapi.types import DecoratedCallable, IncEx
from fastapi.utils import generate_unique_id
from starlette.routing import BaseRoute

from src.exceptions.base import ApiError
from src.exceptions.unauthorized import (
    ExpiredTokenError,
    InvalidTokenError,
    MissingTokenError,
)
from src.security.auth import AuthSecurity


class ApiRouter(APIRouter):
    """Custom class to extend the `APIRouter` class from FastAPI.

    `APIRouter` class, used to group *path operations*, for example to structure
    an app in multiple files. It would then be included in the `FastAPI` app, or
    in another `APIRouter` (ultimately included in the app).

    Read more about it in the
    [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

    ## Example

    ```python
    from fastapi import APIRouter, FastAPI

    app = FastAPI()
    router = APIRouter()


    @router.get("/users/", tags=["users"])
    async def read_users():
        return [{"username": "Rick"}, {"username": "Morty"}]


    app.include_router(router)
    ```
    """

    def __init__(  # noqa: PLR0913
        self,
        *,
        prefix: str = "",
        tags: list[str | Enum] | None = None,
        dependencies: Sequence[Depends] | None = None,
        default_response_class: type[Response] = JSONResponse,
        responses: dict[int | str, dict[str, Any]] | None = None,
        callbacks: list[BaseRoute] | None = None,
        routes: list[BaseRoute] | None = None,
        redirect_slashes: bool = True,
        default: Callable[
            [
                MutableMapping[str, Any],
                Callable[[], Awaitable[MutableMapping[str, Any]]],
                Callable[[MutableMapping[str, Any]], Awaitable[None]],
            ],
            Awaitable[None],
        ]
        | None = None,
        route_class: type[APIRoute] = APIRoute,
        on_startup: Sequence[Callable[[], Any]] | None = None,
        on_shutdown: Sequence[Callable[[], Any]] | None = None,
        lifespan: Callable[[Any], AbstractAsyncContextManager[None]]
        | Callable[[Any], AbstractAsyncContextManager[Mapping[str, Any]]]
        | None = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        generate_unique_id_function: Callable[[APIRoute], str] = generate_unique_id,
        requires_login: bool = False,
        exceptions: Sequence[ApiError | type[ApiError]] | None = None,
    ) -> None:
        super().__init__(
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            default_response_class=default_response_class,
            responses=responses,
            callbacks=callbacks,
            routes=routes,
            redirect_slashes=redirect_slashes,
            default=default,
            dependency_overrides_provider=None,
            route_class=route_class,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            lifespan=lifespan,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            generate_unique_id_function=generate_unique_id_function,
        )
        self.requires_login = requires_login
        self.exceptions = exceptions

    def handle_exceptions(
        self,
        *exceptions: ApiError | type[ApiError],
        responses: dict[int | str, dict[str, Any]] | None,
    ) -> dict[int | str, dict[str, Any]]:
        """Generate a schema for the given exception class.

        Args:
            exceptions (ApiError): The exception class to generate the schema for.
            responses (dict[str | int, Any], optional): The base schema to add the
                exception to. Defaults to None.

        """
        if responses is None:
            responses = {}

        for exception in exceptions:
            exc = exception() if isinstance(exception, type) else exception

            if exc.status_code not in responses:
                responses[exc.status_code] = {
                    "content": {
                        "application/json": {
                            "examples": {
                                exc.__class__.__name__: {
                                    "value": exc.__dict__,
                                },
                            },
                        },
                    },
                }
            else:
                responses[exc.status_code]["content"]["application/json"]["examples"][
                    exc.__class__.__name__
                ] = {
                    "value": exc.__dict__,
                }

        return responses

    def handle_requires_login(
        self,
        *,
        requires_login: bool,
        dependencies: Sequence[Depends] | None = None,
        responses: dict[int | str, dict[str, Any]] | None = None,
    ) -> tuple[Sequence[Depends] | None, dict[int | str, dict[str, Any]] | None]:
        """Handle the `requires_login` attribute."""
        if self.requires_login or requires_login:
            if dependencies is None:
                dependencies = []
            dependencies.append(Security(AuthSecurity()))  # type: ignore[attr-defined]
            responses = self.handle_exceptions(
                MissingTokenError(),
                InvalidTokenError(),
                ExpiredTokenError(),
                responses=responses,
            )
        return dependencies, responses

    def api_route(  # noqa: PLR0913
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: int | None = None,
        tags: list[str | Enum] | None = None,
        dependencies: Sequence[Depends] | None = None,
        summary: str | None = None,
        description: str | None = None,
        response_description: str = "Successful Response",
        responses: dict[int | str, dict[str, Any]] | None = None,
        deprecated: bool | None = None,
        methods: list[str] | None = None,
        operation_id: str | None = None,
        response_model_include: IncEx | None = None,
        response_model_exclude: IncEx | None = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type[Response] = JSONResponse,
        name: str | None = None,
        callbacks: list[BaseRoute] | None = None,
        openapi_extra: dict[str, Any] | None = None,
        generate_unique_id_function: Callable[[APIRoute], str] = generate_unique_id,
        requires_login: bool = False,
        exceptions: Sequence[ApiError | type[ApiError]] | None = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        dependencies, responses = self.handle_requires_login(
            requires_login=requires_login,
            dependencies=dependencies,
            responses=responses,
        )

        if exceptions:
            responses = self.handle_exceptions(
                *exceptions,
                responses=responses,
            )
        return super().api_route(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            methods=methods,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
        )

    def get(  # noqa: PLR0913
        self,
        path: str,
        *,
        response_model: Any = None,
        status_code: int | None = None,
        tags: list[str | Enum] | None = None,
        dependencies: Sequence[Depends] | None = None,
        summary: str | None = None,
        description: str | None = None,
        response_description: str = "Successful Response",
        responses: dict[int | str, dict[str, Any]] | None = None,
        deprecated: bool | None = None,
        operation_id: str | None = None,
        response_model_include: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_exclude: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type[Response] = JSONResponse,
        name: str | None = None,
        callbacks: list[BaseRoute] | None = None,
        openapi_extra: dict[str, Any] | None = None,
        generate_unique_id_function: Callable[[APIRoute], str] = generate_unique_id,
        requires_login: bool = False,
        exceptions: Sequence[ApiError | type[ApiError]] | None = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.api_route(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
            requires_login=requires_login,
            exceptions=exceptions,
        )

    def post(  # noqa: PLR0913
        self,
        path: str,
        *,
        response_model: Any = None,
        status_code: int | None = None,
        tags: list[str | Enum] | None = None,
        dependencies: Sequence[Depends] | None = None,
        summary: str | None = None,
        description: str | None = None,
        response_description: str = "Successful Response",
        responses: dict[int | str, dict[str, Any]] | None = None,
        deprecated: bool | None = None,
        operation_id: str | None = None,
        response_model_include: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_exclude: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type[Response] = JSONResponse,
        name: str | None = None,
        callbacks: list[BaseRoute] | None = None,
        openapi_extra: dict[str, Any] | None = None,
        generate_unique_id_function: Callable[[APIRoute], str] = generate_unique_id,
        requires_login: bool = False,
        exceptions: Sequence[ApiError | type[ApiError]] | None = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.api_route(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
            requires_login=requires_login,
            exceptions=exceptions,
        )

    def put(  # noqa: PLR0913
        self,
        path: str,
        *,
        response_model: Any = None,
        status_code: int | None = None,
        tags: list[str | Enum] | None = None,
        dependencies: Sequence[Depends] | None = None,
        summary: str | None = None,
        description: str | None = None,
        response_description: str = "Successful Response",
        responses: dict[int | str, dict[str, Any]] | None = None,
        deprecated: bool | None = None,
        operation_id: str | None = None,
        response_model_include: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_exclude: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type[Response] = JSONResponse,
        name: str | None = None,
        callbacks: list[BaseRoute] | None = None,
        openapi_extra: dict[str, Any] | None = None,
        generate_unique_id_function: Callable[[APIRoute], str] = generate_unique_id,
        requires_login: bool = False,
        exceptions: Sequence[ApiError | type[ApiError]] | None = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.api_route(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
            requires_login=requires_login,
            exceptions=exceptions,
        )

    def patch(  # noqa: PLR0913
        self,
        path: str,
        *,
        response_model: Any = None,
        status_code: int | None = None,
        tags: list[str | Enum] | None = None,
        dependencies: Sequence[Depends] | None = None,
        summary: str | None = None,
        description: str | None = None,
        response_description: str = "Successful Response",
        responses: dict[int | str, dict[str, Any]] | None = None,
        deprecated: bool | None = None,
        operation_id: str | None = None,
        response_model_include: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_exclude: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type[Response] = JSONResponse,
        name: str | None = None,
        callbacks: list[BaseRoute] | None = None,
        openapi_extra: dict[str, Any] | None = None,
        generate_unique_id_function: Callable[[APIRoute], str] = generate_unique_id,
        requires_login: bool = False,
        exceptions: Sequence[ApiError | type[ApiError]] | None = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.api_route(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
            requires_login=requires_login,
            exceptions=exceptions,
        )

    def delete(  # noqa: PLR0913
        self,
        path: str,
        *,
        response_model: Any = None,
        status_code: int | None = None,
        tags: list[str | Enum] | None = None,
        dependencies: Sequence[Depends] | None = None,
        summary: str | None = None,
        description: str | None = None,
        response_description: str = "Successful Response",
        responses: dict[int | str, dict[str, Any]] | None = None,
        deprecated: bool | None = None,
        operation_id: str | None = None,
        response_model_include: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_exclude: set[int]
        | set[str]
        | dict[int, Any]
        | dict[str, Any]
        | None = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type[Response] = JSONResponse,
        name: str | None = None,
        callbacks: list[BaseRoute] | None = None,
        openapi_extra: dict[str, Any] | None = None,
        generate_unique_id_function: Callable[[APIRoute], str] = generate_unique_id,
        requires_login: bool = False,
        exceptions: Sequence[ApiError | type[ApiError]] | None = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.api_route(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
            requires_login=requires_login,
            exceptions=exceptions,
        )
