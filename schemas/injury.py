from typing import Optional
from pydantic import BaseModel, ConfigDict

from schemas.injury_sub_classification import InjurySubClassificationResponse


class InjuryBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    category_id: str
    parent_id: Optional[str] = None


class InjuryCreate(InjuryBase):
    pass


class InjuryResponse(InjuryBase):
    injury_sub_classification: InjurySubClassificationResponse = None
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
