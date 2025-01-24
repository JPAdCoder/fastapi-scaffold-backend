# coding=utf8
"""
Project :   generate-fastapi-be
Time:   2024/5/7 18:42
Author: AdCoder
Email:  17647309108@163.com
"""
from loguru import logger
from app.crud.crud_user import user as crud_user
from app.schemas.user import UserCreate, UserUpdate
from app.db.session import SessionLocal
from fastapi.encoders import jsonable_encoder
import os
from dotenv import load_dotenv
import pytest
from sqlalchemy.orm import Session
from uuid import uuid1
from app.core.config import settings

# 加载环境变量
load_dotenv()

# 从环境变量获取测试配置
TEST_USER_NAME = os.getenv("TEST_USER_NAME", "test_user")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD", "test_password")
TEST_ROLE_ID = os.getenv("TEST_ROLE_ID", "test_role_id")
TEST_DIVISION_ID = os.getenv("TEST_DIVISION_ID", "test_division_id")

pytestmark = [pytest.mark.unit, pytest.mark.db]

def test_get_users_search_count(db: Session):
    """
    测试获取搜索用户总数
    """
    count = crud_user.get_users_search_count(db=db, name_like="")
    logger.debug(f"\n count={count}")


def test_get_users_search(db: Session):
    """
    测试搜索用户
    """
    data = crud_user.get_users_search(db=db, skip=0, limit=10, name_like="")
    logger.debug(f"\n data={data}")


def test_get_all(db: Session):
    """
    测试获取所有用户
    """
    data = crud_user.get_all(db=db)
    logger.debug(f"\n {data}")


def test_create_user(db: Session):
    """
    测试创建用户
    """
    user_in = UserCreate(
        name=f"test.create.user.{uuid1().hex}",
        password="test-password",
        role_id=uuid1().hex,
        division_id=uuid1().hex,
        is_superuser=False,
        is_active=True
    )
    user_db = crud_user.create(db, obj_in=user_in)
    assert user_db.name == user_in.name
    assert user_db.role_id == user_in.role_id
    assert user_db.division_id == user_in.division_id
    assert not user_db.is_superuser
    assert user_db.is_active

def test_get_user_by_id(db: Session, test_user: dict):
    """
    测试通过ID获取用户
    """
    user_db = crud_user.get(db, model_id=test_user["id"])
    assert user_db
    assert user_db.id == test_user["id"]
    assert user_db.name == test_user["name"]

def test_get_user_by_name(db: Session, test_user: dict):
    """
    测试通过用户名获取用户
    """
    user_db = crud_user.get_by_name(db, name=test_user["name"])
    assert user_db
    assert user_db.id == test_user["id"]
    assert user_db.name == test_user["name"]

def test_update_user(db: Session, test_user: dict):
    """
    测试更新用户信息
    """
    new_division_id = uuid1().hex
    user_update = UserUpdate(division_id=new_division_id)
    # 首先获取用户对象
    user_obj = crud_user.get(db, model_id=test_user["id"])
    assert user_obj, f"用户 {test_user['id']} 不存在"
    user_db = crud_user.update(db, db_obj=user_obj, obj_in=user_update)
    assert user_db.division_id == new_division_id

def test_authenticate_user(db: Session, test_user: dict):
    """
    测试用户认证
    """
    authenticated_user = crud_user.authenticate(
        db, 
        name=test_user["name"], 
        password=settings.TEST_USER_PASSWORD
    )
    assert authenticated_user
    assert authenticated_user.id == test_user["id"]

def test_not_authenticate_user(db: Session):
    """
    测试错误的用户认证
    """
    authenticated_user = crud_user.authenticate(
        db, 
        name="wrong-user", 
        password="wrong-password"
    )
    assert not authenticated_user


if __name__ == '__main__':
    db = SessionLocal()
    test_create_user(db)
    db.close()