from pydantic import BaseModel


class InjuryBase(BaseModel):
    icd10_code: str
    ais_code: str
    description: str


class InjuryCreate(InjuryBase):
    pass


class InjuryResponse(InjuryBase):
    id: int

    class Config:
        from_attributes = True
