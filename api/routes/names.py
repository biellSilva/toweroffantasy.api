
from pathlib import Path
from os import listdir
from fastapi import APIRouter

from api.enums import Lang
from api.response import JsonIndentResponse


router = APIRouter(prefix='/names', tags=['names'])


@router.get('/simulacra')
async def get_simulacra_names(lang: Lang = Lang.en):
    ''' Returns a list of simulacra's name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/simulacra')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/simulacra')

    return JsonIndentResponse(content={'names': [file.name.removesuffix('.json') for file in path.iterdir()]}, status_code=200)


@router.get('/simulacra/v2')
async def get_simulacra_v2_names(lang: Lang = Lang.en):
    ''' Returns a list of simulacra's name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/simulacra_new')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/simulacra_new')

    return JsonIndentResponse(content={'names': [file.name.removesuffix('.json') for file in path.iterdir()]}, status_code=200)

@router.get('/weapons')
async def get_weapons_names(lang: Lang = Lang.en):
    ''' Returns a list of weapons's name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/weapons')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/weapons')

    return JsonIndentResponse(content={'names': [file.name.removesuffix('.json') for file in path.iterdir()]}, status_code=200)

@router.get('/matrices')
async def get_matrices_names(lang: Lang = Lang.en):
    ''' Returns a list of matrices's name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/matrices')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/matrices')

    return JsonIndentResponse(content={'names': [file.name.removesuffix('.json') for file in path.iterdir()]}, status_code=200)

@router.get('/relics')
async def get_relics_names(lang: Lang = Lang.en):
    ''' Returns a list of relics's name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang}/relics')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/relics')

    return JsonIndentResponse(content={'names': [file.name.removesuffix('.json') for file in path.iterdir()]}, status_code=200)