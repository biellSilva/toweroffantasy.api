
from pydantic import BaseModel, BeforeValidator, model_validator
from typing import Annotated, Any


class EntityBase(BaseModel):
    id: Annotated[str, BeforeValidator(lambda x: str(x).lower())]


    @model_validator(mode='before')
    def _camelcase_property_keys__(cls, values: Any) -> Any:
        def _camel__(value: Any) -> Any:

            if isinstance(value, dict):
                return {str(k)[0].lower() + k[1:]: _camel__(v) for k, v in value.items() if k} # type: ignore

            return value

        return _camel__(values)


    def custom_model_dump(self, include: set[str] | None = None, exclude: set[str] | None = None):
        return self.__pascal_to_camel_dict(self.model_dump(include=include))


    def __pascal_to_camel_dict(self, d: dict[Any, Any]) -> dict[str, Any]:
        def pascal_to_camel(string: str) -> str:
            return string[0].lower() + string[1:]

        def process_value(v: Any):
            if isinstance(v, dict):
                return self.__pascal_to_camel_dict(v) # type: ignore
            
            else:
                return v

        return {pascal_to_camel(k): process_value(v) for k, v in d.items()}