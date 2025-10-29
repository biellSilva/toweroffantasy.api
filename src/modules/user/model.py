from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    username: str
    email: str
    is_active: bool
