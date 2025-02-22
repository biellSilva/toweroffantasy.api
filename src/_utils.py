from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import BaseModel
from unidecode import unidecode


def current_datetime() -> datetime:
    return datetime.now(ZoneInfo("America/Sao_Paulo"))


def paginate_items[T: BaseModel](
    data: list[T],
    page: int,
    limit: int,
) -> list[T]:
    start = (page - 1) * limit
    return data[start : start + limit]


def is_str_in_list(
    param: str,
    list_: list[str],
    *,
    equals: bool = False,
) -> bool:
    if equals:
        return any(
            unidecode(param).lower() == unidecode(item).lower() for item in list_
        )

    return any(unidecode(param).lower() in unidecode(item).lower() for item in list_)
