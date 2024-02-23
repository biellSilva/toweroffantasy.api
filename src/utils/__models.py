from pydantic import BaseModel


class License(BaseModel):
    text: str


class Project(BaseModel):
    name: str
    version: str
    description: str
    license: License


class PyProject(BaseModel):
    project: Project
