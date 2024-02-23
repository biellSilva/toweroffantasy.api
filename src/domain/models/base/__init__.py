from typing import Annotated, Any
from pydantic import BaseModel, BeforeValidator, model_validator


class ModelBase(BaseModel):
    id: Annotated[str, BeforeValidator(lambda x: str(x).lower())]

    @model_validator(mode="before")
    def _camelcase_property_keys__(cls, values: Any) -> Any:
        def _camel__(value: Any) -> Any:

            if isinstance(value, dict):
                return {str(k)[0].lower() + k[1:]: _camel__(v) for k, v in value.items() if k != ""}  # type: ignore

            return value

        return _camel__(values)
