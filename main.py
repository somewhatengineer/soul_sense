from fastapi import FastAPI
from app.routers import journal
from app import models
from app.models.journal import JournalEntry
from app.database.base import Base
from app.database.connections import engine

# TEMP: Reset DB schema
Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(journal.router)
