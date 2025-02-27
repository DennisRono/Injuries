from typing import Optional
from pydantic import BaseModel, ConfigDict


class AISBase(BaseModel):
    ais_code: str
    name: str
    description: Optional[str] = None
    severity: int


class AISCreate(AISBase):
    pass


class AISResponse(AISBase):
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
