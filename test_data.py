import logging

from api.infra.repository import *
from api.enums import VERSIONS, LANGS, langs


def config_log():
    logger = logging.getLogger("")
    logger.setLevel("DEBUG")
    ch = logging.StreamHandler()
    ch.setLevel("DEBUG")
    formatter = logging.Formatter("%(name)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug("LOGGER STARTED")


async def test_global_data(lang: str):
    _logger = logging.getLogger(name=lang.upper())

    simulacra = [
        i.model_dump()
        for i in await SimulacraRepo().get_all(
            lang=LANGS(lang), version=VERSIONS("global")
        )
    ]
    _logger.info("simulacra: %s items", len(simulacra))

    weapons = [
        i.model_dump()
        for i in await WeaponRepo().get_all(
            lang=LANGS(lang), version=VERSIONS("global")
        )
    ]
    _logger.info("weapons: %s items", len(weapons))

    matrices = [
        i.model_dump()
        for i in await MatricesRepo().get_all(
            lang=LANGS(lang), version=VERSIONS("global")
        )
    ]
    _logger.info("matrices: %s items", len(matrices))

    simulacra_v2 = [
        i.model_dump()
        for i in await SimulacraV2Repo().get_all(
            lang=LANGS(lang), version=VERSIONS("global"), graphql=True
        )
    ]
    _logger.info("simulacra_v2: %s items", len(simulacra_v2))

    relics = [
        i.model_dump()
        for i in await RelicRepo().get_all(lang=LANGS(lang), version=VERSIONS("global"))
    ]
    _logger.info("relics: %s items", len(relics))

    food = [
        i.model_dump()
        for i in await FoodRepo().get_all(lang=LANGS(lang), version=VERSIONS("global"))
    ]
    _logger.info("food: %s items", len(food))

    items = [
        i.model_dump()
        for i in await ItemRepo().get_all(lang=LANGS(lang), version=VERSIONS("global"))
    ]
    _logger.info("items: %s items", len(items))

    achievs = [
        i.model_dump()
        for i in await AchievementRepo().get_all(
            lang=LANGS(lang), version=VERSIONS("global")
        )
    ]
    _logger.info("achievements: %s items", len(achievs))

    outfits = [
        i.model_dump()
        for i in await OutfitRepo().get_all(
            lang=LANGS(lang), version=VERSIONS("global")
        )
    ]
    _logger.info("outfits: %s items", len(outfits))

    mounts = [
        i.model_dump()
        for i in await MountsRepo().get_all(
            lang=LANGS(lang), version=VERSIONS("global")
        )
    ]
    _logger.info("mounts: %s items", len(mounts))

    servants = [
        i.model_dump()
        for i in await ServantsRepo().get_all(
            lang=LANGS(lang), version=VERSIONS("global")
        )
    ]
    _logger.info("servants: %s items", len(servants))


async def test_init():

    config_log()

    # global test
    for lang in langs:
        await test_global_data(lang=lang)


from asyncio import run

run(test_init())
