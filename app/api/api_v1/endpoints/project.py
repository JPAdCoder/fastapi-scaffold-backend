# coding=utf8
"""
Time:   2022/3/30 17:21
Author: AdCoder
Email:  17647309108@163.com
"""
import json
import os.path

from typing import Any
from loguru import logger
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.core.config import settings
from app.generate import render_py

router = APIRouter()


@router.post("/project/generate", summary="生成项目结构文件")
async def generate_project(
        project_param: schemas.generate_project.FormParam,
        db: Session = Depends(deps.get_db)
) -> Any:
    json_path = '{}/json/{}/{}.json'.format(settings.STATICS_FILE_DIRECTORY, project_param.name,
                                            project_param.core_param.core_file_name)
    # 判断对应的json路径是否存在，不存在则创建
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    generate_core(project_param)
    # 生成 /db
    generate_db(project_param)
    # TODO 生成 /crud
    generate_crud()
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


def generate_core(core_param: schemas.generate_project.FormParam):
    core_dir = '{}/project/{}/app/core'.format(settings.APP_PATH, core_param.name)
    os.makedirs(core_dir, exist_ok=True)
    # 生成/core/config.py文件
    generate_core_config_py(core_dir, core_param)


def generate_core_config_py(core_dir: str, core_param: schemas.generate_project.FormParam):
    json_path = '{}/json/{}/core/{}.json'.format(settings.STATICS_FILE_DIRECTORY, core_param.name,
                                                 core_param.core_param.core_file_name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    core_py_path = '{}/{}.py'.format(core_dir, core_param.core_param.core_file_name)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(core_param), ensure_ascii=False))
    render_py('{}/mako_scripts/core.mako'.format(settings.APP_PATH), json_path, core_py_path)


def generate_db(project_param: schemas.generate_project.FormParam):
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
    generate_db_init_py(db_dir, project_param.name, project_param.db_param.init_file_param)
    # 生成base.py
    generate_db_base_py(db_dir, project_param.name, project_param.db_param.base_file_param)
    # 生成base_class.py
    generate_db_base_class_py(db_dir, project_param.name, project_param.db_param.base_class_file_param)
    # 生成session.py
    generate_db_session_py(db_dir, project_param.name, project_param.db_param.session_file_param)


def generate_db_init_py(db_dir: str, project_name: str, init_param: schemas.generate_project.DBInitFileParam):
    json_path = '{}/json/{}/db/__init__.json'.format(settings.STATICS_FILE_DIRECTORY, project_name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    db_init_py_path = '{}/__init__.py'.format(db_dir)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(init_param), ensure_ascii=False))
    render_py('{}/mako_scripts/db/__init__.mako'.format(settings.APP_PATH), json_path, db_init_py_path)


def generate_db_base_py(db_dir: str, project_name: str, base_param: schemas.generate_project.DBBaseFileParam):
    json_path = '{}/json/{}/db/base.json'.format(settings.STATICS_FILE_DIRECTORY, project_name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    db_base_py_path = '{}/base.py'.format(db_dir)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(base_param), ensure_ascii=False))
    render_py('{}/mako_scripts/db/base.mako'.format(settings.APP_PATH), json_path, db_base_py_path)


def generate_db_base_class_py(db_dir: str, project_name: str,
                              base_class_param: schemas.generate_project.DBBaseClassFileParam):
    json_path = '{}/json/{}/db/base_class.json'.format(settings.STATICS_FILE_DIRECTORY, project_name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    db_base_class_py_path = '{}/base_class.py'.format(db_dir)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(base_class_param), ensure_ascii=False))
    render_py('{}/mako_scripts/db/base_class.mako'.format(settings.APP_PATH), json_path, db_base_class_py_path)


def generate_db_session_py(db_dir: str, project_name: str,
                           session_param: schemas.generate_project.DBSessionFileParam):
    json_path = '{}/json/{}/db/session.json'.format(settings.STATICS_FILE_DIRECTORY, project_name)
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    db_session_py_path = '{}/session.py'.format(db_dir)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(session_param), ensure_ascii=False))
    render_py('{}/mako_scripts/db/session.mako'.format(settings.APP_PATH), json_path, db_session_py_path)


def generate_crud():
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
