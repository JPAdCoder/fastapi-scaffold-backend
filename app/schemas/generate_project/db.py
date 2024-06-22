# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 14:53
Author:     AdCoder
Email:      17647309108@163com
"""

from app.schemas.file_param import FileBaseParam
from pydantic import BaseModel, Field


class DBInitFileParam(FileBaseParam):
    pass


class DBBaseFileParam(FileBaseParam):
    pass


class DBBaseClassFileParam(FileBaseParam):
    pass


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


class DBSessionFileParam(FileBaseParam):
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
