# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 14:54
Author:     AdCoder
Email:      17647309108@163com
"""
from app.schemas.base import FileBaseParam
from pydantic import BaseModel, Field


class SchemasInitFileParam(FileBaseParam):
    pass


class SchemasTokenFileParam(FileBaseParam):
    pass


class SchemasAuthFileParam(FileBaseParam):
    pass


class SchemasRoleFileParam(FileBaseParam):
    pass


class SchemasUserFileParam(FileBaseParam):
    pass


class SchemasRoleAuthRelsFileParam(FileBaseParam):
    pass


class SchemasParam(BaseModel):
    init_file_param: SchemasInitFileParam = Field(
        title="schemas模块init文件参数"
    )
    token_file_param: SchemasTokenFileParam = Field(
        title="schemas模块token文件参数"
    )
    auth_file_param: SchemasAuthFileParam = Field(
        title="schemas模块auth文件参数"
    )
    role_file_param: SchemasRoleFileParam = Field(
        title="schemas模块role文件参数"
    )
    user_file_param: SchemasUserFileParam = Field(
        title="schemas模块user文件参数"
    )
    role_auth_rels_file_param: SchemasRoleAuthRelsFileParam = Field(
        title="schemas模块role_auth_rels文件参数"
    )
