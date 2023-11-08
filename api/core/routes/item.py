
from fastapi import APIRouter

from api.enums import ITEMS, LANGS

from api.infra.entitys import Item, EntityBase
from api.infra.repository import ItemRepo

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound


router = APIRouter(prefix="/item", tags=["item"])

ITEM_REPO = ItemRepo()

@router.get('/{id}', response_model=Item)
async def get_item(id: ITEMS, lang: LANGS = LANGS('en')):
    '''
    return \n
        Item
    '''

    if item := await ITEM_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(item.model_dump())
    
    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})

@router.get('', response_model=dict[str, Item])
async def get_all_items(lang: LANGS = LANGS('en')):
    '''
    return \n
        Dict[Item.id: Item]
    '''

    if items := await ITEM_REPO.get_all(lang):
        return PrettyJsonResponse({item.id: item.model_dump() 
                                   for item in items})
    
    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})