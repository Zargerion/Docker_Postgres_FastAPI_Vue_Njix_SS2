import pydantic as _pydandic

class _Creations(_pydandic.BaseModel):
    type: str
    description: str
    image: str  
    link: str
    is_published: bool

class Creation(_Creations):
    id: int
    class Config:
        orm_mode = True

class CreateCreation(_Creations):
    pass
