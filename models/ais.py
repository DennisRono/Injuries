from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base, TimestampMixin


class AIS(Base, TimestampMixin):
    __tablename__ = "ais_codes"

    ais_code: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    severity: Mapped[int] = mapped_column(Integer)
