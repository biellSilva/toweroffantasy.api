from typing import Annotated
from pydantic import AliasChoices, BaseModel, Field


class GuideBookItem(BaseModel):
    title: str
    description: str
    icon: Annotated[str, Field(validation_alias=AliasChoices("icon", "photo"))]
