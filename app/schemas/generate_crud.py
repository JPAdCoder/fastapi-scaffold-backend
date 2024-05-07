# coding=utf8
"""
Time:   2022/7/18 22:36
Author: AdCoder
Email:  17647309108@163.com
"""
from pydantic import Field
from app.schemas.base_param import BaseParam, ConfigDict


class FormParam(BaseParam):
    base_crud_class: str = Field(
        title="父级模块名称"
    )
    crud_obj: str = Field(
        title="crud对象名"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )

