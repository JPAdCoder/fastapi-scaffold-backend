# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/5/7 18:49
Author:     AdCoder
Email:      17647309108@163com
"""
from loguru import logger
from app.crud.crud_role import role as crud_role
from app.api.deps import SessionLocal
from app.schemas.role import RoleCreate
from fastapi.encoders import jsonable_encoder


def test_get():
    pass


def test_get_multi(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    role_db = crud_role.get_multi(db, skip=skip, limit=limit)
    db.close()
    logger.debug(jsonable_encoder(role_db))


def test_by_name():
    pass


def test_multi_count():
    pass


def test_get_search_by_name_count():
    pass


def test_search_by_name():
    pass


def test_get_all():
    db = SessionLocal()
    role_db = crud_role.get_all(db=db)
    db.close()
    logger.debug(jsonable_encoder(role_db))

def test_get_roles_search():
    pass


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