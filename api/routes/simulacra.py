
import aiofiles

from pathlib import Path
from os import listdir
from json import loads, dump
from fastapi import APIRouter, HTTPException, Depends, UploadFile
from fastapi.responses import JSONResponse
from typing import Optional, Literal

from api import verify_auth
from api.entitys import Simulacra
from api.response import JsonIndentResponse


router = APIRouter(prefix='/simulacra', tags=['simulacra'])


@router.get('/{name}')
async def get_simulacra(name: str, lang: Lang = Lang.en):
    ''' Get simulacra based on name '''
    
    if lang.value in listdir('src/data'):
        path = Path(Path().cwd(), f'src/data/{lang.value}/simulacra/{name.replace(" ", "").lower()}.json')

    else:
        path = Path(Path().cwd(), f'src/data/en-US/simulacra/{name.replace(" ", "").lower()}.json')

    if not path.is_file():
        raise HTTPException(404, f'/simulacra/{name.replace(" ", "").lower()} not found')
    
    else:
        with open(path, 'rb') as f:
            return JsonIndentResponse(content=loads(f.read()), status_code=200, headers={"Content-Disposition": "inline"})


@router.post('', dependencies=[Depends(verify_auth)])
async def create_simulacra(simulacra: Simulacra, file_A0: UploadFile, lang: Literal['en-US', 'pt-BR'] = 'en-US', file_A3: Optional[UploadFile] = None):

    if Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').exists():
        raise HTTPException(403, f'/simulacra/{lang}/{simulacra.name.replace(" ", "_").lower()} already exists')
    
    Path(Path().cwd(), f'src/data/{lang}/simulacra').mkdir(parents=True, exist_ok=True)
    Path(Path().cwd(), f'src/images/simulacra').mkdir(parents=True, exist_ok=True)

    with open(f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json', 'w') as f:
        dump(simulacra.model_dump(), f, ensure_ascii=False, indent=4)

    async with aiofiles.open(f'src/images/simulacra/{simulacra.name.replace(" ", "_").lower()}.webp', 'wb') as f:
        image = await file_A0.read()
        await f.write(image)
    
    if file_A3:
        async with aiofiles.open(f'src/images/simulacra/{simulacra.name.replace(" ", "_").lower()}_A3.webp', 'wb') as f:
            image = await file_A3.read()
            await f.write(image)
    
    return f'/simulacra/{simulacra.name.replace(" ", "_").lower()} created'


@router.put('', dependencies=[Depends(verify_auth)])
async def update_simulacra(simulacra: Simulacra, lang: Literal['en-US', 'pt-BR'] = 'en-US', file_A0: Optional[UploadFile] = None, file_A3: Optional[UploadFile] = None):
    
    if not Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').exists():
        raise HTTPException(404, f'/simulacra/{simulacra.name.replace(" ", "_").lower()} not found')

    with open(f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json', 'w') as f:
        dump(simulacra.model_dump(), f, ensure_ascii=False, indent=4)
    
    if file_A0:
        async with aiofiles.open(f'src/images/simulacra/{simulacra.name.replace(" ", "_").lower()}_A0.webp', 'wb') as f:
            image = await file_A0.read()
            await f.write(image)

    if file_A3:
        async with aiofiles.open(f'src/images/simulacra/{simulacra.name.replace(" ", "_").lower()}_A3.webp', 'wb') as f:
            image = await file_A3.read()
            await f.write(image)
    
    return f'/simulacras/{simulacra.name.replace(" ", "_").lower()} updated'


@router.delete('', dependencies=[Depends(verify_auth)])
async def delete_simulacra(simulacra: Simulacra, lang: Literal['en-US', 'pt-BR'] = 'en-US'):
     
        if not Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').exists():
            raise HTTPException(404, f'/simulacra/{simulacra.name.replace(" ", "_").lower()} not found')

        Path(Path().cwd(), f'src/data/{lang}/simulacra/{simulacra.name.replace(" ", "_").lower()}.json').unlink(missing_ok=True)
        
        return f'/simulacras/{simulacra.name.replace(" ", "_").lower()} deleted'