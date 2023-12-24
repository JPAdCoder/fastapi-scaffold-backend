from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy import create_engine

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_recycle=3600, pool_size=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=True)
