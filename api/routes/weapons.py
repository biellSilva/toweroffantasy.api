
from fastapi import APIRouter

from api.enums import WEAPONS, LANGS

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound

from api.infra.entitys import Weapon, EntityBase
from api.infra.repository import WeaponRepo


router = APIRouter(prefix='/weapons', tags=['Weapons'])

WEAPON_REPO = WeaponRepo()


@router.get('/{id}', name='Get weapon', response_model=Weapon)
async def get_weapon(id: WEAPONS, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: weapon_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
        include: 
            type: bool
            default: True
            desc: Include all data keys

    **Return** \n
        Weapon
    '''

    if weapon := await WEAPON_REPO.get(EntityBase(id=id), lang):
        if include:
            return PrettyJsonResponse(weapon.model_dump())

        else:
            return PrettyJsonResponse(weapon.model_dump(include={'name', 'id', 'assets', 'type', 'rarity', 'element'}))

    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})


@router.get(path='', name='All Weapons', response_model=list[Weapon])
async def get_all_weapons(lang: LANGS = LANGS('en'), include: bool = False):
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
    
    **Return** \n
        List[Weapon]
    '''


    if weapons := await WEAPON_REPO.get_all(lang):
        if include:
            return PrettyJsonResponse([weapon.model_dump() for weapon in weapons])

        else:
            return PrettyJsonResponse([weapon.model_dump(include={'name', 'id', 'assets', 'type', 'rarity', 'element'}) for weapon in weapons])

    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})