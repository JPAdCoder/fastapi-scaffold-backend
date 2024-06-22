# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 14:54
Author:     AdCoder
Email:      17647309108@163com
"""
from app.schemas.file_param import FileBaseParam
from pydantic import BaseModel, Field


class CRUDInitFileParam(FileBaseParam):
    pass


class CRUDParam(BaseModel):
    init_file_param: CRUDInitFileParam = Field(
        title="crud模块init文件参数"
    )
