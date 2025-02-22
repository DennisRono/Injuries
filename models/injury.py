import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.ais import AIS
from models.icd10 import ICD10
from models.base import Base, TimestampMixin


class Injury(Base, TimestampMixin):
    __tablename__ = "injuries"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    icd10_code: Mapped[str] = mapped_column(ForeignKey("icd10_codes.code"))
    ais_code: Mapped[str] = mapped_column(ForeignKey("ais_codes.code"))
    description: Mapped[str] = mapped_column(String(255))

    icd10: Mapped["ICD10"] = relationship()
    ais: Mapped["AIS"] = relationship()
