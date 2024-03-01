import strawberry
from src.domain.models.base import ModelBase


class Outfit(ModelBase):
    name: str | None = None
    type: str
    description: str | None = None
    source: str | None = None
    icon: str | None


@strawberry.experimental.pydantic.type(model=Outfit, all_fields=True)
class OutfitType:
    pass
