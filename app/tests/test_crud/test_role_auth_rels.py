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
from app.crud.crud_role_auth_rels import role_auth_rels as crud_role_auth_rels
from app.schemas.role_auth_rels import RoleAuthRelsCreate, RoleAuthRelsUpdate
from app.db.session import SessionLocal
from fastapi.encoders import jsonable_encoder
import pytest

pytestmark = [pytest.mark.unit, pytest.mark.db]

def test_create_role_auth_rel(db: Session):
    """
    测试创建角色权限关联
    """
    role_auth_rel_in = RoleAuthRelsCreate(
        role_id=uuid1().hex,
        auth_id=uuid1().hex,
        is_active=True
    )
    role_auth_rel_db = crud_role_auth_rels.create(db, obj_in=role_auth_rel_in)
    assert role_auth_rel_db.role_id == role_auth_rel_in.role_id
    assert role_auth_rel_db.auth_id == role_auth_rel_in.auth_id
    assert role_auth_rel_db.is_active == role_auth_rel_in.is_active
    return role_auth_rel_db

def test_get_role_auth_rel(db: Session):
    """
    测试获取角色权限关联
    """
    role_auth_rel_db = test_create_role_auth_rel(db)
    role_auth_rel = crud_role_auth_rels.get(db, model_id=role_auth_rel_db.id)
    assert role_auth_rel
    assert role_auth_rel.id == role_auth_rel_db.id
    assert role_auth_rel.role_id == role_auth_rel_db.role_id
    assert role_auth_rel.auth_id == role_auth_rel_db.auth_id

def test_update_role_auth_rel(db: Session):
    """
    测试更新角色权限关联
    """
    role_auth_rel_db = test_create_role_auth_rel(db)
    role_auth_rel_update = RoleAuthRelsUpdate(is_active=False)
    updated_role_auth_rel = crud_role_auth_rels.update(db, db_obj=role_auth_rel_db, obj_in=role_auth_rel_update)
    assert not updated_role_auth_rel.is_active

def test_get_role_auth_rels_by_role_id(db: Session):
    """
    测试通过角色ID获取权限关联
    """
    role_auth_rel_db = test_create_role_auth_rel(db)
    role_auth_rels = crud_role_auth_rels.get_multi_by_role_id(db, role_id=role_auth_rel_db.role_id)
    assert len(role_auth_rels) > 0
    assert any(rel.id == role_auth_rel_db.id for rel in role_auth_rels)

if __name__ == '__main__':
    db = SessionLocal()
    test_create_role_auth_rel(db)
    db.close()