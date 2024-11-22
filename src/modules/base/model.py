from pydantic import BaseModel


class BackgroundColor(BaseModel):
    r: float
    g: float
    b: float
    a: float
    hex: str
