from pydantic import BaseModel


class AISBase(BaseModel):
    code: str
    description: str
    severity: int


class AISCreate(AISBase):
    pass


class AISResponse(AISBase):
    id: int

    class Config:
        from_attributes = True
