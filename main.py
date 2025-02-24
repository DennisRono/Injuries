from fastapi import FastAPI
from database import engine, Base
from routers import icd10, ais, injury, claim, patient
from routers.icd10 import chapter, block, category, subcategory, mini_category

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(chapter.router, prefix="/api/v1", tags=["ICD-10"])
app.include_router(block.router, prefix="/api/v1", tags=["ICD-10"])
app.include_router(category.router, prefix="/api/v1", tags=["ICD-10"])
app.include_router(subcategory.router, prefix="/api/v1", tags=["ICD-10"])
app.include_router(mini_category.router, prefix="/api/v1", tags=["ICD-10"])

app.include_router(ais.router, prefix="/api/v1", tags=["AIS"])
app.include_router(injury.router, prefix="/api/v1", tags=["Injuries"])
app.include_router(claim.router, prefix="/api/v1", tags=["Claims"])
app.include_router(patient.router, prefix="/api/v1", tags=["Patients"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Injury Classification API"}
