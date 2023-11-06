from pydantic import BaseModel


class Language(BaseModel):
    lang: str = 'en-US'