from sqlalchemy import Boolean, Column, String, DateTime
from app.db.base_class import Base
from datetime import datetime


class RoleAuthRels(Base):
    id = Column(String, primary_key=True, index=True)
    role_id = Column(String, index=True)
    auth_id = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    add_datetime = Column(DateTime, default=datetime.now)
    update_datetime = Column(DateTime, onupdate=datetime.now)

    __tablename__ = 'role_auth_rels'
