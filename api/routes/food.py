
from fastapi import APIRouter

from api.enums import FOOD, LANGS

from api.infra.entitys import Food, EntityBase
from api.infra.repository import FoodRepo

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound


router = APIRouter(prefix="/food", tags=["Food"])

FOOD_REPO = FoodRepo()

@router.get('/{id}', name='Get food', response_model=Food)
async def get_food(id: FOOD, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: food_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: True
            desc: Include all data keys
            
    return \n
        Food
    '''

    if food := await FOOD_REPO.get(EntityBase(id=id), lang):
        if include:
            return PrettyJsonResponse(food.model_dump())
        else:
            return PrettyJsonResponse(food.model_dump(include={'id', 'name', 'icon', 'quality', 'stars'}))
    
    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})


@router.get('', name='All foods', response_model=list[Food])
async def get_all_foods(lang: LANGS = LANGS('en'), include: bool = False):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: False
            desc: Include all data keys

            
    return \n
        List[Food]
    '''

    if foods := await FOOD_REPO.get_all(lang):
        if include:
            return PrettyJsonResponse([food.model_dump() for food in foods])
        else:
            return PrettyJsonResponse([food.model_dump(include={'id', 'name', 'icon', 'quality', 'stars'}) for food in foods])
    
    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})