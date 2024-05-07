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
from app.api.deps import SessionLocal
from fastapi.encoders import jsonable_encoder


def test_get_users_search_count():
    db = SessionLocal()
    user_db = crud_user.get_users_search_count(db=db, name_like="")
    db.close()
    logger.debug(user_db)


def test_get_users_search():
    db = SessionLocal()
    user_db = crud_user.get_users_search(db=db)
    db.close()
    logger.debug(user_db)


def test_get_all():
    db = SessionLocal()
    user_db = crud_user.get_all(db=db)
    db.close()
    logger.debug(jsonable_encoder(user_db))


def test_create(user_name: str = "adcoder", password: str = "96241158a0",
                role_id: str = "a95318200c6411efb2be8e7602803e81",
                division_id: str = "0"):
    """
    测试crud_user中的添加用户方法
    """
    db = SessionLocal()
    user_in = crud_user.get_by_name(db, name=user_name)
    if user_in:
        raise ValueError("用户已存在")
    user_db = crud_user.create(db, obj_in=UserCreate(
        name=user_name,
        password=password,
        role_id=role_id
    ))
    db.close()
    logger.debug(jsonable_encoder(user_db))


def test_update(user_id: str = "33fac4520c7211efa1868e7602803e81",
                user_name: str = "",
                division_id: str = "",
                password: str = "",
                role_id: str = ""):
    """
    测试crud_user中更新用户的方法
    """
    db = SessionLocal()
    db_user = crud_user.get(db, model_id=user_id)
    if not db_user:
        raise ValueError(
            detail="用户不存在"
        )
    db_user = crud_user.update(db, db_obj=db_user, obj_in=UserUpdate(
        role_id="a95318200c6411efb2be8e7602803e81"
    ))
    db.close()
    logger.debug(jsonable_encoder(db_user))


def test_remove(user_id: str = "33fac4520c7211efa1868e7602803e81"):
    """
    测试crud_user中的删除用户方法
    """
    db = SessionLocal()
    db_user = crud_user.get(db, model_id=user_id)
    if not db_user:
        raise ValueError(
            detail="用户不存在"
        )
    db_usr = crud_user.remove(db, model_id=user_id)
    db.close()
    logger.debug(jsonable_encoder(db_user))


if __name__ == '__main__':
    test_create()
    # test_get_all()
    # test_update()
    # test_remove()