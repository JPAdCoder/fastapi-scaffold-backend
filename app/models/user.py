from sqlalchemy import Boolean, Column, String, DateTime
from app.db.base_class import Base
from datetime import datetime


class User(Base):
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    hashed_password = Column(String, nullable=False)
    role_id = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    division_id = Column(String, index=True)
    add_datetime = Column(DateTime, default=datetime.now)
    update_datetime = Column(DateTime, onupdate=datetime.now)

    __tablename__ = 'user'
