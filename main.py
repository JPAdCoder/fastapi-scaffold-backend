# coding=utf8
"""
Time:   2022/3/30 15:35
Author: AdCoder
Email:  17647309108@163.com
"""

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from app.api.api_v1.api import api_router
from app.db.session import SessionLocal
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from loguru import logger
from app.models.auth import Auth
from app.models.role_auth_rels import RoleAuthRels
from app.crud import crud_auth, crud_role_auth_rels
from uuid import uuid1
import uvicorn
from app.generate.mako_render import get_generate_json_params

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.OPENAPI_JSON_URL}",
    docs_url=f"{settings.OPENAPI_DOC_URL}",
    redoc_url=f"{settings.OPENAPI_REDOC_URL}",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
app.include_router(api_router, prefix=settings.API_V1_STR)


def update_api_path_to_auth():
    """
    根据当前所有的路由信息更新权限表内容，存在则跳过，不存在则添加，将新增的权限赋值给管理员
    :TODO如果权限信息中含有路由信息中不存在的路径，说明该路由以被删除，需要删除对应的权限信息及角色权限关系信息
    """
    db = SessionLocal()
    db_auth_paths = [v.path for v in crud_auth.auth.get_all(db)]
    for v in api_router.routes:
        if v.__dict__['path'] not in db_auth_paths:
            auth = crud_auth.auth.create(db=db, obj_in=Auth(
                id=uuid1().hex,
                name=v.__dict__['summary'],
                path=v.__dict__['path'],
                is_active=True
            ))
            # 将新增的权限赋值给管理员
            crud_role_auth_rels.role_auth_rels.create(db=db, obj_in=RoleAuthRels(
                id=uuid1().hex,
                auth_id=auth.id,
                role_id="a95318200c6411efb2be8e7602803e81",
                is_active=True
            ))
            logger.debug(v.__dict__['path'])
            logger.debug(v.__dict__['summary'])
    db.close()
import json

if __name__ == '__main__':
    # 添加启动注释
    update_api_path_to_auth()
    uvicorn.run(app='main:app', host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
