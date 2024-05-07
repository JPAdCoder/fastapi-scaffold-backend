# coding=utf-8
"""
Time 2022-7-19 11:11
Author AdCoder
Email 17647309108@163.com
"""
from pydantic import Field, BaseModel
from typing import List, Optional
from app.schemas.base_param import BaseParam, ConfigDict


class MetaClassFieldParam(BaseModel):
    name: str = Field(
        title="子类属性名称"
    )
    value: str = Field(
        title="子类属性值"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class MetaClassParam(BaseModel):
    name: str = Field(
        title="子类名称"
    )
    fields: List[MetaClassFieldParam] = Field(
        title="子类属性数组"
    )


class AttrParam(BaseModel):
    attr_name: Optional[str] = Field(
        title="属性名称",
        description="可选存在时生成内容为attr_name=attr_value, 不存在时是attr_value"
    )
    attr_value: str = Field(
        title="属性值"
    )


class FieldParam(BaseModel):
    optional: bool = Field(
        title="字段是否可选"
    )
    field_name: str = Field(
        title="字段名称"
    )
    field_type: str = Field(
        title="字段类型"
    )
    attrs: List[AttrParam] = Field(
        title="属性列表"
    )


class SchemaClassParam(BaseModel):
    name: str = Field(
        title="类名"
    )
    parent_class: str = Field(
        title="父类名"
    )
    is_pass: bool = Field(
        title="是否跳过"
    )
    fields: List[FieldParam] = Field(
        title="字段数组"
    )
    meta_class: Optional[MetaClassParam] = Field(
        None,
        title="子类"
    )


class FormParam(BaseParam):
    schema_classes: List[SchemaClassParam] = Field(
        title="参数类列表"
    )
