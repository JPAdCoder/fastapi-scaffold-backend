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

def test_login_with_wrong_password(client: TestClient, test_user: dict):
    """
    测试使用错误密码登录
    """
    login_data = {
        "username": test_user["name"],
        "password": "wrong-password"
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    assert r.status_code == 400
    assert "用户名或密码错误" in r.json()["detail"]

def test_login_with_nonexistent_user(client: TestClient):
    """
    测试使用不存在的用户登录
    """
    login_data = {
        "username": "nonexistent-user",
        "password": "any-password"
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    assert r.status_code == 400
    assert "用户名或密码错误" in r.json()["detail"]

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

def test_use_invalid_token(client: TestClient):
    """
    测试使用无效的访问令牌
    """
    headers = {"Authorization": "Bearer invalid-token"}
    r = client.get(f"{settings.API_V1_STR}/user/me", headers=headers)
    assert r.status_code == 403
    assert "用户信息验证错误" in r.json()["detail"]

def test_access_without_token(client: TestClient):
    """
    测试未提供访问令牌
    """
    r = client.get(f"{settings.API_V1_STR}/user/me")
    assert r.status_code == 401
    assert "Not authenticated" in r.json()["detail"]
