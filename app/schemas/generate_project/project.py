# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/16 15:55
Author:     AdCoder
Email:      17647309108@163com
"""
from pydantic import BaseModel, Field
from app.schemas.generate_project.db import DBParam
from app.schemas.generate_project.crud import CRUDParam
from app.schemas.generate_project.core import CoreParam
from app.schemas.file_param import FileBaseParam


class ProjectParam(FileBaseParam):
    pass


class FormParam(ProjectParam):
    name: str = Field(
        title="项目名称"
    )
    core_param: CoreParam = Field(
        title="core文件配置参数"
    )
    db_param: DBParam = Field(
        title="db模块配置参数"
    )
    crud_param: CRUDParam = Field(
        title="crud模块配置参数"
    )
