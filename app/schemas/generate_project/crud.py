# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 14:54
Author:     AdCoder
Email:      17647309108@163com
"""
from app.schemas.base import FileBaseParam
from pydantic import BaseModel, Field


class CRUDInitFileParam(FileBaseParam):
    pass


class CRUDBaseFileParam(FileBaseParam):
    pass


class CRUDAuthFileParam(FileBaseParam):
    pass


class CRUDRoleFileParam(FileBaseParam):
    pass


class CRUDUserFileParam(FileBaseParam):
    pass


class CRUDRoleAuthRelsFileParam(FileBaseParam):
    pass


class CRUDParam(BaseModel):
    init_file_param: CRUDInitFileParam = Field(
        title="crud模块init文件参数"
    )
    base_file_param: CRUDBaseFileParam = Field(
        title="crud模块base文件参数"
    )
    auth_file_param: CRUDAuthFileParam = Field(
        title="crud模块crud_auth文件参数"
    )
    role_file_param: CRUDRoleFileParam = Field(
        title="crud模块crud_role文件参数"
    )
    user_file_param: CRUDUserFileParam = Field(
        title="crud模块crud_user文件参数"
    )
    role_auth_rels_file_param: CRUDRoleAuthRelsFileParam = Field(
        title="crud模块crud_role_auth_rels文件参数"
    )
