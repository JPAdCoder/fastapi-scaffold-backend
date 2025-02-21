# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 15:00
Author:     AdCoder
Email:      17647309108@163com

This module defines base parameter classes that are used throughout the project
for configuration and code generation.
"""
from typing import List
from pydantic import BaseModel, Field, ConfigDict


class BaseParam(BaseModel):
    """Base parameter class for all parameter models"""
    author: str = Field(
        title="作者"
    )
    email: str = Field(
        title="邮箱"
    )
    project_name: str = Field(
        title="项目名称"
    )
    model_name: str = Field(
        title="模块名称"
    )
    base_model_name: str = Field(
        None,
        title="父类名"
    )
    file_name: str = Field(
        None,
        title="生成的文件名"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class FileBaseParam(BaseModel):
    """Base parameter class for file generation"""
    author: str = Field(
        "AdCoder"
    )
    email: str = Field(
        "17647309108@163.com"
    )
    merged_import_pkg_list: List[dict] = Field(
        [],
        title="导入包列表"
    )
