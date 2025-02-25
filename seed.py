import json
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import IntegrityError
from database import engine

from models import Base
from models.ais import AIS
from models.icd10 import (
    ClassificationGroup,
    Injury,
    InjuryClassification,
    InjurySubClassification,
)

Session = sessionmaker(bind=engine)
session = Session()


def seed_all_icd10_tables():
    with open("data/injuries_data.json") as f:
        icd10_json_arr = json.load(f)
        for icd in icd10_json_arr:
            try:
                new_classification_group = ClassificationGroup(
                    range_code=icd["range"],
                    description=icd["range_name"],
                )
                session.add(new_classification_group)
                session.commit()
            except IntegrityError:
                session.rollback()
                new_classification_group = (
                    session.query(ClassificationGroup)
                    .filter_by(range_code=icd["range"])
                    .first()
                )

            try:
                new_injury_classification = InjuryClassification(
                    code=icd["classsification_code"],
                    description=icd["classification_name"],
                    classification_group_id=new_classification_group.range_code,
                )
                session.add(new_injury_classification)
                session.commit()
            except IntegrityError:
                session.rollback()
                new_injury_classification = (
                    session.query(InjuryClassification)
                    .filter_by(code=icd["classsification_code"])
                    .first()
                )

            try:
                new_injury_sub_classification = InjurySubClassification(
                    code=icd["sub_classification_code"],
                    description=icd["sub_classification_name"],
                    block_id=new_injury_classification.code,
                )
                session.add(new_injury_sub_classification)
                session.commit()
            except IntegrityError:
                session.rollback()
                new_injury_sub_classification = (
                    session.query(InjurySubClassification)
                    .filter_by(code=icd["sub_classification_code"])
                    .first()
                )

            if icd["mini_classification_code"] and icd["mini_classification_name"]:
                try:
                    new_injury = Injury(
                        code=icd["sub_sub_classification_code"],
                        name=icd["sub_sub_classification_name"],
                        category_id=new_injury_sub_classification.code,
                    )
                    session.add(new_injury)
                    session.commit()
                except IntegrityError:
                    session.rollback()
                if new_injury:
                    try:
                        new_precise_injury = Injury(
                            code=icd["mini_classification_code"],
                            name=icd["mini_classification_name"],
                            parent_id=new_injury.code,
                            category_id=new_injury_sub_classification.code,
                        )
                        session.add(new_precise_injury)
                        session.commit()
                    except IntegrityError:
                        session.rollback()
            else:
                try:
                    new_injury = Injury(
                        code=icd["sub_sub_classification_code"],
                        name=icd["sub_sub_classification_name"],
                        category_id=new_injury_sub_classification.code,
                    )
                    session.add(new_injury)
                    session.commit()
                except IntegrityError:
                    session.rollback()


def seed_ais():
    with open("data/ais.json") as f:
        aiss = json.load(f)
        for ais in aiss:
            new_ais = AIS(
                ais_code=ais["ais_code"], name=ais["name"], severity=ais["severity"]
            )
            session.add(new_ais)
            session.commit()


if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    seed_all_icd10_tables()
    seed_ais()
    print("Data seeding completed successfully.")
