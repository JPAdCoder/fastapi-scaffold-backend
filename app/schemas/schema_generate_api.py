# coding=utf-8
"""
Time 2022-7-25 11:25
Author AdCoder
Email 17647309108@163.com
"""
from pydantic import Field
from app.schemas.schema_base_param import BaseParam, ConfigDict


class FormParam(BaseParam):
    model_name_lower_case: str = Field(
        title="模块名小写"
    )
    schema_create_model: str = Field(
        title="添加对象参数类"
    )
    schema_update_model: str = Field(
        title="更新对象参数类"
    )
    schema_rep_model: str = Field(
        title="返回对象参数类"
    )
    schema_page_rep_model: str = Field(
        title="分页返回对象参数类"
    )
    model_name_comment: str = Field(
        title="模块中文名称"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )

