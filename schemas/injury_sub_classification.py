from typing import Optional
from pydantic import BaseModel, ConfigDict

from schemas.injury_classification import InjuryClassificationResponse


class InjurySubClassificationBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    injury_classification_id: str


class InjurySubClassificationCreate(InjurySubClassificationBase):
    pass


class InjurySubClassificationResponse(InjurySubClassificationBase):
    injury_classification: InjuryClassificationResponse = None
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
