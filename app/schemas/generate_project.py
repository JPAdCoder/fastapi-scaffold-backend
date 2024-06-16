# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/16 15:55
Author:     AdCoder
Email:      17647309108@163com
"""
from typing import List
from pydantic import BaseModel, Field
from app.schemas.base_param import BaseParam


class APIConfig(BaseModel):
    api_v1_str: str = Field(
        title="API接口路径"
    )
    openapi_json_url: str = Field(
        title="openapi.json文件路径"
    )
    openapi_doc_url: str = Field(
        title="doc文档路径"
    )
    openapi_redoc_url: str = Field(
        title="redoc文档路径"
    )
    server_host: str = Field(
        title="API 服务器host"
    )
    server_port: int = Field(
        title="API 服务器端口"
    )
    secret_key: str = Field(
        title="Token加密key"
    )
    project_name: str = Field(
        title="doc文档显示项目名称"
    )
    access_token_expire_minutes: int = Field(
        title="token过期时间"
    )


class DatabaseConfig(BaseModel):
    database_host: str = Field(
        title="数据库host"
    )
    database_port: int = Field(
        title="数据库端口"
    )
    database_user: str = Field(
        title="数据库用户名"
    )
    database_password: str = Field(
        title="数据库密码"
    )
    database_db: str = Field(
        title="数据库名称"
    )
    sqlalchemy_database_url: str = Field(
        title="sqlalchemy数据库连接字符串"
    )


class MinIOConfig(BaseModel):
    minio_host: str = Field(
        title="minio服务器host"
    )
    minio_port: int = Field(
        title="minio端口"
    )
    minio_bucket: str = Field(
        title="minio存储bucket名称"
    )


class GeneralConfig(BaseModel):
    app_path: str = Field(
        title="app根路径"
    )
    statics_file_directory: str = Field(
        title="静态资源文件路径"
    )


class CoreFileParam(BaseModel):
    api_config: APIConfig = Field(
        title="API相关配置"
    )
    database_config: DatabaseConfig = Field(
        title="数据库相关配置"
    )
    minio_config: MinIOConfig = Field(
        title="minio相关配置"
    )
    general_config: GeneralConfig = Field(
        title="通用配置"
    )


class FormParam(BaseParam):
    core_file_param: CoreFileParam = Field(
        title="core文件配置参数"
    )