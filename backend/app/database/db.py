import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load .env from backend root correctly
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./socratic.db")

# If it's a local sqlite database, ensure the path is absolute so it doesn't fail based on CWD
if DATABASE_URL.startswith("sqlite:///./"):
    db_file_path = env_path.parent / DATABASE_URL.replace("sqlite:///./", "")
    DATABASE_URL = f"sqlite:///{db_file_path}"
    
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)