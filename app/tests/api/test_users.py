import pytest
from fastapi.testclient import TestClient
from app.core.config import settings

pytestmark = pytest.mark.api

def test_create_user(client: TestClient, test_auth_headers: dict):
    """
    测试创建用户
    """
    user_data = {
        "name": "test-user",
        "email": "test@example.com",
        "password": "test-password-123",
        "is_active": True
    }
    r = client.post(
        f"{settings.API_V1_STR}/users/",
        headers=test_auth_headers,
        json=user_data
    )
    result = r.json()
    assert r.status_code == 200
    assert result["name"] == user_data["name"]
    assert result["email"] == user_data["email"]
    assert "password" not in result

def test_get_user(client: TestClient, test_auth_headers: dict, test_user: dict):
    """
    测试获取单个用户
    """
    r = client.get(
        f"{settings.API_V1_STR}/users/{test_user['id']}",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == test_user["id"]
    assert result["name"] == test_user["name"]

def test_get_users(client: TestClient, test_auth_headers: dict):
    """
    测试获取用户列表
    """
    r = client.get(
        f"{settings.API_V1_STR}/users/",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert isinstance(result, list)

def test_update_user(client: TestClient, test_auth_headers: dict, test_user: dict):
    """
    测试更新用户
    """
    update_data = {
        "email": "updated@example.com"
    }
    r = client.put(
        f"{settings.API_V1_STR}/users/{test_user['id']}",
        headers=test_auth_headers,
        json=update_data
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == test_user["id"]
    assert result["email"] == update_data["email"]

def test_delete_user(client: TestClient, test_auth_headers: dict):
    """
    测试删除用户
    """
    # 先创建一个用户
    user_data = {
        "name": "test-user-to-delete",
        "email": "delete@example.com",
        "password": "test-password-123",
        "is_active": True
    }
    create_response = client.post(
        f"{settings.API_V1_STR}/users/",
        headers=test_auth_headers,
        json=user_data
    )
    created_user = create_response.json()
    
    # 删除用户
    r = client.delete(
        f"{settings.API_V1_STR}/users/{created_user['id']}",
        headers=test_auth_headers
    )
    assert r.status_code == 200
    
    # 验证用户已被删除
    r = client.get(
        f"{settings.API_V1_STR}/users/{created_user['id']}",
        headers=test_auth_headers
    )
    assert r.status_code == 404