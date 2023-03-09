from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DBSettings as _DBSettings


@lru_cache 
def get_db_settings() -> _DBSettings:
    return _DBSettings()

settings = get_db_settings()
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.username}:{settings.password}@{settings.host}:{settings.port}/{settings.database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Model = declarative_base()