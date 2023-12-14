
from pathlib import Path
from json import loads

from api.infra.entitys.banners import Banner


GLOBAL_ASSETS = 'https://raw.githubusercontent.com/FortOfFans/ToF.github.io/main'
CN_ASSETS = 'https://raw.githubusercontent.com/Silyky/Icon_CN/main'


GB_BANNERS: list[Banner] = [Banner(**data) for data in loads(Path(f'api/infra/database/global/banners_global.json').read_bytes())]


