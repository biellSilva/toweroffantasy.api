from collections.abc import Callable, Generator
from enum import StrEnum
from typing import Annotated, Any

from pydantic import (
    AfterValidator,
    AliasChoices,
    BeforeValidator,
    Field,
    GetCoreSchemaHandler,
    ValidationInfo,
)
from pydantic_core import core_schema

from src._settings import config

__all__ = ("AssetPath", "LangsEnum", "Translate")


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


def _modify_asset_path(value: str, info: ValidationInfo) -> str:
    if config.ASSETS_PREFIX in value:
        return value

    if "L10N" in value:
        lang = info.context.get(  # type: ignore[assignment]
            "lang",
            "MISSING_LANG",
        )  # Default to English
        return f"{config.ASSETS_PREFIX}/Hotta/Content{value.format(lang)}"

    return f"{config.ASSETS_PREFIX}/Hotta/Content/Resources{value}"


AssetPath = Annotated[
    str,
    AfterValidator(_modify_asset_path),
]

ObjectIdType = Annotated[
    str,
    Field(validation_alias=AliasChoices("_id", "object_id")),
    BeforeValidator(lambda x: str(x)),
]


class Translate(str):
    """Translate field."""

    __slots__ = ()

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., str], Any, None]:
        """Get validators."""
        yield cls.validate

    @classmethod
    def validate(cls, value: Any, _: Any) -> str:
        """Validate the value."""
        if not isinstance(value, str):
            msg = "Value must be a string."
            raise TypeError(msg)
        return value

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source: type[Any],
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        if source is not Translate:
            msg = f"Expected source to be Translate, got {source}"
            raise TypeError(msg)

        return core_schema.no_info_after_validator_function(
            cls._validate,
            core_schema.str_schema(),
        )

    @staticmethod
    def _validate(value: Any) -> str:
        if not isinstance(value, str):
            msg = "Value must be a string."
            raise TypeError(msg)
        return value


class TranslateWithValues(Translate):
    """Translate field with values."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source: type[Any],
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        if source is not TranslateWithValues:
            msg = f"Expected source to be TranslateWithValues, got {source}"
            raise TypeError(msg)

        return core_schema.no_info_after_validator_function(
            cls._validate,
            core_schema.str_schema(),
        )


class TranslateSplitBreakLine(Translate):
    """Translate field with values."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source: type[Any],
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        if source is not TranslateSplitBreakLine:
            msg = f"Expected source to be TranslateSplitBreakLine, got {source}"
            raise TypeError(msg)

        return core_schema.no_info_after_validator_function(
            cls._validate,
            core_schema.str_schema(),
        )
