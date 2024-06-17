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
from loguru import logger
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app import schemas
from app.api import deps
from app.core.config import settings
from app.generate import render_py

router = APIRouter()


@router.post("/schema/generate", summary="生成schema文件")
async def generate_schema(
        schema_param: schemas.generate_schema.FormParam,
        db: Session = Depends(deps.get_db)
) -> Any:
    json_path = '{}/json/{}/schemas/{}.json'.format(settings.STATICS_FILE_DIRECTORY, schema_param.project_name,
                                                    schema_param.file_name)
    # 判断对应的json路径是否存在，不存在则创建
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    # 判断生成的schema py文件路径是否存在，不存在则创建
    schema_py_path = '{}/project/{}/app/schemas/{}.py'.format(settings.APP_PATH, schema_param.project_name,
                                                              schema_param.file_name)
    py_dir = os.path.dirname(schema_py_path)
    os.makedirs(py_dir, exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonable_encoder(schema_param), ensure_ascii=False))
    render_py('{}/mako_scripts/schema.mako'.format(settings.APP_PATH), json_path, schema_py_path)
    return schema_param
