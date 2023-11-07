
from pathlib import Path
from os import listdir
from json import dump, loads
from fastapi import APIRouter, HTTPException, Depends

from api import verify_auth
from api.entitys import Simulacra
from api.enums import SIMULACRAS, Lang
from api.response import JsonIndentResponse


router = APIRouter(prefix='/simulacra', tags=['simulacra'])


@router.get('/{name}', response_model_by_alias=False)
async def get_simulacra(name: SIMULACRAS, lang: Lang = Lang.en):
    ''' Get simulacra based on name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang.value}/simulacra/{name.replace(" ", "_").lower()}.json')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/simulacra/{name.replace(" ", "_").lower()}.json')

    if not path.is_file():
        raise HTTPException(404, f'/simulacra/{name.replace(" ", "_").lower()} not found')
    
    else:
        with open(path, 'rb') as f:
            return JsonIndentResponse(content=loads(f.read()), status_code=200, headers={"Content-Disposition": "inline"})


@router.post('', dependencies=[Depends(verify_auth)], response_model_by_alias=False)
async def create_simulacra(simulacra: Simulacra, lang: Lang = Lang.en):

    if Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').exists():
        raise HTTPException(403, f'/simulacra/{lang}/{simulacra.name.replace(" ", "_").lower()} already exists')
    
    Path(Path().cwd(), f'src/data/{lang}/simulacra').mkdir(parents=True, exist_ok=True)

    with open(f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json', 'w') as f:
        dump(simulacra.model_dump(), f, ensure_ascii=False, indent=4)

    return f'/simulacra/{simulacra.name.replace(" ", "_").lower()} created'


@router.put('', dependencies=[Depends(verify_auth)])
async def update_simulacra(simulacra: Simulacra, lang: Lang = Lang.en):
    
    if not Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').exists():
        raise HTTPException(404, f'/simulacra/{simulacra.name.replace(" ", "_").lower()} not found')

    with open(f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json', 'w') as f:
        dump(simulacra.model_dump(), f, ensure_ascii=False, indent=4)
    
    return f'/simulacras/{simulacra.name.replace(" ", "_").lower()} updated'


@router.delete('', dependencies=[Depends(verify_auth)])
async def delete_simulacra(simulacra: Simulacra, lang: Lang = Lang.en):
     
    if not Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').exists():
        raise HTTPException(404, f'/simulacra/{simulacra.name.replace(" ", "_").lower()} not found')

    Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').unlink(missing_ok=True)
    
    return f'/simulacras/{simulacra.name.replace(" ", "_").lower()} deleted'