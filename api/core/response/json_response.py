
import json, typing

from fastapi.responses import Response
from starlette.background import BackgroundTask


class PrettyJsonResponse(Response):
    media_type = 'application/json'

    def __init__(self, content: typing.Any, status_code: int = 200, 
                 headers: typing.Mapping[str, str] | None = None, media_type: str | None = None, 
                 background: BackgroundTask | None = None) -> None:
        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content: dict[str, typing.Any]) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")