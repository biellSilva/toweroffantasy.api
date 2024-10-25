from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import DeclarativeBase

if TYPE_CHECKING:
    from pydantic import BaseModel


class BaseTable(DeclarativeBase):
    """Base model for all models."""

    def update(self, model: "BaseModel", exclude: set[str] | None = None) -> None:
        """Update the model with the given data."""
        for key, value in model.model_dump(
            exclude_defaults=True,
            exclude_unset=True,
            exclude=exclude,
        ).items():
            setattr(self, key, value)

    def model_dump(self) -> dict[str, Any]:
        """Return a dictionary representation of the model."""
        _return: dict[str, Any] = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue

            _return[key] = value

            if isinstance(value, list):
                items: list[Any] = []
                item: Any
                for item in value:
                    if isinstance(item, BaseTable):
                        items.append(item.model_dump())
                    else:
                        items.append(item)

                _return[key] = items
                continue

        return _return
