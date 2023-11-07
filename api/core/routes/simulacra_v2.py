
from pathlib import Path
from os import listdir
from json import loads
from fastapi import APIRouter, HTTPException

from api.entitys import Simulacra_v2
from api.enums import SIMULACRAS_V2, Lang


router = APIRouter(prefix='/simulacra/v2', tags=['simulacra_v2'])


@router.get('/{name}', response_model_exclude_none=True)
async def get_simulacra(name: SIMULACRAS_V2, lang: Lang = Lang.en):
    ''' Get simulacra based on name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/simulacra_v2/{name.replace(" ", "_").lower()}.json')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/simulacra_v2/{name.replace(" ", "_").lower()}.json')

    if not path.is_file():
        raise HTTPException(404, f'/simulacra/v2/{name.replace(" ", "_").lower()} not found')
    
    else:
        with open(path, 'rb') as f:
            return Simulacra_v2(**loads(f.read()))
