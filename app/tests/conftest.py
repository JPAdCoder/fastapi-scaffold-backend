import pytest
from typing import Dict, Generator
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from uuid import uuid1

from app.core.config import settings
from app.db.session import SessionLocal
from app.main import app
from app import crud, schemas
from app.utils import security

# 添加项目根目录到Python路径
root_dir = str(Path(__file__).parent.parent.parent)
sys.path.append(root_dir)

from main import app
from app.core.config import settings
from app.crud.crud_user import user
from app.schemas.user import UserCreate
from uuid import uuid1
import os
from dotenv import load_dotenv

# 加载测试环境变量
load_dotenv()

@pytest.fixture(scope="session")
def db() -> Generator:
    """
    数据库会话固件
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def client() -> Generator:
    """
    FastAPI TestClient固件
    """
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def test_role(db: Session) -> dict:
    """
    测试角色固件
    """
    role_name = "admin"
    role_in = crud.role.get_by_name(db, name=role_name)
    if not role_in:
        role_in = crud.role.create(db, obj_in=schemas.RoleCreate(
            name=role_name,
            is_active=True
        ))
    return {
        "id": role_in.id,
        "name": role_in.name,
        "is_active": role_in.is_active
    }

@pytest.fixture(scope="module")
def test_user(db: Session) -> dict:
    """
    测试用户固件
    """
    user_in = UserCreate(
        name=os.getenv("TEST_USER_NAME", "test.user"),
        password=os.getenv("TEST_USER_PASSWORD", "test-password-123"),
        role_id=os.getenv("TEST_ROLE_ID", uuid1().hex),
        division_id=os.getenv("TEST_DIVISION_ID", uuid1().hex),
        is_superuser=False,
        is_active=True
    )
    
    # 检查用户是否已存在
    existing_user = user.get_by_name(db, name=user_in.name)
    if existing_user:
        return {
            "id": existing_user.id,
            "name": existing_user.name,
            "role_id": existing_user.role_id,
            "division_id": existing_user.division_id
        }
    
    # 创建新用户
    new_user = user.create(db, obj_in=user_in)
    return {
        "id": new_user.id,
        "name": new_user.name,
        "role_id": new_user.role_id,
        "division_id": new_user.division_id
    }

@pytest.fixture(scope="module")
def test_superuser(db: Session) -> Dict:
    """
    测试超级用户固件
    """
    user_in = UserCreate(
        name="test.admin",
        password="admin-test-123",
        role_id=uuid1().hex,
        division_id=uuid1().hex,
        is_superuser=True,
        is_active=True
    )
    
    # 检查用户是否已存在
    existing_user = user.get_by_name(db, name=user_in.name)
    if existing_user:
        return {
            "id": existing_user.id,
            "name": existing_user.name,
            "role_id": existing_user.role_id,
            "division_id": existing_user.division_id
        }
    
    # 创建新用户
    new_user = user.create(db, obj_in=user_in)
    return {
        "id": new_user.id,
        "name": new_user.name,
        "role_id": new_user.role_id,
        "division_id": new_user.division_id
    }

@pytest.fixture(scope="module")
def test_auth_headers(client: TestClient, test_user: dict) -> Dict[str, str]:
    """
    测试用户认证头固件
    """
    login_data = {
        "username": test_user["name"],
        "password": os.getenv("TEST_USER_PASSWORD", "test-password-123")
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    return {"Authorization": f"Bearer {tokens['access_token']}"}
