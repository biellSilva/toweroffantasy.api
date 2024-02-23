from typing import Annotated, Any

from pydantic import BaseModel, BeforeValidator, model_validator

from src.utils import to_lowercase


class ModelBase(BaseModel):
    id: Annotated[str, BeforeValidator(to_lowercase)]

    @model_validator(mode="before")
    def _camelcase_property_keys__(cls, values: Any) -> Any:
        def _camel__(value: Any) -> Any:

            if isinstance(value, dict):
                return {
                    cls.__to_camel(key): _camel__(value_)
                    for key, value_ in value.items()  # type: ignore
                    if isinstance(key, str) and key != ""
                }

            return value

        return _camel__(values)

    @classmethod
    def __to_camel(cls, text: str) -> str:
        return text[0].lower() + text[1:]
