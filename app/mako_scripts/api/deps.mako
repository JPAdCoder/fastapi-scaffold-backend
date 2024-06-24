"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in api_param["deps_file_param"]["merged_import_pkg_list"]:
% if v["from"] != "null":
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
        security_scopes: SecurityScopes, db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        for v in security_scopes.scopes:
            logger.debug(v)
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户信息验证错误"
        )
    if len(token_data.scopes) < 1:
        raise HTTPException(status_code=400, detail="用户权限未分配")
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(status_code=403, detail="没有权限")
    user = crud.user.get(db, model_id=str(token_data.sub))
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


def get_current_active_user(
        current_user: models.User = Depends(get_current_user)
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="用户权限不足"
        )
    return current_user


def get_current_active_superuser(
        current_user: models.User = Depends(get_current_user)
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="用户权限不足"
        )
    return current_user