# coding=utf-8
"""
Time 2022-7-18 10:12
Author AdCoder
Email 17647309108@163.com
"""
from typing import List
from pydantic import BaseModel, Field, ConfigDict


class BaseParam(BaseModel):
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
    merged_import_pkg_list: List[dict] = Field(
        title="导入包列表"
    )
    file_name: str = Field(
        title="生成文件对应的名称"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )

