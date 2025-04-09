from app.database.connections import SessionLocal
from app.models.journal import JournalEntry
from datetime import datetime

def test_journal_entry():
    db = SessionLocal()
    try:
        new_entry = JournalEntry(
            id=1,  # make sure this user_id exists if you have FK constraints
            content="Test entry via script.",
            timestamp=datetime.utcnow()
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        print("✅ Successfully added Journal Entry with ID:", new_entry.id)
    except Exception as e:
        print("❌ Failed to insert journal entry:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_journal_entry()
