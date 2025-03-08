from pydantic import BaseModel


class Pagination[T: BaseModel](BaseModel):
    data: list[T]
    total_items: int
    page: int
    max_page: int
    limit: int


def paginate_items[T: BaseModel](
    data: list[T],
    page: int,
    limit: int,
) -> Pagination[T]:
    start = (page - 1) * limit
    return Pagination[T](
        data=data[start : start + limit],
        total_items=len(data),
        page=page,
        max_page=(len(data) + limit - 1) // limit,
        limit=limit,
    )
