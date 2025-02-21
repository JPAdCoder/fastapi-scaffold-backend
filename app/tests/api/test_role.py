import pytest
from fastapi.testclient import TestClient
from app.core.config import settings

pytestmark = pytest.mark.api

def test_create_role(client: TestClient, test_auth_headers: dict):
    """
    测试创建角色
    """
    role_data = {
        "name": "test-role",
        "description": "Test role description",
        "is_active": True
    }
    r = client.post(
        f"{settings.API_V1_STR}/role/",
        headers=test_auth_headers,
        json=role_data
    )
    result = r.json()
    assert r.status_code == 200
    assert result["name"] == role_data["name"]
    assert result["description"] == role_data["description"]
    return result

def test_get_role(client: TestClient, test_auth_headers: dict):
    """
    测试获取单个角色
    """
    role = test_create_role(client, test_auth_headers)
    r = client.get(
        f"{settings.API_V1_STR}/role/{role['id']}",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == role["id"]
    assert result["name"] == role["name"]

def test_get_roles(client: TestClient, test_auth_headers: dict):
    """
    测试获取角色列表
    """
    r = client.get(
        f"{settings.API_V1_STR}/role/",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert isinstance(result, list)

def test_update_role(client: TestClient, test_auth_headers: dict):
    """
    测试更新角色
    """
    role = test_create_role(client, test_auth_headers)
    update_data = {
        "description": "Updated role description"
    }
    r = client.put(
        f"{settings.API_V1_STR}/role/{role['id']}",
        headers=test_auth_headers,
        json=update_data
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == role["id"]
    assert result["description"] == update_data["description"]

def test_delete_role(client: TestClient, test_auth_headers: dict):
    """
    测试删除角色
    """
    role = test_create_role(client, test_auth_headers)
    r = client.delete(
        f"{settings.API_V1_STR}/role/{role['id']}",
        headers=test_auth_headers
    )
    assert r.status_code == 200
    
    # 验证角色已被删除
    r = client.get(
        f"{settings.API_V1_STR}/role/{role['id']}",
        headers=test_auth_headers
    )
    assert r.status_code == 404

def test_assign_role_to_user(client: TestClient, test_auth_headers: dict, test_user: dict):
    """
    测试为用户分配角色
    """
    role = test_create_role(client, test_auth_headers)
    assign_data = {
        "user_id": test_user["id"],
        "role_id": role["id"]
    }
    r = client.post(
        f"{settings.API_V1_STR}/role/assign",
        headers=test_auth_headers,
        json=assign_data
    )
    assert r.status_code == 200
    
    # 验证用户角色分配
    r = client.get(
        f"{settings.API_V1_STR}/role/user/{test_user['id']}",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert any(r["id"] == role["id"] for r in result)