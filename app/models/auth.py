from sqlalchemy import Boolean, Column, String, DateTime
from app.db.base_class import Base
from datetime import datetime


class Auth(Base):
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    path = Column(String)
    is_active = Column(Boolean(), default=True)
    add_datetime = Column(DateTime, default=datetime.now())
    update_datetime = Column(DateTime, onupdate=datetime.now)

    __tablename__ = 'auth'
