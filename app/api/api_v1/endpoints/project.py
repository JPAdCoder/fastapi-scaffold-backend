# coding=utf8
"""
Time:   2022/3/30 17:21
Author: AdCoder
Email:  17647309108@163.com
"""
import json
import os.path

from typing import Any
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from loguru import logger
from app.api import deps
from app.core.config import settings
from app.generate import render_py
from app.schemas.generate_project.project import FormParam
from app.schemas.generate_project.db import DBInitFileParam, DBBaseFileParam, DBBaseClassFileParam, DBSessionFileParam
from app.schemas.generate_project.crud import CRUDInitFileParam

router = APIRouter()


@router.post("/project/generate", summary="生成项目结构文件")
async def generate_project(
        project_param: FormParam,
        db: Session = Depends(deps.get_db)
) -> Any:
    json_path = '{}/json/{}/config.json'.format(settings.STATICS_FILE_DIRECTORY, project_param.name, )
    # 判断对应的json路径是否存在，不存在则创建
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    generate_core(project_param)
    # 生成 /db
    generate_db(project_param)
    # 生成 /crud
    # TODO 生成 /models
    generate_models(project_param)
    # TODO 生成 /schemas
    generate_schemas(project_param)
    # TODO 生成 /api
    generate_api(project_param)
    # TODO 生成 /tests
    generate_tests(project_param)
    # TODO 生成 /utils
    generate_utils(project_param)
    # TODO 生成 .drone.yml
    generate_drone_yml(project_param)
    # TODO 生成 .gitignore
    generate_gitignore(project_param)
    # TODO 生成 Dockerfile
    generate_dockerfile(project_param)
    # TODO 生成 version.txt.mako
    generate_version_txt(project_param)
    return jsonable_encoder({"msg": "success"})


def generate_core(core_param: FormParam):
    core_dir = '{}/project/{}/app/core'.format(settings.APP_PATH, core_param.name)
    os.makedirs(core_dir, exist_ok=True)
    # 生成/core/config.py文件
    generate_file(core_dir, core_param.name, 'core', 'config.py', 'config.mako', core_param)


def generate_core_config_py(core_dir: str, core_param: FormParam):
    json_path = '{}/json/{}/core/config.json'.format(settings.STATICS_FILE_DIRECTORY, core_param.name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    core_py_path = '{}/config.py'.format(core_dir)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(core_param), ensure_ascii=False))
    render_py('{}/mako_scripts/core/config.mako'.format(settings.APP_PATH), json_path, core_py_path)


def generate_db(project_param: FormParam):
    db_dir = '{}/project/{}/app/db'.format(settings.APP_PATH, project_param.name)
    os.makedirs(db_dir, exist_ok=True)
    project_param.db_param.init_file_param.author = project_param.author
    project_param.db_param.init_file_param.email = project_param.email
    project_param.db_param.base_file_param.author = project_param.author
    project_param.db_param.base_file_param.email = project_param.email
    project_param.db_param.base_class_file_param.author = project_param.author
    project_param.db_param.base_class_file_param.email = project_param.email
    project_param.db_param.session_file_param.author = project_param.author
    project_param.db_param.session_file_param.email = project_param.email
    # 生成__init__.py
    generate_file(db_dir, project_param.name, 'db', '__init__.py', '__init__.mako',
                  project_param.db_param.init_file_param)
    # 生成base.py
    generate_file(db_dir, project_param.name, 'db', 'base.py', 'base.mako', project_param.db_param.base_file_param)
    # 生成base_class.py
    generate_file(db_dir, project_param.name, 'db', 'base_class.py', 'base_class.mako',
                  project_param.db_param.base_file_param)
    # 生成session.py
    generate_file(db_dir, project_param.name, 'db', 'session.py', 'session.mako',
                  project_param.db_param.session_file_param)


def generate_file(module_dir: str, project_name: str, module_name: str, file_name: str, mako_path: str, param):
    json_path = '{}/json/{}/{}/{}.json'.format(settings.STATICS_FILE_DIRECTORY, project_name, module_name, file_name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    py_path = '{}/{}'.format(module_dir, file_name)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(param), ensure_ascii=False))
    render_py('{}/mako_scripts/{}/{}'.format(settings.APP_PATH, module_name, mako_path), json_path, py_path)


def generate_crud(project_param: FormParam):
    crud_dir = '{}/project/{}/app/crud'.format(settings.APP_PATH, project_param.name)
    os.makedirs(crud_dir, exist_ok=True)
    # 生成__init__.py
    generate_file(crud_dir, project_param.name, 'crud', '__init__.py', '__init__.mako',
                  project_param.crud_param.init_file_param)
    # 生成base.py
    generate_file(crud_dir, project_param.name, 'crud', 'base.py', 'base.mako',
                  project_param.crud_param.base_file_param)
    # 生成crud_auth.py
    generate_file(crud_dir, project_param.name, 'crud', 'crud_auth.py',
                  'crud_auth.mako',
                  project_param.crud_param.auth_file_param)
    # 生成crud_role.py
    generate_file(crud_dir, project_param.name, 'crud', 'crud_role.py',
                  'crud_role.mako',
                  project_param.crud_param.role_file_param)
    # 生成crud_role_auth_rels.py
    generate_file(crud_dir, project_param.name, 'crud', 'crud_role_auth_rels.py',
                  'crud_role_auth_rels.mako',
                  project_param.crud_param.role_auth_rels_file_param)
    # 生成crud_user.py
    generate_file(crud_dir, project_param.name, 'crud', 'crud_user.py',
                  'crud_user.mako',
                  project_param.crud_param.user_file_param)


