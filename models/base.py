from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    date_created: Mapped[datetime] = mapped_column(default=func.now())  # date_created
