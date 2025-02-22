import uuid
from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base, TimestampMixin


class Claim(Base, TimestampMixin):
    __tablename__ = "claims"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    patient_id: Mapped[str] = mapped_column(String(36), ForeignKey("patients.id"))
    injury_id: Mapped[str] = mapped_column(String(36), ForeignKey("injuries.id"))
    status: Mapped[str] = mapped_column(String(20))
    compensation_amount: Mapped[float] = mapped_column(Float)
    patient: Mapped["Patient"] = relationship("Patient", back_populates="claims")
    injury: Mapped["Injury"] = relationship("Injury", back_populates="claims")
