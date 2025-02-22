from pydantic import BaseModel


class ICD10Base(BaseModel):
    code: str
    description: str


class ICD10Create(ICD10Base):
    pass


class ICD10Response(ICD10Base):
    id: int

    class Config:
        from_attributes = True
