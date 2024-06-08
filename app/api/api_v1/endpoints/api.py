# coding=utf8
"""
Time:   2022/3/30 17:20
Author: AdCoder
Email:  17647309108@163.com
"""
import json
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


@router.post("/api/generate", summary="生成api文件")
async def generate_crud(
        model_param: schemas.generate_api.FormParam,
        db: Session = Depends(deps.get_db)
) -> Any:
    json_path = '{}/json/api/{}.json'.format(settings.STATICS_FILE_DIRECTORY, model_param.file_name)
    with open(json_path, 'w', encoding='utf-8') as f:
        logger.debug(model_param.model_dump(exclude_unset=False))
        f.write(json.dumps(jsonable_encoder(model_param), ensure_ascii=False))
    file_path = render_py('{}/mako_scripts/api.mako'.format(settings.APP_PATH), json_path,
                          '{}/project/mako_project/app/api/{}.py'.format(settings.APP_PATH, model_param.file_name))
    return FileResponse(file_path)
