
from pathlib import Path
from os import listdir
from json import loads
from fastapi import APIRouter, HTTPException

from api.enums import SIMULACRAS, Lang
from api.entitys import Simulacra


router = APIRouter(prefix='/simulacra', tags=['simulacra'])


@router.get('/{name}', response_model_exclude_none=True)
async def get_simulacra(name: SIMULACRAS, lang: Lang = Lang.en):
    ''' Get simulacra based on name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/simulacra/{name.replace(" ", "_").lower()}.json')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/simulacra/{name.replace(" ", "_").lower()}.json')

    if not path.is_file():
        raise HTTPException(404, f'/simulacra/{name.replace(" ", "_").lower()} not found')
    
    else:
        with open(path, 'rb') as f:
            return Simulacra(**loads(f.read()))