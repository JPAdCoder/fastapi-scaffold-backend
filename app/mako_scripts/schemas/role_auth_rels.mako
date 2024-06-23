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
