"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in merged_import_pkg_list:
% if v["from"]:
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor


class Token(BaseModel):
    access_token: str = Field(
        description="",
        title="权限token"
    )
    token_type: str = Field(
        description="",
        title="token类型"
    )
    model_config = ConfigDict(
        protected_namespaces=()
    )


class TokenPayload(BaseModel):
    sub: Optional[str] = Field(
        None,
        description="",
        title=""
    )
    scopes: List = Field(
        description="",
        title="权限路径范围"
    )