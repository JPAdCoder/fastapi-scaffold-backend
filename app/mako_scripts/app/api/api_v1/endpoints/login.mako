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

@router.post("/login/access-token", response_model=schemas.Token, summary="获取用户access_token")
async def login_access_token(
        db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests \n
    :param db: database Session object \n
    :param form_data: login form data: username password \n
    :return: dict type access_token \n
    """
    user_out = crud.user.authenticate(
        db, name=form_data.username, password=form_data.password
    )
    if not user_out:
        raise HTTPException(status_code=400, detail="用户名或密码错误🤔")
    elif not crud.user.is_active(user_out):
        raise HTTPException(status_code=400, detail="用户状态异常,请联系管理员")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # 获取权限路径
    if user_out.role_id is None:
        raise HTTPException(status_code=400, detail="用户未分配角色")
    scopes = crud.crud_role_auth_rels.role_auth_rels \
        .get_auth_by_role_id(db=db, role_id=user_out.role_id)
    return {
        "access_token": security.create_access_token(
            user_out.id, scopes, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }