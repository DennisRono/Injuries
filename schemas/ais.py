from pydantic import BaseModel, ConfigDict, UUID4


class AISBase(BaseModel):
    code: str
    description: str
    severity: int


class AISCreate(AISBase):
    pass


class AISResponse(AISBase):
    id: UUID4

    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
