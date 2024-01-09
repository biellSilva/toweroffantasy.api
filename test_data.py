
import logging

from api.infra.repository import *
from api.enums import VERSIONS, LANGS, langs


def config_log():
    logger = logging.getLogger('')
    logger.setLevel('DEBUG')
    ch = logging.StreamHandler()
    ch.setLevel('DEBUG')
    formatter = logging.Formatter('%(name)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug('LOGGER STARTED')


async def test_global_data(lang: str):
    _logger = logging.getLogger(name=lang.upper())

    simulacra = await SimulacraRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('simulacra: %s items', len(simulacra))

    weapons = await WeaponRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('weapons: %s items', len(weapons))

    matrices = await MatricesRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('matrices: %s items', len(matrices))
    
    simulacra_v2 = await SimulacraV2Repo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('simulacra_v2: %s items', len(simulacra_v2))

    relics = await RelicRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('relics: %s items', len(relics))
    
    food = await FoodRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('food: %s items', len(food))

    items = await ItemRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('items: %s items', len(items))

    achievs = await AchievementRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('achievements: %s items', len(achievs))

    outfits =  await OutfitRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('outfits: %s items', len(outfits))
    
    mounts = await MountsRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('mounts: %s items', len(mounts))

    servants = await ServantsRepo().get_all(lang=LANGS(lang), version=VERSIONS('global'))
    _logger.info('servants: %s items', len(servants))


async def test_init():

    config_log()

    # global test
    for lang in langs:
        await test_global_data(lang=lang)


from asyncio import run 

run(test_init())