
from pathlib import Path
from os import listdir
from json import loads
from fastapi import APIRouter, HTTPException

from api.enums import RELICS, Lang
from api.entitys import Relic


router = APIRouter(prefix='/relics', tags=['relics'])


@router.get('/{name}', response_model_exclude_none=True)
async def get_relic(name: RELICS, lang: Lang = Lang.en):
    ''' Get relic based on name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/relics/{name.replace(" ", "_").lower()}.json')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/relics/{name.replace(" ", "_").lower()}.json')

    if not path.is_file():
        raise HTTPException(404, f'/{lang}/relics/{name.replace(" ", "_").lower()} not found')
    
    else:
        with open(path, 'rb') as f:
            return Relic(**loads(f.read()))

