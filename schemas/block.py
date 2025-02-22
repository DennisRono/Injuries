from pydantic import BaseModel


class BlockBase(BaseModel):
    code: str
    description: str


class ICD10BlockCreate(BlockBase):
    pass


class ICD10BlockResponse(BlockBase):
    id: int

    class Config:
        from_attributes = True
