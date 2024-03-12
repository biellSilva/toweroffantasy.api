from typing import Any, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def filter_models(models: list[T], filter_dict: dict[str, Any]) -> list[T]:
    filtered_models: list[T] = []

    for model in models:
        is_match = True

        for filter_key, filter_value in filter_dict.items():
            keys = filter_key.split(".")
            current_value = model

            for k in keys:
                if isinstance(current_value, list):
                    for item in current_value:
                        item: Any

                        if isinstance(item, (BaseModel)) and hasattr(item, k):
                            if getattr(item, k) == filter_value:
                                current_value = getattr(item, k)
                                break

                elif hasattr(current_value, k):
                    current_value = getattr(current_value, k)
                else:
                    is_match = False
                    break

            if is_match and (
                current_value == filter_value
                or (isinstance(current_value, list) and filter_value in current_value)
            ):
                filtered_models.append(model)
                break

    return filtered_models
