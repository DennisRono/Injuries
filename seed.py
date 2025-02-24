import json
import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session, sessionmaker
from database import engine
from models.base import Base
from models.icd10 import (
    ICD10Chapter,
    ICD10Block,
    ICD10Category,
    ICD10Subcategory,
    ICD10MiniCategory,
)
from models.ais import AIS
from models.injury import Injury
from models.patient import Patient
from models.claim import Claim

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def generate_uuid():
    return str(uuid.uuid4())


def seed_icd10_chapters():
    chapters = [
        {"range": "S00-S09", "description": "Injuries to the head"},
        {"range": "S10-S19", "description": "Injuries to the neck"},
        {"range": "S20-S29", "description": "Injuries to the thorax"},
        {
            "range": "S30-S39",
            "description": "Injuries to the abdomen, lower back, lumbar spine, pelvis and external genitals",
        },
        {"range": "S40-S49", "description": "Injuries to the shoulder and upper arm"},
        {"range": "S50-S59", "description": "Injuries to the elbow and forearm"},
        {"range": "S60-S69", "description": "Injuries to the wrist, hand and fingers"},
        {"range": "S70-S79", "description": "Injuries to the hip and thigh"},
        {"range": "S80-S89", "description": "Injuries to the knee and lower leg"},
        {"range": "S90-S99", "description": "Injuries to the ankle and foot"},
    ]

    for chapter in chapters:
        new_chapter = ICD10Chapter(
            id=generate_uuid(),
            range_code=chapter["range"],
            description=chapter["description"],
        )
        session.add(new_chapter)
    session.commit()


def seed_icd10_blocks():
    blocks = [
        {"code": "S00", "description": "Superficial injury of head"},
        {"code": "S01", "description": "Open wound of head"},
        {"code": "S02", "description": "Fracture of skull and facial bones"},
        {
            "code": "S03",
            "description": "Dislocation and sprain of joints and ligaments of head",
        },
        {"code": "S04", "description": "Injury of cranial nerves"},
    ]

    chapter = (
        session.query(ICD10Chapter).filter(ICD10Chapter.range_code == "S00-S09").first()
    )

    for block in blocks:
        new_block = ICD10Block(
            id=generate_uuid(),
            code=block["code"],
            description=block["description"],
            chapter_id=chapter.id,
        )
        session.add(new_block)
    session.commit()


def seed_icd10_categories():
    with open("data/one_decimal_icd10.json") as f:
        categories = json.load(f)

        for category in categories:
            block = (
                session.query(ICD10Block)
                .filter(ICD10Block.code == category["block_code"])
                .first()
            )
            existing_category = (
                session.query(ICD10Category)
                .filter(ICD10Category.code == category["code"])
                .first()
            )
            if existing_category is None and block is not None:
                new_category = ICD10Category(
                    id=generate_uuid(),
                    code=category["code"],
                    description=category["description"],
                    block_id=block.id,
                )
                session.add(new_category)
            session.add(new_category)
        session.commit()


def seed_icd10_subcategories():
    subcategories = [
        {
            "code": "S00.01",
            "description": "Abrasion of scalp",
            "category_code": "S00.0",
        },
        {
            "code": "S00.11",
            "description": "Contusion of eyelid",
            "category_code": "S00.1",
        },
        {
            "code": "S01.01",
            "description": "Laceration of scalp",
            "category_code": "S01.0",
        },
        {
            "code": "S01.11",
            "description": "Laceration of eyelid",
            "category_code": "S01.1",
        },
        {
            "code": "S02.01",
            "description": "Closed fracture of vault of skull",
            "category_code": "S02.0",
        },
    ]

    for subcategory in subcategories:
        category = (
            session.query(ICD10Category)
            .filter(ICD10Category.code == subcategory["category_code"])
            .first()
        )
        new_subcategory = ICD10Subcategory(
            id=generate_uuid(),
            code=subcategory["code"],
            description=subcategory["description"],
            category_id=category.id,
        )
        session.add(new_subcategory)
    session.commit()


def seed_icd10_mini_categories():
    mini_categories = [
        {
            "code": "S00.201",
            "description": "Unspecified superficial injury of right eyelid and periocular area",
            "subcategory_code": "S00.01",
        },
    ]

    for mini_category in mini_categories:
        subcategory = (
            session.query(ICD10Subcategory)
            .filter(ICD10Subcategory.code == mini_category["subcategory_code"])
            .first()
        )
        new_mini_category = ICD10MiniCategory(
            id=generate_uuid(),
            code=mini_category["code"],
            description=mini_category["description"],
            subcategory_id=subcategory.id,
        )
        session.add(new_mini_category)
    session.commit()


def seed_ais_codes():
    ais_codes = [
        {"code": "1", "description": "Minor", "severity": 1},
        {"code": "2", "description": "Moderate", "severity": 2},
        {"code": "3", "description": "Serious", "severity": 3},
        {"code": "4", "description": "Severe", "severity": 4},
        {"code": "5", "description": "Critical", "severity": 5},
        {"code": "6", "description": "Maximum", "severity": 6},
    ]

    for ais in ais_codes:
        new_ais = AIS(
            id=generate_uuid(),
            code=ais["code"],
            description=ais["description"],
            severity=ais["severity"],
        )
        session.add(new_ais)
    session.commit()


def seed_injuries():
    mini_categories = session.query(ICD10MiniCategory).limit(5).all()
    ais_codes = session.query(AIS).all()

    for i in range(10):  # Create 10 sample injuries
        mini_category = mini_categories[i % len(mini_categories)]
        ais = ais_codes[i % len(ais_codes)]
        new_injury = Injury(
            id=generate_uuid(),
            icd10_mini_category_id=mini_category.id,
            ais_code=ais.code,
            description=f"Sample injury {i+1} - {mini_category.description}",
        )
        session.add(new_injury)
    session.commit()


def seed_patients():
    for i in range(5):
        new_patient = Patient(
            id=generate_uuid(),
            name=f"Patient {i+1}",
            date_of_birth=str((datetime.now() - timedelta(days=365 * 30)).date()),
        )
        session.add(new_patient)
    session.commit()


def seed_claims():
    patients = session.query(Patient).all()
    injuries = session.query(Injury).all()
    statuses = ["Pending", "Approved", "Rejected", "Under Review"]

    for i in range(20):
        patient = patients[i % len(patients)]
        injury = injuries[i % len(injuries)]
        new_claim = Claim(
            id=generate_uuid(),
            patient_id=patient.id,
            injury_id=injury.id,
            status=statuses[i % len(statuses)],
            compensation_amount=float(1000 * (i + 1)),
        )
        session.add(new_claim)
    session.commit()


if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    seed_icd10_chapters()
    seed_icd10_blocks()
    seed_icd10_categories()
    seed_icd10_subcategories()
    seed_icd10_mini_categories()
    seed_ais_codes()
    seed_injuries()
    seed_patients()
    seed_claims()
    print("Data seeding completed successfully.")
