# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 22:44
Author:     AdCoder
Email:      17647309108@163com
"""
from app.schemas.base import FileBaseParam
from pydantic import BaseModel, Field


class UtilsSecurityFileParam(FileBaseParam):
    pass


class UtilsParam(BaseModel):
    security_file_param: UtilsSecurityFileParam = Field(
        title="utils模块security文件参数"
    )
