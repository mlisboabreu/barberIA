from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

if DATABASE_URL.startswith("postgresql"):
    db = create_engine(DATABASE_URL)
else:
    db = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()