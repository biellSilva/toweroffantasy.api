
from pathlib import Path
from os import listdir
from json import loads
from fastapi import APIRouter, HTTPException

from api.enums import WEAPONS, Lang
from api.entitys import Weapon


router = APIRouter(prefix='/weapons', tags=['weapons'])


@router.get('/{name}', response_model_exclude_none=True)
async def get_weapon(name: WEAPONS, lang: Lang = Lang.en):
    ''' Get weapon based on name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/weapons/{name.replace(" ", "_").lower()}.json')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/weapons/{name.replace(" ", "_").lower()}.json')

    if not path.is_file():
        raise HTTPException(404, f'/{lang}/weapons/{name.replace(" ", "_").lower()} not found')
    
    else:
        with open(path, 'rb') as f:
            return Weapon(**loads(f.read()))