from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base, TimestampMixin
from typing import List


class ClassificationGroup(Base, TimestampMixin):
    __tablename__ = "classification_groups"

    range_code: Mapped[str] = mapped_column(String(50), primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    injury_classifications: Mapped[List["InjuryClassification"]] = relationship(
        "InjuryClassification", back_populates="classification_group"
    )


class InjuryClassification(Base, TimestampMixin):
    __tablename__ = "injury_classifications"

    code: Mapped[str] = mapped_column(String(50), primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    classification_group_id: Mapped[str] = mapped_column(
        String(50), ForeignKey("classification_groups.range_code")
    )
    classification_group: Mapped["ClassificationGroup"] = relationship(
        "ClassificationGroup", back_populates="injury_classifications"
    )
    injury_sub_classifications: Mapped[List["InjurySubClassification"]] = relationship(
        "InjurySubClassification", back_populates="injury_classification"
    )


class InjurySubClassification(Base, TimestampMixin):
    __tablename__ = "injury_sub_classifications"

    code: Mapped[str] = mapped_column(String(50), primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    block_id: Mapped[str] = mapped_column(
        String(50), ForeignKey("injury_classifications.code")
    )

    injury_classification: Mapped["InjuryClassification"] = relationship(
        "InjuryClassification", back_populates="injury_sub_classifications"
    )
    subcategories: Mapped[List["Injury"]] = relationship(
        "Injury", back_populates="category"
    )


class Injury(Base, TimestampMixin):
    __tablename__ = "injuries"

    code: Mapped[str] = mapped_column(String(50), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    category_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("injury_sub_classifications.code")
    )
    parent_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("injuries.code"), nullable=True
    )

    category: Mapped["InjurySubClassification"] = relationship(
        "InjurySubClassification", back_populates="subcategories"
    )
    parent: Mapped["Injury"] = relationship("Injury", remote_side=[code])
