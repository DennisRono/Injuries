import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.claim import Claim
from models.base import Base, TimestampMixin


class Patient(Base, TimestampMixin):
    __tablename__ = "patients"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[str] = mapped_column(String(10))

    claims: Mapped[list["Claim"]] = relationship(back_populates="patient")
