# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/16 15:55
Author:     AdCoder
Email:      17647309108@163com
"""
from typing import List
from pydantic import BaseModel, Field

import secrets


class APIConfig(BaseModel):
    api_v1_str: str = Field(
        "/generate/api/v1",
        title="API接口路径"
    )
    openapi_json_url: str = Field(
        "/generate/api/v1/openapi.json",
        title="openapi.json文件路径"
    )
    openapi_doc_url: str = Field(
        "/generate/api/v1/docs",
        title="doc文档路径"
    )
    openapi_redoc_url: str = Field(
        "/generate/api/v1/redoc",
        title="redoc文档路径"
    )
    server_host: str = Field(
        "0.0.0.0",
        title="API 服务器host"
    )
    server_port: int = Field(
        80,
        title="API 服务器端口"
    )
    secret_key: str | None = Field(
        secrets.token_urlsafe(32),
        title="token加密key"
    )
    project_name: str = Field(
        "FastAPI通用接口生成接口文档",
        title="doc文档显示项目名称"
    )
    access_token_expire_minutes: int = Field(
        60 * 24 * 8,
        title="token过期时间"
    )
    backend_cors_origins: str = Field(
        "['*']",
        title="跨域请求地址白名单"
    )


class DatabaseConfig(BaseModel):
    database_host: str = Field(
        "192.168.31.29",
        title="数据库host"
    )
    database_port: int = Field(
        54334,
        title="数据库端口"
    )
    database_user: str = Field(
        "postgres",
        title="数据库用户名"
    )
    database_password: str = Field(
        "96241158a0",
        title="数据库密码"
    )
    database_db: str = Field(
        "fastapi-generate",
        title="数据库名称"
    )
    sqlalchemy_database_url: str = Field(
        "postgresql://{}:{}@{}:{}/{}".format(
            database_user, database_password, database_host,
            database_port, database_db
        ),
        title="sqlalchemy数据库连接字符串"
    )


class MinIOConfig(BaseModel):
    minio_host: str = Field(
        "192.168.31.29",
        title="minio服务器host"
    )
    minio_port: int = Field(
        4000,
        title="minio端口"
    )
    minio_bucket: str = Field(
        "fastapi-generate",
        title="minio存储bucket名称"
    )


class GeneralConfig(BaseModel):
    app_path: str = Field(
        "/Users/adcoder/PycharmProjects/generate-fastapi-be/app",
        title="app根路径"
    )
    statics_file_directory: str = Field(
        "{}/statics".format(app_path),
        title="静态资源文件路径"
    )


class CoreFileParam(BaseModel):
    core_file_name: str = Field(
        "config",
        title="core文件名"
    )
    merged_import_pkg_list: List[dict] = Field(
        title="导入包列表"
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


class DBInitFileParam(BaseModel):
    author: str = Field(
        "AdCoder"
    )
    email: str = Field(
        "17647309108@163.com"
    )
    merged_import_pkg_list: List[dict] = Field(
        title="导入包列表"
    )


class DBBaseFileParam(BaseModel):
    author: str = Field(
        "AdCoder"
    )
    email: str = Field(
        "17647309108@163.com"
    )
    merged_import_pkg_list: List[dict] = Field(
        title="导入包列表"
    )


class DBBaseClassFileParam(BaseModel):
    author: str = Field(
        "AdCoder"
    )
    email: str = Field(
        "17647309108@163.com"
    )
    merged_import_pkg_list: List[dict] = Field(
        title="导入包列表"
    )


class EngineParam(BaseModel):
    pool_pre_ping: str = Field(
        "True",
        title="pool_pre_ping"
    )
    pool_recycle: int = Field(
        3600,
        title="pool_recycle"
    )
    pool_size: int = Field(
        10,
        title="pool_size"
    )


class SessionLocal(BaseModel):
    autocommit: str = Field(
        "False",
        title="自动commit"
    )
    autoflush: str = Field(
        "False",
        title="自动刷新"
    )
    expire_on_commit: str = Field(
        "True",
        title="超时自动提交"
    )


class DBSessionFileParam(BaseModel):
    author: str = Field(
        "AdCoder"
    )
    email: str = Field(
        "17647309108@163.com"
    )
    merged_import_pkg_list: List[dict] = Field(
        title="导入包列表"
    )
    engine: EngineParam = Field(
        title="engine对象"
    )
    session_local: SessionLocal = Field(
        title="session_local对象"
    )


class DBParam(BaseModel):
    init_file_param: DBInitFileParam = Field(
        title="DB模块init文件参数"
    )
    base_file_param: DBBaseFileParam = Field(
        title="DB模块base文件参数"
    )
    base_class_file_param: DBBaseClassFileParam = Field(
        title="DB模块base_class文件参数"
    )
    session_file_param: DBSessionFileParam = Field(
        title="DB模块session文件参数"
    )


class ProjectParam(BaseModel):
    name: str = Field(
        "Generate",
        title="项目名称"
    )
    author: str = Field(
        "AdCoder",
        title="作者"
    )
    email: str = Field(
        "17647309108@163.com",
        title="邮箱"
    )


class FormParam(ProjectParam):
    core_param: CoreFileParam = Field(
        title="core文件配置参数"
    )
    db_param: DBParam = Field(
        title="db模块配置参数"
    )
