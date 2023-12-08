
from pydantic import BaseModel, model_validator
from typing import Any


class Assets(BaseModel):
    avatar: str 
    icon: str 
    lotteryCardImage: str 
    lotteryDrawing: str 
    painting: str 
    namePicture: str 
    grayPainting: str
    thumbPainting: str 
    weaponShowPicture: str 
    hasGotAwakenEntrance: str 
    notGotAwakenEntrance: str 
    advancePainting: str 
    advanceGrayPainting: str 
    backPhoto: str 
    rarityIcon: str 
    soloLeagueBanPickBanner: str 
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
    cn: str | None
    jp: str | None
    en: str | None
    kr: str | None
    pt: str | None

    @model_validator(mode='before')
    def _replace_strings(cls, values: Any):

        def _replace_string__(value: Any) -> Any:
            if isinstance(value, dict):
                _: dict[str, Any] = {}

                for k, v in values.items():
                    if isinstance(v, str):
                        if v.startswith(' '):
                            _.update({k: v[1:]})

                    else:
                        _.update({k: v})

                return _
            
            return value

        return _replace_string__(values)


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