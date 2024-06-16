# coding=utf8
"""
Time:   2022/3/30 16:31
Author: AdCoder
Email:  17647309108@163.com
"""
from loguru import logger
from fastapi import APIRouter
from app.api.api_v1.endpoints import login, users, auth, role, models, crud, schemas, api, project

api_router = APIRouter()
api_router.include_router(login.router, tags=["login(登录相关)"])
api_router.include_router(users.router, tags=["user(用户相关)"])
api_router.include_router(role.router, tags=["role(角色相关)"])
api_router.include_router(auth.router, tags=["auth(权限相关)"])
api_router.include_router(project.router, tags=["project(项目相关)"])
api_router.include_router(models.router, tags=["model(生成模型相关)"])
api_router.include_router(crud.router, tags=["crud(生成crud相关)"])
api_router.include_router(schemas.router, tags=["schema(生成schema相关)"])
api_router.include_router(api.router, tags=["api(生成api相关)"])
