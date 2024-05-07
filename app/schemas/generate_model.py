# coding=utf-8
"""
Time 2022-7-15 16:23
Author AdCoder
Email 17647309108@163.com
"""
from typing import List
from pydantic import BaseModel, Field
from app.schemas.base_param import BaseParam, ConfigDict


class ColumnParam(BaseModel):
    column_name: str = Field(
        title="生成model对应的字段名称"
    )
    column_attr: str = Field(
        title="生成model对应的属性内容"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class FormParam(BaseParam):
    base_model_name: str = Field(
        title="父级模块名称"
    )
    table_name: str = Field(
        title="数据表名"
    )
    table_comment: str = Field(
        title="数据表备注"
    )
    columns: List[ColumnParam] = Field(
        title="字段数组"
    )
