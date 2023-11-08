
from fastapi import APIRouter

from api.enums import FOOD, LANGS

from api.infra.entitys import Food, EntityBase
from api.infra.repository import FoodRepo

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound


router = APIRouter(prefix="/food", tags=["food"])

FOOD_REPO = FoodRepo()

@router.get('/{id}', response_model=Food)
async def get_food(id: FOOD, lang: LANGS = LANGS('en')):
    '''
    return \n
        Food
    '''

    if food := await FOOD_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(food.model_dump())
    
    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})

@router.get('', response_model=dict[str, Food])
async def get_all_foods(lang: LANGS = LANGS('en')):
    '''
    return \n
        Dict[Food.id: Food]
    '''

    if foods := await FOOD_REPO.get_all(lang):
        return PrettyJsonResponse({food.id: food.model_dump() 
                                   for food in foods})
    
    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})