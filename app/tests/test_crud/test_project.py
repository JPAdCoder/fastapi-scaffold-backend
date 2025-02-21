# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/5/7 18:50
Author:     AdCoder
Email:      17647309108@163.com
"""
from loguru import logger
from sqlalchemy.orm import Session
from uuid import uuid1
from app.crud.crud_project import project as crud_project
from app.schemas.generate_project import ProjectCreate, ProjectUpdate
from app.db.session import SessionLocal
from fastapi.encoders import jsonable_encoder
import pytest

pytestmark = [pytest.mark.unit, pytest.mark.db]

def test_create_project(db: Session):
    """
    测试创建项目
    """
    project_in = ProjectCreate(
        name=f"test.project.{uuid1().hex}",
        description="Test project description",
        is_active=True
    )
    project_db = crud_project.create(db, obj_in=project_in)
    assert project_db.name == project_in.name
    assert project_db.description == project_in.description
    assert project_db.is_active == project_in.is_active
    return project_db

def test_get_project(db: Session):
    """
    测试获取项目
    """
    project_db = test_create_project(db)
    project = crud_project.get(db, model_id=project_db.id)
    assert project
    assert project.id == project_db.id
    assert project.name == project_db.name

def test_get_project_by_name(db: Session):
    """
    测试通过名称获取项目
    """
    project_db = test_create_project(db)
    project = crud_project.get_by_name(db, name=project_db.name)
    assert project
    assert project.id == project_db.id
    assert project.name == project_db.name

def test_update_project(db: Session):
    """
    测试更新项目
    """
    project_db = test_create_project(db)
    new_description = "Updated test project description"
    project_update = ProjectUpdate(description=new_description)
    updated_project = crud_project.update(db, db_obj=project_db, obj_in=project_update)
    assert updated_project.description == new_description

def test_get_projects_search(db: Session):
    """
    测试搜索项目
    """
    test_create_project(db)  # 确保有测试数据
    data = crud_project.get_projects_search(db=db, skip=0, limit=10, name_like="")
    assert hasattr(data, 'data')
    assert hasattr(data, 'total')
    assert len(data.data) > 0

if __name__ == '__main__':
    db = SessionLocal()
    test_create_project(db)
    db.close()
