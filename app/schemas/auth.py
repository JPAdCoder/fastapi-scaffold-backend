# coding=utf8
"""
Time:   2022/2/15 8:57 AM
Author: AdCoder
Email:  17647309108@163.com
"""
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class AuthBase(BaseModel):
    id: Optional[str] = Field(
        None,
        description="",
        title="权限id"
    )
    name: Optional[str] = Field(
        None,
        description="",
        title="权限名称"
    )
    path: Optional[str] = Field(
        None,
        description="",
        title="权限路径"
    )
    is_active: Optional[bool] = Field(
        True,
        description="",
        title="是否启用"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class AuthCreate(AuthBase):
    name: str = Field(
        description="",
        title="权限名称"
    )
    path: str = Field(
        description="",
        title="权限路径"
    )


class AuthUpdate(AuthBase):
    pass


class AuthInDBBase(AuthBase):
    id: Optional[str] = Field(
        None,
        description="",
        title="权限id"
    )

    class Config:
        from_attributes = True


class Auth(AuthInDBBase):
    pass


class AuthInDB(AuthInDBBase):
    pass


class AuthPage(BaseModel):
    data: List[Auth] = Field(
        title="当前分页的权限列表"
    )
    total: int = Field(
        title="符合分页查询条件的对象总数"
    )
