import uuid
from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin


class Claim(Base, TimestampMixin):
    __tablename__ = "claims"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    injury_id: Mapped[int] = mapped_column(ForeignKey("injuries.id"))
    status: Mapped[str] = mapped_column(String(20))
    compensation_amount: Mapped[float] = mapped_column(Float)

    patient: Mapped["Patient"] = relationship(back_populates="claims")
    injury: Mapped["Injury"] = relationship()
