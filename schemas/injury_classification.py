from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from schemas.classification_group import ClassificationGroupResponse


class InjuryClassificationBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    classification_group_id: str


class InjuryClassificationCreate(InjuryClassificationBase):
    pass


class InjuryClassificationResponse(InjuryClassificationBase):
    classification_group: ClassificationGroupResponse = None
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
