import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base, TimestampMixin
from typing import List, Optional


class ICD10(Base, TimestampMixin):
    __tablename__ = "icd10_codes"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))


class InjurySubcategory(Base, TimestampMixin):
    __tablename__ = "injury_subcategories"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    code: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[str] = mapped_column()
    category_id: Mapped[str] = mapped_column(ForeignKey("injury_categories.id"))

    parent_category: Mapped["ICD10"] = relationship(back_populates="subcategories")
    details: Mapped[List["InjuryDetail"]] = relationship(
        back_populates="parent_subcategory", cascade="all, delete"
    )


class InjuryDetail(Base, TimestampMixin):
    __tablename__ = "injury_details"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    code: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[str] = mapped_column()
    subcategory_id: Mapped[str] = mapped_column(ForeignKey("injury_subcategories.id"))
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()

    parent_subcategory: Mapped["InjurySubcategory"] = relationship(
        back_populates="details"
    )
    severity: Mapped[List["InjurySeverity"]] = relationship(
        back_populates="parent_injury", cascade="all, delete"
    )


class InjurySeverity(Base, TimestampMixin):
    __tablename__ = "injury_severity"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    injury_id: Mapped[str] = mapped_column(ForeignKey("injury_details.id"))
    severity_score: Mapped[int] = mapped_column(index=True)
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()
    notes: Mapped[Optional[str]] = mapped_column()

    parent_injury: Mapped["InjuryDetail"] = relationship(back_populates="severity")
