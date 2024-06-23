# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 14:54
Author:     AdCoder
Email:      17647309108@163com
"""
from app.schemas.file_param import FileBaseParam
from pydantic import BaseModel, Field


class ApiDepsFileParam(FileBaseParam):
    pass


class ApiV1ApiFileParam(FileBaseParam):
    pass


class ApiV1EndPointsUserFileParam(FileBaseParam):
    pass


class ApiV1EndPointsAuthFileParam(FileBaseParam):
    pass


class ApiV1EndPointsRoleFileParam(FileBaseParam):
    pass

class ApiV1EndPointsLoginFileParam(FileBaseParam):
    pass


class ApiParam(FileBaseParam):
    deps_file_param: ApiDepsFileParam = Field(
        title="api模块deps文件参数"
    )
    api_v1_api_file_param: ApiV1ApiFileParam = Field(
        title="api模块中v1版本api.py文件参数"
    )
    api_v1_endpoints_user_file_param: ApiV1EndPointsUserFileParam = Field(
        title="api模块中v1版本endpoints user.py文件参数"
    )
    api_v1_endpoints_role_file_param: ApiV1EndPointsRoleFileParam = Field(
        title="api模块中v1版本endpoints role.py文件参数"
    )
    api_v1_endpoints_auth_file_param: ApiV1EndPointsAuthFileParam = Field(
        title="api模块中v1版本endpoints auth.py文件参数"
    )
    api_v1_endpoints_login_file_param: ApiV1EndPointsLoginFileParam = Field(
        title="api模块v1版本endpoints login.py文件参数"
    )
