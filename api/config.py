
from pathlib import Path
from json import loads

from api.infra.entitys.banners import Banner


GLOBAL_ASSETS = 'https://raw.githubusercontent.com/FortOfFans/ToF.github.io/main'
CN_ASSETS = 'https://raw.githubusercontent.com/Silyky/Icon_CN/main' 


GB_BANNERS: list[Banner] = [Banner(**data) for data in loads(Path(f'api/infra/database/global/banners_global.json').read_bytes())]

EXTRA_ASSETS: dict[str, str | list[str]] = {
    'DPS': "icon_qianggong",
    'Tank': "icon_fangyu",
    'SUP': "icon_zengyi",

    'white': ['ElementDef', 'CommonAtkAdded', 'CritAdded', 'MaxHealthAdded'],

    'Flame': "icon_element_huo",
    'FlamePhysics': "icon_element_huowu",

    'Ice': "icon_element_bing",
    'IceThunder': "icon_element_leibing",

    'Thunder': "icon_element_lei",
    'ThunderIce': "icon_element_binglei",

    'Physics': "icon_element_wu",
    'PhysicsFlame': "icon_element_wuhuo",

    'Superpower': "icon_element_powers"
}
