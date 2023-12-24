# coding=utf8
"""
Time:   2022/2/15 8:54 AM
Author: AdCoder
Email:  17647309108@163.com
"""
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class RoleBase(BaseModel):
    id: Optional[str] = Field(
        None,
        description="",
        title="角色id"
    )
    name: Optional[str] = Field(
        None,
        description="",
        title="角色名称"
    )
    is_active: Optional[bool] = Field(
        True,
        description="",
        title="是否启用"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class RoleCreate(RoleBase):
    name: str = Field(
        description="",
        title="角色名称"
    )


class RoleUpdate(RoleBase):
    pass


class RoleInDBBase(RoleBase):
    id: Optional[str] = Field(
        None,
        description="",
        title="角色id"
    )

    class Config:
        from_attributes = True


class Role(RoleInDBBase):
    pass


class RoleInDB(RoleInDBBase):
    pass


class RolePage(BaseModel):
    data: List[Role] = Field(
        title="当前分页的角色列表"
    )
    total: int = Field(
        title="符合分页查询条件的对象总数"
    )
