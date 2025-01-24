# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 22:43
Author:     AdCoder
Email:      17647309108@163com
"""
from app.schemas.base import FileBaseParam
from pydantic import BaseModel, Field


class ModelsInitFileParam(FileBaseParam):
    pass


class ModelsUserFileParam(FileBaseParam):
    pass


class ModelsRoleFileParam(FileBaseParam):
    pass


class ModelsAuthFileParam(FileBaseParam):
    pass


class ModelsRoleAuthRelsFileParam(FileBaseParam):
    pass


class ModelsParam(BaseModel):
    init_file_param: ModelsInitFileParam = Field(
        title="models模块init文件参数"
    )
    user_file_param: ModelsUserFileParam = Field(
        title="models模块user文件参数"
    )
    role_file_param: ModelsRoleFileParam = Field(
        title="models模块role文件参数"
    )
    auth_file_param: ModelsAuthFileParam = Field(
        title="models模块auth文件参数"
    )
    role_auth_rels_file_param: ModelsRoleAuthRelsFileParam = Field(
        title="models模块role_auth_rels文件参数"
    )
