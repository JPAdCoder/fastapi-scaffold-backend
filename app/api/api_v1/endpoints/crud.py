# coding=utf8
"""
Time:   2022/3/30 17:20
Author: AdCoder
Email:  17647309108@163.com
"""
import json
import os.path
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from loguru import logger
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app import schemas
from app.api import deps
from app.core.config import settings
from app.generate import render_py

router = APIRouter()


@router.post("/crud/generate", summary="生成crud文件")
async def generate_crud(
        crud_param: schemas.CrudFormParam,
        db: Session = Depends(deps.get_db)
) -> Any:
    json_path = '{}/json/{}/crud/{}.json'.format(settings.STATICS_FILE_DIRECTORY, crud_param.project_name,
                                                 crud_param.file_name)
    # 判断对应的json路径是否存在，不存在则创建
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    # 判断生成的crud py文件路径是否存在，不存在则创建
    crud_py_path = '{}/project/{}/app/crud/{}.py'.format(settings.APP_PATH, crud_param.project_name,
                                                         crud_param.file_name)
    py_dir = os.path.dirname(crud_py_path)
    os.makedirs(py_dir, exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        logger.debug(crud_param.model_dump(exclude_unset=False))
        f.write(json.dumps(jsonable_encoder(crud_param), ensure_ascii=False))
    render_py('{}/mako_scripts/crud.mako'.format(settings.APP_PATH), json_path, crud_py_path)
    return crud_param
