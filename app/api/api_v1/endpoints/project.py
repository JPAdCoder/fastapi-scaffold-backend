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
    # TODO 生成 /crud
    # generate_crud()
    # TODO 生成 /models
    generate_models()
    # TODO 生成 /schemas
    generate_schemas()
    # TODO 生成 /tests
    generate_tests()
    # TODO 生成 /utils
    generate_utils()
    # TODO 生成 .drone.yml
    generate_drone_yml()
    # TODO 生成 .gitignore
    generate_gitignore()
    # TODO 生成 Dockerfile
    generate_dockerfile()
    # TODO 生成 version.txt
    generate_version_txt()
    return jsonable_encoder({"msg": "success"})


def generate_core(core_param: FormParam):
    core_dir = '{}/project/{}/app/core'.format(settings.APP_PATH, core_param.name)
    os.makedirs(core_dir, exist_ok=True)
    # 生成/core/config.py文件
    generate_file(core_dir, core_param.name, 'config.py', 'core/config.mako', core_param)


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
    generate_file(db_dir, project_param.name, '__init__.py', 'db/__init__.mako', project_param.db_param.init_file_param)
    # 生成base.py
    generate_file(db_dir, project_param.name, 'base.py', 'db/base.mako', project_param.db_param.base_file_param)
    # 生成base_class.py
    generate_file(db_dir, project_param.name, 'base_class.py', 'db/base_class.mako',
                  project_param.db_param.base_file_param)
    # 生成session.py
    generate_file(db_dir, project_param.name, 'session.py', 'db/session.mako',
                  project_param.db_param.session_file_param)


def generate_file(module_dir: str, project_name: str, file_name: str, mako_path: str, param):
    json_path = '{}/json/{}/db/{}.json'.format(settings.STATICS_FILE_DIRECTORY, project_name, file_name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    py_path = '{}/{}'.format(module_dir, file_name)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(param), ensure_ascii=False))
    render_py('{}/mako_scripts/{}'.format(settings.APP_PATH, mako_path), json_path, py_path)


def generate_crud(project_param: FormParam):
    crud_dir = '{}/project/{}/app/crud'.format(settings.APP_PATH, project_param.name)
    os.makedirs(crud_dir, exist_ok=True)
    # 生成__init__.py
    # 生成base.py
    # 生成crud_auth.py
    # 生成crud_role.py
    # 生成crud_role_auth_rels.py
    # 生成crud_user.py
    pass


def generate_models():
    pass


def generate_schemas():
    pass


def generate_tests():
    pass


def generate_utils():
    pass


def generate_drone_yml():
    pass


def generate_gitignore():
    pass


def generate_dockerfile():
    pass


def generate_version_txt():
    pass
