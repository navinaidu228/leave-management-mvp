# leave_management/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database (file: leave_mgmt.db in project root)
SQLALCHEMY_DATABASE_URL = "sqlite:///./leave_mgmt.db"

# For SQLite, we need connect_args
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session for interacting with DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency (used in main.py for DB sessions)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
