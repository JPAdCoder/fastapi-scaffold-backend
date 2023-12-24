# coding=utf8
"""
Time:   2022/2/15 8:54 AM
Author: AdCoder
Email:  17647309108@163.com
"""
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class RoleAuthRelsBase(BaseModel):
    id: Optional[str] = Field(
        None,
        description="",
        title="角色权限关系id"
    )
    role_id: Optional[str] = Field(
        None,
        description="",
        title="角色id"
    )
    auth_id: Optional[str] = Field(
        None,
        description="",
        title="权限id"
    )
    is_active: Optional[bool] = Field(
        True,
        description="",
        title="是否启用"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class RoleAuthRelsCreate(RoleAuthRelsBase):
    role_id: str = Field(
        description="",
        title="角色id"
    )
    auth_id: str = Field(
        description="",
        title="权限id"
    )


class RoleAuthRelsUpdate(RoleAuthRelsBase):
    pass


class RoleAuthRelsInDBBase(RoleAuthRelsBase):
    id: Optional[str] = Field(
        None,
        description="",
        title="角色权限关系id"
    )

    class Config:
        from_attributes = True


class RoleAuthRels(RoleAuthRelsInDBBase):
    pass


class RoleAuthRelsPage(BaseModel):
    data: List[RoleAuthRels] = Field(
        title="当前分页的角色权限关系列表"
    )
    total: int = Field(
        title="符合分页查询条件的对象总数"
    )
