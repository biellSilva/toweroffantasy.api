
from fastapi import APIRouter

from pathlib import Path
from json import loads

from api.config import GB_BANNERS

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