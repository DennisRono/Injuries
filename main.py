from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base
from routers.icd10 import (
    classification_groups,
    injury_classification,
    ais,
    injury_sub_classification,
    injury,
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    classification_groups.router, prefix="/api/v1", tags=["Classification Groups"]
)
app.include_router(
    injury_classification.router, prefix="/api/v1", tags=["Injury Classification"]
)
app.include_router(
    injury_sub_classification.router,
    prefix="/api/v1",
    tags=["Injury Sub Classification"],
)
app.include_router(
    injury.router,
    prefix="/api/v1",
    tags=["Injury"],
)
app.include_router(ais.router, prefix="/api/v1", tags=["Abbreviated Injury Scale"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Injury Classification API"}


@asynccontextmanager
async def lifespan_wrapper(app: FastAPI):
    with engine.begin():
        Base.metadata.create_all(bind=engine)
    yield


app.router.lifespan_context = lifespan_wrapper
