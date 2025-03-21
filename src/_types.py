from enum import StrEnum
from typing import Annotated

from pydantic import AfterValidator

from src._settings import config

__all__ = ("AssetPath", "LangsEnum")


class LangsEnum(StrEnum):
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    ID = "id"
    JA = "ja"
    PT = "pt"
    RU = "ru"
    TH = "th"
    ZH_CN = "zh-CN"


def _modify_asset_path(value: str) -> str:
    if config.ASSETS_PREFIX in value:
        return value

    if "L10N" in value:
        return f"{config.ASSETS_PREFIX}/Hotta/Content{value}"

    return f"{config.ASSETS_PREFIX}/Hotta/Content/Resources{value}"


AssetPath = Annotated[
    str,
    AfterValidator(_modify_asset_path),
]
