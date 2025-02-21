import pytest
from fastapi.testclient import TestClient
from app.core.config import settings
from uuid import uuid1
import os

pytestmark = pytest.mark.api

def test_generate_crud(client: TestClient, test_auth_headers: dict):
    """
    测试生成CRUD文件
    """
    crud_data = {
        "project_name": f"test-project-{uuid1().hex}",
        "file_name": "test_crud",
        "model_name": "TestModel",
        "table_name": "test_table",
        "fields": [
            {
                "field_name": "name",
                "field_type": "str",
                "field_description": "Test field"
            }
        ]
    }
    
    r = client.post(
        f"{settings.API_V1_STR}/crud/generate",
        headers=test_auth_headers,
        json=crud_data
    )
    
    result = r.json()
    assert r.status_code == 200
    assert result["project_name"] == crud_data["project_name"]
    assert result["file_name"] == crud_data["file_name"]
    
    # 验证文件是否生成
    json_path = f"{settings.STATICS_FILE_DIRECTORY}/json/{crud_data['project_name']}/crud/{crud_data['file_name']}.json"
    crud_py_path = f"{settings.APP_PATH}/project/{crud_data['project_name']}/app/crud/{crud_data['file_name']}.py"
    
    assert os.path.exists(json_path)
    assert os.path.exists(crud_py_path)

def test_generate_crud_without_auth(client: TestClient):
    """
    测试未认证时生成CRUD文件
    """
    crud_data = {
        "project_name": f"test-project-{uuid1().hex}",
        "file_name": "test_crud",
        "model_name": "TestModel",
        "table_name": "test_table",
        "fields": []
    }
    
    r = client.post(
        f"{settings.API_V1_STR}/crud/generate",
        json=crud_data
    )
    
    assert r.status_code == 401
    assert "Not authenticated" in r.json()["detail"]