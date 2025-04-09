from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connections import get_db
from app import models
from app.schemas import journal as journal_schema

router = APIRouter(
    prefix="/journal",
    tags=["Journal Entries"]
)

@router.post("/", response_model=journal_schema.JournalEntryResponse)
def create_journal(entry: journal_schema.JournalEntryCreate, db: Session = Depends(get_db)):
    new_entry = models.journal.JournalEntry(**entry.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.get("/{entry_id}", response_model=journal_schema.JournalEntryResponse)
def read_journal(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(models.journal.JournalEntry).filter_by(id=entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@router.get("/", response_model=list[journal_schema.JournalEntryResponse])
def list_journals(db: Session = Depends(get_db)):
    return db.query(models.journal.JournalEntry).all()

@router.put("/{entry_id}", response_model=journal_schema.JournalEntryResponse)
def update_journal(entry_id: int, updated_entry: journal_schema.JournalEntryUpdate, db: Session = Depends(get_db)):
    entry = db.query(models.journal.JournalEntry).filter_by(id=entry_id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    # Update the fields of the existing entry
    for field, value in updated_entry.dict(exclude_unset=True).items():
        setattr(entry, field, value)

    db.commit()
    db.refresh(entry)
    return entry

@router.delete("/{entry_id}")
def delete_journal(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(models.journal.JournalEntry).filter_by(id=entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"message": "Entry deleted successfully"}
