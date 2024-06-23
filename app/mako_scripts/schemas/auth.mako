"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in core_param["config_file_param"]["merged_import_pkg_list"]:
% if v["from"] != "null":
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor


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