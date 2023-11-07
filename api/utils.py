
import re

from fastapi import Header
from fastapi.exceptions import HTTPException

from api.config import API_KEY


def bold_numbers(text: str):
    return re.sub(r'\d+(.\d+)?%?', lambda x: f'**{x.group(0)}**' 
                  if text[x.span(0)[0]-1] != '*' else x.group(0), 
                  text.replace('<shuzhi>', '').replace('</>', ''), flags=re.IGNORECASE)

def replace_cv(text: str):
    return text.replace('CV : ', '')


def verify_auth(auth: str = Header(...)):
    if auth == API_KEY:
        return True
    else:
        raise HTTPException(status_code=401, detail='Wrong API TOKEN')