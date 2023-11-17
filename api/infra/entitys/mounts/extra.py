
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import replace_icon


class MountAsset(BaseModel):
    icon: Annotated[str, BeforeValidator(replace_icon)] = Field(alias='Icon', serialization_alias='icon')
    showImage: Annotated[str, BeforeValidator(replace_icon)] = Field(alias='ShowImage', serialization_alias='showImage')