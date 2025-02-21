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
from app.crud.crud_auth import auth as crud_auth
from app.schemas.auth import AuthCreate, AuthUpdate
from app.db.session import SessionLocal
from fastapi.encoders import jsonable_encoder
import pytest

pytestmark = [pytest.mark.unit, pytest.mark.db]

def test_get_auths_search_count(db: Session):
    """
    测试获取搜索权限总数
    """
    count = crud_auth.get_auths_search_count(db=db, name_like="")
    logger.debug(f"\n count={count}")
    assert isinstance(count, int)

def test_get_auths_search(db: Session):
    """
    测试搜索权限
    """
    data = crud_auth.get_auths_search(db=db, skip=0, limit=10, name_like="")
    logger.debug(f"\n data={data}")
    assert hasattr(data, 'data')
    assert hasattr(data, 'total')

def test_create_auth(db: Session):
    """
    测试创建权限
    """
    auth_in = AuthCreate(
        name=f"test.create.auth.{uuid1().hex}",
        path="/api/test",
        is_active=True
    )
    auth_db = crud_auth.create(db, obj_in=auth_in)
    assert auth_db.name == auth_in.name
    assert auth_db.path == auth_in.path
    assert auth_db.is_active == auth_in.is_active
    return auth_db

def test_get_auth_by_name(db: Session):
    """
    测试通过名称获取权限
    """
    auth_db = test_create_auth(db)
    auth = crud_auth.get_by_name(db, name=auth_db.name)
    assert auth
    assert auth.id == auth_db.id
    assert auth.name == auth_db.name

def test_update_auth(db: Session):
    """
    测试更新权限
    """
    auth_db = test_create_auth(db)
    new_path = "/api/test/updated"
    auth_update = AuthUpdate(path=new_path)
    updated_auth = crud_auth.update(db, db_obj=auth_db, obj_in=auth_update)
    assert updated_auth.path == new_path

if __name__ == '__main__':
    db = SessionLocal()
    test_create_auth(db)
    db.close()
