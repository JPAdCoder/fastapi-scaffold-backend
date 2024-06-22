# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 15:00
Author:     AdCoder
Email:      17647309108@163com
"""
from typing import List
from pydantic import BaseModel, Field


class FileBaseParam(BaseModel):
    author: str = Field(
        "AdCoder"
    )
    email: str = Field(
        "17647309108@163.com"
    )
    merged_import_pkg_list: List[dict] = Field(
        title="导入包列表"
    )
