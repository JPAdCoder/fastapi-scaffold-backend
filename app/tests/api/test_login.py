import pytest
from fastapi.testclient import TestClient
from app.core.config import settings

pytestmark = pytest.mark.api

def test_get_access_token(client: TestClient, test_user: dict):
    """
    测试获取访问令牌
    """
    login_data = {
        "username": test_user["name"],
        "password": settings.TEST_USER_PASSWORD
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["token_type"] == "bearer"

def test_use_access_token(client: TestClient, test_auth_headers: dict):
    """
    测试使用访问令牌访问受保护的端点
    """
    r = client.get(
        f"{settings.API_V1_STR}/user/me", 
        headers=test_auth_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "name" in result
