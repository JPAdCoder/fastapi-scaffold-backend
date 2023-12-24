# coding=utf8
"""
Time:   2022/3/30 17:18
Author: AdCoder
Email:  17647309108@163.com
"""
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, String, DateTime, JSON


class Generator(Base):
    id = Column(String, primary_key=True, index=True)
    project_id = Column(String, index=True)
    api_json = Column(JSON)
    module = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    add_datetime = Column(DateTime, default=datetime.now())
    update_datetime = Column(DateTime, onupdate=datetime.now)

    __tablename__ = 'generate'