def generate_models(project_param: FormParam):
    models_dir = '{}/project/{}/app/models'.format(settings.APP_PATH, project_param.name)
    os.makedirs(models_dir, exist_ok=True)
    # 生成__init__.py
    generate_file(models_dir, project_param.name, 'models', '__init__.py',
                  '__init__.mako', project_param.models_param.init_file_param)
    # 生成auth.py
    generate_file(models_dir, project_param.name, 'models', 'auth.py',
                  'auth.mako', project_param.models_param.auth_file_param)
    # 生成role.py
    generate_file(models_dir, project_param.name, 'models', 'role.py',
                  'role.mako', project_param.models_param.role_file_param)
    # 生成user.py
    generate_file(models_dir, project_param.name, 'models', 'user.py',
                  'user.mako', project_param.models_param.user_file_param)
    # 生成role_auth_rels.py
    generate_file(models_dir, project_param.name, 'models', 'role_auth_rels.py',
                  'role_auth_rels.mako', project_param.models_param.role_auth_rels_file_param)


def generate_schemas(project_param: FormParam):
    schemas_dir = '{}/project/{}/app/schemas'.format(settings.APP_PATH, project_param.name)
    os.makedirs(schemas_dir, exist_ok=True)
    # 生成__init__.py
    generate_file(schemas_dir, project_param.name, 'schemas', '__init__.py',
                  '__init__.mako', project_param.schemas_param.init_file_param)
    # 生成token.py
    generate_file(schemas_dir, project_param.name, 'schemas', 'token.py',
                  'token.mako', project_param.schemas_param.token_file_param)
    # 生成auth.py
    generate_file(schemas_dir, project_param.name, 'schemas', 'auth.py',
                  'auth.mako', project_param.schemas_param.auth_file_param)
    # 生成role.py
    generate_file(schemas_dir, project_param.name, 'schemas', 'role.py',
                  'role.mako', project_param.schemas_param.role_file_param)
    # 生成user.py
    generate_file(schemas_dir, project_param.name, 'schemas', 'user.py',
                  'user.mako', project_param.schemas_param.user_file_param)
    # 生成role_auth_rels.py
    generate_file(schemas_dir, project_param.name, 'schemas', 'role_auth_rels.py',
                  'role_auth_rels.mako', project_param.schemas_param.role_auth_rels_file_param)


def generate_api(project_param: FormParam):
    api_dir = '{}/project/{}/app/api'.format(settings.APP_PATH, project_param.name)
    os.makedirs(api_dir, exist_ok=True)
    # 生成deps.py文件
    generate_file(api_dir, project_param.name, 'api', 'deps.py',
                  'deps.mako', project_param.api_param.deps_file_param)
    # 生成api_v1/api.py文件
    generate_file(api_dir, project_param.name, 'api/api_v1', 'api.py',
                  'api.mako', project_param.api_param.api_v1_api_file_param)
    # 生成api_v1/endpoints/user.py文件
    generate_file(api_dir, project_param.name, 'api/api_v1/endpoints', 'user.py',
                  'user.mako', project_param.api_param.api_v1_endpoints_user_file_param)
    # 生成api_v1/endpoints/role.py文件
    generate_file(api_dir, project_param.name, 'api/api_v1/endpoints', 'role.py',
                  'role.mako', project_param.api_param.api_v1_endpoints_role_file_param)
    # 生成api_v1/endpoints/auth.py文件
    generate_file(api_dir, project_param.name, 'api/api_v1/endpoints', 'auth.py',
                  'auth.mako', project_param.api_param.api_v1_endpoints_auth_file_param)
    # 生成api_v1/endpoints/login.py文件
    generate_file(api_dir, project_param.name, 'api/api_v1/endpoints', 'login.py',
                  'login.mako', project_param.api_param.api_v1_endpoints_login_file_param)


def generate_tests(project_param: FormParam):
    tests_dir = '{}/project/{}/app/tests'.format(settings.APP_PATH, project_param.name)
    os.makedirs(tests_dir, exist_ok=True)


def generate_utils(project_param: FormParam):
    utils_dir = '{}/project/{}/app/utils'.format(settings.APP_PATH, project_param.name)
    os.makedirs(utils_dir, exist_ok=True)
    # 生成security.py
    generate_file(utils_dir, project_param.name, 'utils', 'security.py',
                  'security.mako', project_param.utils_param.security_file_param)


def generate_drone_yml(project_param: FormParam):
    drone_yml_dir = '{}/project/{}/app'.format(settings.APP_PATH, project_param.name)
    os.makedirs(drone_yml_dir, exist_ok=True)
    # 生成.drone.yml
    generate_file(drone_yml_dir, project_param.name, '', '.drone.yml',
                  '.drone.yml.mako', project_param.drone_yml_file_param)


def generate_gitignore(project_param: FormParam):
    gitignore_dir = '{}/project/{}/app'.format(settings.APP_PATH, project_param.name)
    os.makedirs(gitignore_dir, exist_ok=True)
    # 生成.gitignore
    generate_file(gitignore_dir, project_param.name, '', '.gitignore',
                  '.gitignore.mako', project_param.gitignore_file_param)


def generate_dockerfile(project_param: FormParam):
    dockerfile_dir = '{}/project/{}/app'.format(settings.APP_PATH, project_param.name)
    os.makedirs(dockerfile_dir, exist_ok=True)
    # 生成dockerfile
    generate_file(dockerfile_dir, project_param.name, '', 'Dockerfile',
                  'Dockerfile.mako', project_param.dockerfile_file_param)


def generate_version_txt(project_param: FormParam):
    version_txt_dir = '{}/project/{}/app'.format(settings.APP_PATH, project_param.name)
    os.makedirs(version_txt_dir, exist_ok=True)
    # 生成version.txt
    generate_file(version_txt_dir, project_param.name, '', 'version.txt',
                  'version.txt.mako', project_param.version_txt_file_param)
