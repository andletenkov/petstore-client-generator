from typing import Optional

from pydantic import BaseModel, Field


class PetstoreMethodParameter(BaseModel):
    name: str
    desc: str = Field(alias='description')
    in_: str = Field(alias='in')
    required: bool
    type: str


class PetstoreMethodDetails(BaseModel):
    name: str = Field(alias='operationId')
    summary: str
    parameters: Optional[list[PetstoreMethodParameter]] = Field(default_factory=list)


class PetstoreMethod(BaseModel):
    __root__: dict[str, PetstoreMethodDetails]

    def __iter__(self):
        return iter(self.__root__.items())


class PetstorePaths(BaseModel):
    __root__: dict[str, PetstoreMethod]

    def __iter__(self):
        return iter(self.__root__.items())


class PetstoreSchema(BaseModel):
    base_path: str = Field(alias='basePath')
    host: str
    paths: PetstorePaths
