from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class JournalEntryCreate(BaseModel):
    title: str
    content: str
    mood: Optional[str] = None
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)

class JournalEntryResponse(JournalEntryCreate):
    id: int

    class Config:
        from_attributes = True

class JournalEntryUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    mood: Optional[str] = None
    timestamp: Optional[datetime] = None
