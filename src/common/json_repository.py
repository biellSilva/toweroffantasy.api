from json import loads
from typing import Generic, TypeVar

import aiofiles

from src._types import LangsEnum
from src.common.base_model import ModelBase
from src.common.redis import Redis

SimpleModel = TypeVar("SimpleModel", bound=ModelBase)
Model = TypeVar("Model", bound=ModelBase)


class JsonRepository(Generic[SimpleModel, Model]):
    """Json repository for loading data from json files."""

    def __init__(
        self,
        filename: str,
        simple_model: type[SimpleModel],
        model: type[Model],
    ) -> None:
        self.filename = filename
        self.simple_model = simple_model
        self.model = model
        self._redis = Redis(name=filename)

    async def _load_json(self) -> dict[str, str]:
        """Load all items from the database."""
        async with aiofiles.open(f"src/database/{self.filename}.json") as file:
            return loads(await file.read())

    async def _translate_data(
        self,
        lang: str | LangsEnum,
    ) -> dict[str, Model]:
        """Translate the data to the simple model."""
        data = {
            id_: self.model.model_validate(data, context={"lang": lang})
            for id_, data in (await self._load_json()).items()
        }

        await self._redis.set_all(
            lang=lang,
            value_dict=data,
        )
        return data

    async def get_id(self, lang: str | LangsEnum, id_: str) -> Model | None:
        """Get all items from the database."""
        if data := await self._redis.get(lang=lang, key=id_):
            return self.model.model_validate(data, context={"lang": lang})

        data = await self._translate_data(lang)
        return data.get(id_, None)

    async def get_all(self, lang: str | LangsEnum) -> list[SimpleModel]:
        """Get all items from the database."""
        if data := await self._redis.get_all(lang=lang):
            return [
                self.simple_model.model_validate(value, context={"lang": lang})
                for value in data.values()
            ]

        return [
            self.simple_model.model_validate(value, context={"lang": lang})
            for value in (await self._translate_data(lang)).values()
        ]
