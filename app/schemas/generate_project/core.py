# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 14:54
Author:     AdCoder
Email:      17647309108@163com
"""
from app.schemas.base import FileBaseParam
from pydantic import BaseModel, Field
from typing import List
import secrets
from app.core.config import settings


class APIConfig(BaseModel):
    api_v1_str: str = Field(
        settings.API_V1_STR,
        title="API接口路径"
    )
    openapi_json_url: str = Field(
        settings.OPENAPI_JSON_URL,
        title="openapi.json文件路径"
    )
    openapi_doc_url: str = Field(
        settings.OPENAPI_DOC_URL,
        title="doc文档路径"
    )
    openapi_redoc_url: str = Field(
        settings.OPENAPI_REDOC_URL,
        title="redoc文档路径"
    )
    server_host: str = Field(
        settings.SERVER_HOST,
        title="API 服务器host"
    )
    server_port: int = Field(
        settings.SERVER_PORT,
        title="API 服务器端口"
    )
    secret_key: str | None = Field(
        settings.SECRET_KEY,
        title="token加密key"
    )
    project_name: str = Field(
        settings.PROJECT_NAME,
        title="doc文档显示项目名称"
    )
    access_token_expire_minutes: int = Field(
        settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        title="token过期时间"
    )
    backend_cors_origins: str = Field(
        str(settings.BACKEND_CORS_ORIGINS),
        title="跨域请求地址白名单"
    )


class DatabaseConfig(BaseModel):
    database_host: str = Field(
        settings.POSTGRES_SERVER,
        title="数据库host"
    )
    database_port: int = Field(
        settings.POSTGRES_PORT,
        title="数据库端口"
    )
    database_user: str = Field(
        settings.POSTGRES_USER,
        title="数据库用户名"
    )
    database_password: str = Field(
        settings.POSTGRES_PASSWORD,
        title="数据库密码"
    )
    database_db: str = Field(
        settings.POSTGRES_DB,
        title="数据库名称"
    )
    sqlalchemy_database_url: str = Field(
        settings.SQLALCHEMY_DATABASE_URL,
        title="sqlalchemy数据库连接字符串"
    )


class MinIOConfig(BaseModel):
    minio_host: str = Field(
        settings.MINIO_HOST,
        title="minio服务器host"
    )
    minio_port: int = Field(
        settings.MINIO_PORT,
        title="minio端口"
    )
    minio_bucket: str = Field(
        settings.MINIO_BUCKET,
        title="minio存储bucket名称"
    )


class GeneralConfig(BaseModel):
    app_path: str = Field(
        settings.APP_PATH,
        title="app根路径"
    )
    statics_file_directory: str = Field(
        "{}/statics".format(settings.APP_PATH),
        title="静态资源文件路径"
    )


class ConfigFileParam(FileBaseParam):
    pass


class CoreParam(BaseModel):
    config_file_param: ConfigFileParam = Field(
        title="core模块"
    )
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
