echo "Digite o nome da classe:"
read classname

echo "Digite o nome da Pasta:"
read foldername

to_camel_case() {
    s="$1"
    s=$(echo "$s" | tr '[:upper:]' '[:lower:]' | sed -r 's/(^|_)(.)/\U\2/g')
    echo "$s"
}

create_path() {
    path="$1"
    if [ ! -d "$path" ]; then
        mkdir -p "$path"
    fi
}

classname=$(echo "$classname" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
foldername=$(echo "$foldername" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

camel_classname=$(to_camel_case "$classname")
camel_foldername=$(to_camel_case "$foldername")

classname_python="${camel_classname}${camel_foldername}"

create_path "src/domain/usecases/$foldername"
create_path "src/data/usecases/$foldername"
create_path "src/presentation/controller/${foldername}"
create_path "src/main/factories/controller/${foldername}"
create_path "src/main/factories/usecases/${foldername}"

echo >> "src/domain/usecases/$foldername/${classname}.py" "
from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.usecases.base import IUsecase


class ${classname_python}Params(BaseModel):
    ...


class ${classname_python}Result(BaseModel):
    ...


class I${classname_python}UseCase(IUsecase[${classname_python}Params, ${classname_python}Result], ABC):
    @abstractmethod
    async def execute(self, params: ${classname_python}Params) -> ${classname_python}Result: ...

"



echo >> "src/data/usecases/$foldername/${classname}.py" "
from src.domain.usecases.$foldername.${classname} import ${classname_python}Params, ${classname_python}Result, I${classname_python}UseCase


class ${classname_python}UseCase(I${classname_python}UseCase):
    async def execute(self, params: ${classname_python}Params) -> ${classname_python}Result:
        ...

"


echo >> "src/presentation/controller/$foldername/${classname}.py" "
from src.domain.usecases.$foldername.${classname} import ${classname_python}Params, ${classname_python}Result, I${classname_python}UseCase


class ${classname_python}Controller:
    def __init__(self, usecase: I${classname_python}UseCase):
        self.usecase = usecase

    async def handle(self, params: ${classname_python}Params) -> ${classname_python}Result:
        return await self.usecase.execute(params)

"


echo >> "src/main/factories/usecases/${foldername}/${classname}.py" "
from src.data.usecases.$foldername.${classname} import ${classname_python}UseCase


class ${classname_python}UsecaseFactory:

    @staticmethod
    def create() -> ${classname_python}UseCase:
        return ${classname_python}UseCase(

        )
"

echo >> "src/main/factories/controller/${foldername}/${classname}.py" "
from src.presentation.controller.$foldername.${classname} import ${classname_python}Controller
from src.main.factories.usecases.$foldername.${classname} import ${classname_python}UsecaseFactory

class ${classname_python}ControllerFactory:

    @staticmethod
    def create() -> ${classname_python}Controller:
        return ${classname_python}Controller(
            ${classname_python}UsecaseFactory.create()
        )

"
