# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 15:00
Author:     AdCoder
Email:      17647309108@163com

This module contains parameter classes for various code generators including
API, CRUD, Model, and Schema generators.
"""
from pydantic import Field
from app.schemas.base import BaseParam


class ApiFormParam(BaseParam):
    """Parameters for API code generation"""
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


class CrudFormParam(BaseParam):
    """Parameters for CRUD code generation"""
    base_crud_class: str = Field(
        title="父级模块名称"
    )
    crud_obj: str = Field(
        title="crud对象名"
    )


class ModelFormParam(BaseParam):
    """Parameters for Model code generation"""
    table_name: str = Field(
        title="数据库表名"
    )
    field_list: list = Field(
        title="字段列表"
    )


class SchemaFormParam(BaseParam):
    """Parameters for Schema code generation"""
    field_list: list = Field(
        title="字段列表"
    )
    schema_name: str = Field(
        title="schema名称"
    )
    schema_description: str = Field(
        title="schema描述"
    )
