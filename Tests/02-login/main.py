
from fastapi import FastAPI

from src.api.auth import router as auth_router
from src.api.database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Python Authentication API",
    version="1.0.0"
)


app.include_router(auth_router)