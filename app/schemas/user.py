from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    division_id: Optional[str] = Field(
        None,
        description="",
        title="部门id"
    )
    name: Optional[str] = Field(
        None,
        description="",
        title="用户名"
    )
    role_id: Optional[str] = Field(
        None,
        description="",
        title="角色id"
    )
    is_active: Optional[bool] = Field(
        True,
        description="",
        title="是否启用"
    )
    is_superuser: Optional[bool] = Field(
        False,
        description="",
        title="是否超级管理员"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class UserCreate(UserBase):
    division_id: str = Field(
        "",
        description="",
        title="部门id"
    )
    name: str = Field(
        description="",
        title="用户名"
    )
    role_id: str = Field(
        description="",
        title="角色id"
    )
    password: str = Field(
        description="",
        title="密码"
    )


class UserUpdate(UserBase):
    password: Optional[str] = Field(
        None,
        description="",
        title="密码"
    )


class UserInDBBase(UserBase):
    id: Optional[str] = Field(
        None,
        description="",
        title="用户id"
    )

    class Config:
        from_attributes = True


class User(UserInDBBase):
    role_name: str = Field(
        None,
        description="",
        title="角色名"
    )


class UserInDB(UserInDBBase):
    hashed_password: str


class UserPage(BaseModel):
    data: List[User] = Field(
        title="当前分页的用户列表"
    )
    total: int = Field(
        title="符合分页查询条件的对象总数"
    )


class UserFilterRequest(UserBase):
    id: Optional[str] = Field(
        None,
        title="id"
    )
