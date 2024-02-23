import pytest

from src.enums import LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.infra.repository.items import ItemsRepository


class ItemsSuite:

    @pytest.mark.asyncio
    async def global_de_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("de")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_en_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("en")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_es_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("es")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_fr_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("fr")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_id_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("id")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_ja_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("ja")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_pt_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("pt")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_ru_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("ru")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_th_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("th")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_zh_cn_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("zh-cn")
        )
        assert len(DATA) != 0

    @pytest.mark.asyncio
    async def global_zh_hans_sg_test(self):
        REPO = ItemsRepository()

        DATA = await REPO.get_all(
            version=VERSIONS_ENUM("global"), lang=LANGS_GLOBAL_ENUM("zh-hans-sg")
        )
        assert len(DATA) != 0
