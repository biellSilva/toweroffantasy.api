
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import replace_cv



class VoiceActors(BaseModel):
    chinese: Annotated[str, BeforeValidator(replace_cv)] | None = None
    japanese: Annotated[str, BeforeValidator(replace_cv)] | None = None
    english: Annotated[str, BeforeValidator(replace_cv)] | None = None
    korean: Annotated[str, BeforeValidator(replace_cv)] | None = None
    portuguese: Annotated[str, BeforeValidator(replace_cv)] | None = None


class Simulacra(BaseModel):
    id: str
    name: str
    icon: str
    cnName: str
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str]
    voice_actors: VoiceActors

