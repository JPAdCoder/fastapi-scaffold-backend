# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/5/7 18:49
Author:     AdCoder
Email:      17647309108@163com
"""
from loguru import logger
from sqlalchemy.orm import Session
from uuid import uuid1
from app.crud.crud_role import role as crud_role
from app.schemas.role import RoleCreate, RoleUpdate
from app.db.session import SessionLocal
from fastapi.encoders import jsonable_encoder
import pytest

pytestmark = [pytest.mark.unit, pytest.mark.db]


def test_get_roles_search_count(db: Session):
    """
    测试获取搜索角色总数
    """
    count = crud_role.get_roles_search_count(db=db, name_like="")
    logger.debug(f"\n count={count}")
    assert isinstance(count, int)

def test_get_roles_search(db: Session):
    """
    测试搜索角色
    """
    data = crud_role.get_roles_search(db=db, skip=0, limit=10, name_like="")
    logger.debug(f"\n data={data}")
    assert hasattr(data, 'data')
    assert hasattr(data, 'total')

def test_create_role(db: Session):
    """
    测试创建角色
    """
    role_in = RoleCreate(
        name=f"test.create.role.{uuid1().hex}",
        is_active=True
    )
    role_db = crud_role.create(db, obj_in=role_in)
    assert role_db.name == role_in.name
    assert role_db.is_active == role_in.is_active
    return role_db

def test_get_role_by_name(db: Session):
    """
    测试通过名称获取角色
    """
    role_db = test_create_role(db)
    role = crud_role.get_by_name(db, name=role_db.name)
    assert role
    assert role.id == role_db.id
    assert role.name == role_db.name

def test_update_role(db: Session):
    """
    测试更新角色
    """
    role_db = test_create_role(db)
    new_name = f"test.update.role.{uuid1().hex}"
    role_update = RoleUpdate(name=new_name)
    updated_role = crud_role.update(db, db_obj=role_db, obj_in=role_update)
    assert updated_role.name == new_name


def test_roles_by_filter():
    pass


def test_get_roles_search_count():
    pass


def test_get_roles_by_filter_count():
    pass


def test_create(role_name: str = "admin"):
    """
    测试crud_role中的添加角色方法
    """
    db = SessionLocal()
    role_in = crud_role.get_by_name(db, role_name)
    if role_in:
        raise ValueError(f"角色 {role_name} 已存在")
    role_db = crud_role.create(db, obj_in=RoleCreate(
        name=role_name
    ))
    db.close()
    logger.debug(jsonable_encoder(role_db))


def test_update():
    pass


if __name__ == '__main__':
    # test_create()
    # test_get_all()
    test_get_multi()