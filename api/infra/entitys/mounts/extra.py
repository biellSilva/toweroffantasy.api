
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import replace_icon


class MountAsset(BaseModel):
    icon: Annotated[str, BeforeValidator(replace_icon)]
    showImage: Annotated[str, BeforeValidator(replace_icon)]