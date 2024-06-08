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
from fastapi.responses import FileResponse
from loguru import logger
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.core.config import settings
from app.generate import render_py

router = APIRouter()


@router.post("/model/generate", summary="生成model文件")
async def generate_model(
        model_param: schemas.generate_model.FormParam,
        db: Session = Depends(deps.get_db)
) -> Any:
    json_path = '{}/json/models/{}.json'.format(settings.STATICS_FILE_DIRECTORY, model_param.file_name)
    # 判断对应的json路径是否存在，不存在则创建
    json_dir = os.path.dirname(json_path)
    os.makedirs(json_dir, exist_ok=True)
    # 判断生成的model py文件路径是否存在，不存在则创建
    model_py_path = '{}/project/{}/app/models/{}.py'.format(settings.APP_PATH, model_param.project_name,
                                                            model_param.file_name)
    model_py_dir = os.path.dirname(model_py_path)
    os.makedirs(model_py_dir, exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        logger.debug(model_param.model_dump(exclude_unset=False))
        f.write(json.dumps(jsonable_encoder(model_param), ensure_ascii=False))
    render_py('{}/mako_scripts/model.mako'.format(settings.APP_PATH), json_path, model_py_path)
    return model_param
