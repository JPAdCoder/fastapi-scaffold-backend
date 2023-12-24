from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict


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
    sub: Optional[int] = Field(
        None,
        description="",
        title=""
    )
    scopes: List = Field(
        description="",
        title="权限路径范围"
    )
