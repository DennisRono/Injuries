import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base, TimestampMixin


class Injury(Base, TimestampMixin):
    __tablename__ = "injuries"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    icd10_mini_category_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("icd10_mini_categories.id")
    )
    ais_code: Mapped[str] = mapped_column(String(10), ForeignKey("ais_codes.code"))
    description: Mapped[str] = mapped_column(String(255))
    icd10_mini_category: Mapped["ICD10MiniCategory"] = relationship(
        "ICD10MiniCategory", back_populates="injuries"
    )
    ais: Mapped["AIS"] = relationship(back_populates="injuries")
    claims: Mapped[list["Claim"]] = relationship("Claim", back_populates="injury")
