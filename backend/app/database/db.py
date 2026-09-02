import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./socratic.db")

if DATABASE_URL is None:
    print("WARNING: DATABASE_URL not set. Falling back to SQLite.")
    DATABASE_URL = "sqlite:///./socratic.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)