from typing import Optional
from pydantic import BaseModel, ConfigDict


class ClassificationGroupBase(BaseModel):
    range_code: str
    name: str
    description: Optional[str] = None


class ClassificationGroupCreate(ClassificationGroupBase):
    pass


class ClassificationGroupResponse(ClassificationGroupBase):
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
