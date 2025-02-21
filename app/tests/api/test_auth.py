import pytest
from fastapi.testclient import TestClient
from app.core.config import settings

pytestmark = pytest.mark.api

def test_get_auths(client: TestClient, test_auth_headers: dict):
    """
    测试获取权限列表
    """
    r = client.get(
        f"{settings.API_V1_STR}/auths",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert "items" in result
    assert isinstance(result["items"], list)

def test_get_auth_by_id(client: TestClient, test_auth_headers: dict):
    """
    测试通过ID获取权限
    """
    # 先获取权限列表
    r = client.get(
        f"{settings.API_V1_STR}/auths",
        headers=test_auth_headers
    )
    auths = r.json()["items"]
    if not auths:
        pytest.skip("No auth records available for testing")
    
    # 测试获取单个权限
    auth_id = auths[0]["id"]
    r = client.get(
        f"{settings.API_V1_STR}/auth/{auth_id}",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == auth_id

def test_search_auths(client: TestClient, test_auth_headers: dict):
    """
    测试搜索权限
    """
    r = client.get(
        f"{settings.API_V1_STR}/auths/search?name_like=test",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert "items" in result
    assert isinstance(result["items"], list)

def test_update_auth(client: TestClient, test_auth_headers: dict):
    """
    测试更新权限
    """
    # 先获取权限列表
    r = client.get(
        f"{settings.API_V1_STR}/auths",
        headers=test_auth_headers
    )
    auths = r.json()["items"]
    if not auths:
        pytest.skip("No auth records available for testing")
    
    # 测试更新权限
    auth_id = auths[0]["id"]
    update_data = {
        "description": "Updated auth description"
    }
    r = client.put(
        f"{settings.API_V1_STR}/auth/{auth_id}",
        headers=test_auth_headers,
        json=update_data
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == auth_id
    assert result["description"] == update_data["description"]

def test_delete_auth(client: TestClient, test_auth_headers: dict):
    """
    测试删除权限
    """
    # 先获取权限列表
    r = client.get(
        f"{settings.API_V1_STR}/auths",
        headers=test_auth_headers
    )
    auths = r.json()["items"]
    if not auths:
        pytest.skip("No auth records available for testing")
    
    # 测试删除权限
    auth_id = auths[0]["id"]
    r = client.delete(
        f"{settings.API_V1_STR}/auth/delete/{auth_id}",
        headers=test_auth_headers
    )
    assert r.status_code == 200
    
    # 验证权限已被标记为非活动状态
    r = client.get(
        f"{settings.API_V1_STR}/auth/{auth_id}",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert not result["is_active"]

def test_access_auth_without_token(client: TestClient):
    """
    测试未认证访问权限接口
    """
    r = client.get(f"{settings.API_V1_STR}/auths")
    assert r.status_code == 401
    assert "Not authenticated" in r.json()["detail"]