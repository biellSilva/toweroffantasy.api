from types import UnionType
from typing import Any, get_args, get_origin

from pydantic import BaseModel, ConfigDict, ValidationInfo, model_validator

from src._types import Translate, TranslateSplitBreakLine, TranslateWithValues
from src._utils import needs_translation, needs_values, truncate_value
from src.common.translator import Translator


class ModelBase(BaseModel):
    """Base model for all models."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @model_validator(mode="before")
    @classmethod
    def validate_translation(  # noqa: C901
        cls,
        data: dict[str, Any],
        info: ValidationInfo,
    ) -> dict[str, Any]:
        """Translate the data to the simple model."""
        if not info.context or not isinstance(info.context, dict):
            msg = "Context is required for translation."
            raise ValueError(msg)

        context: dict[str, Any] = info.context  # type: ignore
        lang = context.get("lang", "en")

        for key, value in cls.model_fields.items():
            if value.annotation == Translate or (
                get_origin(value.annotation) is UnionType
                and any(arg == Translate for arg in get_args(value.annotation))
            ):
                field = data.get(key)
                if isinstance(field, str) and needs_translation(field):
                    data[key] = Translator.translate(
                        lang=lang,
                        key=data[key],
                    )

            elif value.annotation == TranslateWithValues or (
                get_origin(value.annotation) is UnionType
                and any(
                    arg == TranslateWithValues for arg in get_args(value.annotation)
                )
            ):
                field = data.get(key)
                if isinstance(field, str) and needs_translation(field):
                    data[key] = Translator.translate(
                        lang=lang,
                        key=data[key],
                    )
                    if needs_values(data[key]):
                        data[key] = data[key].format(
                            *[
                                truncate_value(value)
                                for value in data.get("values", [])
                            ],
                        )

            elif get_origin(value.annotation) is list and any(
                type_ in (Translate, TranslateSplitBreakLine)
                for type_ in get_args(value.annotation)
            ):
                items = [
                    Translator.translate(lang=lang, key=item)
                    if isinstance(item, str) and needs_translation(item)
                    else item
                    for item in data.get(key, [])
                ]

                if items and needs_values(items[0]):
                    items = [
                        item.format(
                            *[
                                truncate_value(value)
                                for value in data.get("values", [])
                            ],
                        )
                        for item in items
                    ]

                if TranslateSplitBreakLine in get_args(value.annotation) and items:
                    items = [line for item in items for line in item.split("\r\n")]

                data[key] = items
        return data
