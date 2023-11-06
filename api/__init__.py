
from fastapi import Header
from fastapi.exceptions import HTTPException

from api.config import API_KEY


def verify_auth(auth: str = Header(...)):
    if auth == API_KEY:
        return True
    else:
        raise HTTPException(status_code=401, detail='Wrong API TOKEN')