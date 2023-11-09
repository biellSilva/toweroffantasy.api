
from fastapi import APIRouter

from api.enums import WEAPONS, LANGS

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound

from api.infra.entitys import Weapon, EntityBase
from api.infra.repository import WeaponRepo


router = APIRouter(prefix='/weapons', tags=['weapons'])

WEAPON_REPO = WeaponRepo()


@router.get('/{id}', name='Get weapon', response_model=Weapon)
async def get_weapon(id: WEAPONS, lang: LANGS = LANGS('en'), exclude: bool = True):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
        exclude: 
            type: bool
            default: True
            desc: removes some keys

    **Return** \n
        List[Weapon]
    '''

    if weapon := await WEAPON_REPO.get(EntityBase(id=id), lang):
        if exclude:
            return PrettyJsonResponse(weapon.model_dump(exclude={'skills', 'mats', 
                                                                 'advancements', 'advanceID',
                                                                 'shatter', 'charge'}))

        else:
            return PrettyJsonResponse(weapon.model_dump())

    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})


@router.get(path='', name='All Weapons', response_model=list[Weapon])
async def get_all_weapons(lang: LANGS = LANGS('en'), exclude: bool = True):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
        exclude: 
            type: bool
            default: True
            desc: removes some keys
    
    **Return** \n
        List[Weapon]
    '''


    if weapons := await WEAPON_REPO.get_all(lang):
        if exclude:
            return PrettyJsonResponse([weapon.model_dump(exclude={'skills', 'mats', 
                                                                  'advancements', 'advanceID',
                                                                  'shatter', 'charge', 'weaponEffects'}) 
                                        for weapon in weapons])

        else:
            return PrettyJsonResponse([weapon.model_dump() 
                                        for weapon in weapons])

    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})