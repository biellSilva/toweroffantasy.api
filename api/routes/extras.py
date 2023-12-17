
from fastapi import APIRouter, Path as ApiPath
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.exceptions import HTTPException

from pathlib import Path
from json import loads

from api.config import GB_BANNERS, EXTRA_ASSETS, CN_ASSETS

from api.infra.entitys import Raritys
from api.infra.entitys.banners import Banner


RARITYS_DATA: dict[str, dict[str, dict[str, str]]] = loads(Path('api/infra/database/rarity.json').read_bytes())
RARITY_DATA_RE = {rarity_key: value_asset
                for rarity_key, rarity_value in RARITYS_DATA.items() 
                for _, value_asset in rarity_value.items()}

RARITY_MODEL = Raritys(**RARITY_DATA_RE) # type: ignore


router = APIRouter(prefix='/extras', tags=['Extras'])
METADATA = {
    'name': 'Extras',
    'description': 'Simple route to get extra data/assets',
    }


@router.get('/rarities', name='Get rarity', response_model=Raritys)
async def get_rarity():
    '''  
    **Return** \n
        Rarity
    '''
    return RARITY_MODEL


@router.get('/banners', name='Banners', response_model=list[Banner])
async def get_banners():
    '''  
    **Return** \n
        list[Banner]
    '''
    return GB_BANNERS

@router.get('/assets/{id}', name='Extra Assets')
async def get_extra_asset(id: str = ApiPath(description='Asset ID')):

    '''
    Route to serve assets from weapon element, category and base stats\n
    Element Ref, CommonAtkAdded, CritAdded and MaxHealthAdded are in the white version of it
    '''

    if id in EXTRA_ASSETS:
        return RedirectResponse(url=f'{CN_ASSETS}/UI/wuqi/{EXTRA_ASSETS[id]}.png')
    
    if id in EXTRA_ASSETS['white']:
        return FileResponse(f'api/assets/white/{id}.webp', media_type='image/WEBP')
    
    raise HTTPException(status_code=404, detail='Asset not found')
        
