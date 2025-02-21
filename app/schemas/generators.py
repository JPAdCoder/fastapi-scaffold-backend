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
from typing import List
from app.schemas.base import BaseParam, FileBaseParam


class ApiFormParam(BaseParam, FileBaseParam):
    """Parameters for API code generation"""
    model_name_lower_case: str = Field(
        title="模块名小写"
    )
    model_name_comment: str = Field(
        title="模块信息说明"
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
        title="返回对象分页参数类"
    )


class CrudFormParam(BaseParam, FileBaseParam):
    """Parameters for CRUD code generation"""
    base_crud_class: str = Field(
        title="父级模块名称"
    )
    crud_obj: str = Field(
        title="crud对象名"
    )


class ModelFormParam(BaseParam, FileBaseParam):
    """Parameters for Model code generation"""
    table_name: str = Field(
        title="数据库表名"
    )
    table_comment: str = Field(
        title="数据表描述"
    )
    columns: List[dict] = Field(
        title="字段列表"
    )


class SchemaFormParam(BaseParam, FileBaseParam):
    """Parameters for Schema code generation"""
    schema_classes: list = Field(
        title="字段列表"
    )