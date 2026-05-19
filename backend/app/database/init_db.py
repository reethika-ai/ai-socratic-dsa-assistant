from app.database.db import engine
from app.database.base import Base

from app.models.message import Message


def init_db():
    Base.metadata.create_all(bind=engine)