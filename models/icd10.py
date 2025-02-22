import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base, TimestampMixin
from typing import List


class ICD10Chapter(Base, TimestampMixin):
    __tablename__ = "icd10_chapters"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    range_code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    blocks: Mapped[List["ICD10Block"]] = relationship(
        "ICD10Block", back_populates="chapter"
    )


class ICD10Block(Base, TimestampMixin):
    __tablename__ = "icd10_blocks"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    chapter_id: Mapped[str] = mapped_column(String(36), ForeignKey("icd10_chapters.id"))

    chapter: Mapped["ICD10Chapter"] = relationship(back_populates="blocks")
    categories: Mapped[List["ICD10Category"]] = relationship(
        "ICD10Category", back_populates="block"
    )


class ICD10Category(Base, TimestampMixin):
    __tablename__ = "icd10_categories"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    block_id: Mapped[str] = mapped_column(String(36), ForeignKey("icd10_blocks.id"))

    block: Mapped["ICD10Block"] = relationship(back_populates="categories")
    subcategories: Mapped[List["ICD10Subcategory"]] = relationship(
        "ICD10Subcategory", back_populates="category"
    )


class ICD10Subcategory(Base, TimestampMixin):
    __tablename__ = "icd10_subcategories"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("icd10_categories.id")
    )

    category: Mapped["ICD10Category"] = relationship(back_populates="subcategories")
    mini_categories: Mapped[List["ICD10MiniCategory"]] = relationship(
        "ICD10MiniCategory", back_populates="subcategory"
    )


class ICD10MiniCategory(Base, TimestampMixin):
    __tablename__ = "icd10_mini_categories"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    subcategory_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("icd10_subcategories.id")
    )

    subcategory: Mapped["ICD10Subcategory"] = relationship(
        back_populates="mini_categories"
    )
    injuries: Mapped[list["Injury"]] = relationship(
        "Injury", back_populates="icd10_mini_category"
    )
