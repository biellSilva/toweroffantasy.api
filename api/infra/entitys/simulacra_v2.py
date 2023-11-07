
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.entitys.weapons import Weapon
from api.entitys.matrices import Matrice
from api.utils import replace_cv



class VoiceActors(BaseModel):
    chinese: Annotated[str, BeforeValidator(replace_cv)] | None = None
    japanese: Annotated[str, BeforeValidator(replace_cv)] | None = None
    english: Annotated[str, BeforeValidator(replace_cv)] | None = None
    korean: Annotated[str, BeforeValidator(replace_cv)] | None = None
    portuguese: Annotated[str, BeforeValidator(replace_cv)] | None = None


class Simulacra_v2(BaseModel):
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
    weapon: Weapon | None = None
    matrice: Matrice | None = None

