from app.database.connections import SessionLocal

db = SessionLocal()
print("Connected to DB:", db)
db.close()
