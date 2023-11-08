
import re

from fastapi import Header
from fastapi.exceptions import HTTPException

from api.config import API_KEY


def bold_numbers(text: str):
    return re.sub(r'\d+(.\d+)?%?', lambda x: f'**{x.group(0)}**' 
                  if text[x.span(0)[0]-1] not in ('*', '+', '-') or text[x.span(0)[1]] not in ('*', '+', '-') else x.group(0), 
                  text.replace('<shuzhi>', '').replace('</>', ''), flags=re.IGNORECASE)

def replace_cv(text: str):
    return text.replace('CV : ', '')

def replace_icon(text: str):
    if '/Game/Resources/' in text:
        return text.replace('/Game/Resources', '/assets')
    else:
        return text

def verify_auth(auth: str = Header(...)):
    if auth == API_KEY:
        return True
    else:
        raise HTTPException(status_code=401, detail='Wrong API TOKEN')
    

def classifier(number: float):
    if number >= 15:
        return 'SS'
    elif number >= 10.01:
        return 'S'
    elif number >= 8:
        return 'A'
    elif number >= 4:
        return 'B'
    else:
        return 'C'