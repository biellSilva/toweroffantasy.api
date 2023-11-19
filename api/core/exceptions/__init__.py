
from fastapi.exceptions import HTTPException


class ItemNotFound(HTTPException):
    def __init__(self, id: str, lang: str, version: str) -> None:
        super().__init__(404, f'Unable to find id **{id}** in language **{lang}** in version **{version}**')

class LanguageNotFound(HTTPException):
    def __init__(self, lang: str, version: str) -> None:
        super().__init__(404, f'Unable to find language **{lang}** in version **{version}**')

class VersionNotFound(HTTPException):
    def __init__(self, version: str) -> None:
        super().__init__(404, f'Unable to find version **{version}**')

class FileNotFound(HTTPException):
    def __init__(self, file: str, lang: str, version: str) -> None:
        super().__init__(404, f'Unable to find file **{file}** in **{version}/{lang}**')

class AssetNotFound(HTTPException):
    def __init__(self) -> None:
        super().__init__(404, 'Unable to find asset')