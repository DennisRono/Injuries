import uuid
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base, TimestampMixin


class AIS(Base, TimestampMixin):
    __tablename__ = "ais_codes"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    severity: Mapped[int] = mapped_column(Integer)
