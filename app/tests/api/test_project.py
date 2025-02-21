import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from uuid import uuid1
from app.core.config import settings
from app.crud.crud_project import project as crud_project
from app.schemas.project import ProjectCreate

pytestmark = pytest.mark.api

def test_create_project(client: TestClient, test_auth_headers: dict):
    """
    测试创建项目
    """
    project_data = {
        "name": f"test-project-{uuid1().hex}",
        "description": "Test project description",
        "is_active": True
    }
    r = client.post(
        f"{settings.API_V1_STR}/project/",
        headers=test_auth_headers,
        json=project_data
    )
    result = r.json()
    assert r.status_code == 200
    assert result["name"] == project_data["name"]
    assert result["description"] == project_data["description"]
    return result

def test_get_project(client: TestClient, test_auth_headers: dict):
    """
    测试获取单个项目
    """
    project = test_create_project(client, test_auth_headers)
    r = client.get(
        f"{settings.API_V1_STR}/project/{project['id']}",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == project["id"]
    assert result["name"] == project["name"]

def test_get_projects(client: TestClient, test_auth_headers: dict):
    """
    测试获取项目列表
    """
    r = client.get(
        f"{settings.API_V1_STR}/project/",
        headers=test_auth_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert isinstance(result, list)

def test_update_project(client: TestClient, test_auth_headers: dict):
    """
    测试更新项目
    """
    project = test_create_project(client, test_auth_headers)
    update_data = {
        "description": "Updated project description"
    }
    r = client.put(
        f"{settings.API_V1_STR}/project/{project['id']}",
        headers=test_auth_headers,
        json=update_data
    )
    result = r.json()
    assert r.status_code == 200
    assert result["id"] == project["id"]
    assert result["description"] == update_data["description"]

def test_delete_project(client: TestClient, test_auth_headers: dict):
    """
    测试删除项目
    """
    project = test_create_project(client, test_auth_headers)
    r = client.delete(
        f"{settings.API_V1_STR}/project/{project['id']}",
        headers=test_auth_headers
    )
    assert r.status_code == 200
    # 验证项目已被删除
    r = client.get(
        f"{settings.API_V1_STR}/project/{project['id']}",
        headers=test_auth_headers
    )
    assert r.status_code == 404

def test_create_project_without_auth(client: TestClient):
    """
    测试未认证时创建项目
    """
    project_data = {
        "name": f"test-project-{uuid1().hex}",
        "description": "Test project description",
        "is_active": True
    }
    r = client.post(
        f"{settings.API_V1_STR}/project/",
        json=project_data
    )
    assert r.status_code == 401
    assert "Not authenticated" in r.json()["detail"]