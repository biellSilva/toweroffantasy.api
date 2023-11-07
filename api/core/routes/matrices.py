
from pathlib import Path
from os import listdir
from json import loads
from fastapi import APIRouter, HTTPException

from api.enums import MATRICES, Lang
from api.entitys import Matrice


router = APIRouter(prefix='/matrices', tags=['matrices'])


@router.get('/{name}', response_model_exclude_none=True)
async def get_matrice(name: MATRICES, lang: Lang = Lang.en):
    ''' Get matrice based on name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/matrices/{name.replace(" ", "_").lower()}.json')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/matrices/{name.replace(" ", "_").lower()}.json')

    if not path.is_file():
        raise HTTPException(404, f'/{lang}/matrices/{name.replace(" ", "_").lower()} not found')
    
    else:
        with open(path, 'rb') as f:
            return Matrice(**loads(f.read()))

