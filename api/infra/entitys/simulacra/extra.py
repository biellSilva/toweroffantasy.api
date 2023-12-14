
from pydantic import BaseModel, model_validator, BeforeValidator
from typing import Any, Annotated

from api.utils import voice_actor_string_rework


class Assets(BaseModel):
    avatar: str
    titlePicture: str
    painting: str
    namePicture: str
    grayPainting: str
    thumbPainting: str
    weaponShowPicture: str
    activeImitation: str
    inactiveImitation:str
    advancePainting: str
    advanceGrayPainting: str
    backPhoto: str
    rarityIcon: str
    lotteryCardImage: str
    # lotteryDrawing: str
    matrixPainting: str
    descPainting: str

    @model_validator(mode='before')
    def _replace_assets(cls, values: Any):

        def _replace_string__(value: Any) -> Any:
            if isinstance(value, dict):
                _: dict[str, Any] = {}

                for k, v in values.items():
                    if isinstance(v, str):
                        _.update({k: v.replace('/Game/Resources', '/assets')})

                    else:
                        _.update({k: v})

                return _
            
            return value

        return _replace_string__(values)


class VoiceActors(BaseModel):
    cn: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    jp: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    en: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    kr: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None
    pt: Annotated[str, BeforeValidator(voice_actor_string_rework)] | None = None


class Awakening(BaseModel):
    name: str
    description: str
    icon: str
    need: int


    @model_validator(mode='before')
    def _replace_assets(cls, values: Any):

        def _replace_string__(value: Any) -> Any:
            if isinstance(value, dict):
                _: dict[str, Any] = {}

                for k, v in values.items():
                    if isinstance(v, str):
                        _.update({k: v.replace('/Game/Resources', '/assets')})

                    else:
                        _.update({k: v})

                return _
            
            return value

        return _replace_string__(values)