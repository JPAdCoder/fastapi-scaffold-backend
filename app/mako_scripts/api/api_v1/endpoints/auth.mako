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


router = APIRouter()


@router.get("/auths", response_model=schemas.AuthPage, summary="分页获取权限")
async def get_auths(
        db: Session = Depends(deps.get_db),
        skip: int = Query(0, title="分页中当前分页需要跳过的数据个数", description="(当前分页数 - 1) x 每页数据个数"),
        limit: int = Query(10, title="分页中每页数据个数"),
        current_user: models.User = Security(deps.get_current_user, scopes=["/auths"])
) -> Any:
    """
    获取多个权限信息 \n
    :param db:  \n
    :param skip: \n
    :param limit: \n
    :param current_user:  \n
    :return:  \n
    """
    auths = crud.auth.get_multi(db, skip=skip, limit=limit)
    return auths


@router.get("/auth/{auth_id}", response_model=schemas.Auth, summary="根据id获取权限")
async def get_auth_by_id(
        auth_id: str,
        current_user: models.User = Security(deps.get_current_user, scopes=["/auth/{auth_id}"]),
        db: Session = Depends(deps.get_db)
) -> Any:
    auth = crud.auth.get(db, id=auth_id)
    if not auth:
        raise HTTPException(status_code=400, detail="权限不存在")
    return auth


@router.get("/auths/search", response_model=schemas.AuthPage, summary="根据权限名分页搜索权限")
async def get_users_search(
        db: Session = Depends(deps.get_db),
        skip: int = Query(0, title="分页中当前分页需要跳过的数据个数", description="(当前分页数 - 1) x 每页数据个数"),
        limit: int = Query(10, title="分页中每页数据个数"),
        name_like: str = "",
        current_user: models.User = Security(deps.get_current_user, scopes=["/auths/search"])
) -> Any:
    return crud.auth.get_auths_search(db, skip=skip, limit=limit, name_like=name_like)


@router.put("/auth/{auth_id}", response_model=schemas.Auth, summary="根据权限id更新权限")
async def update_auth(
        *,
        db: Session = Depends(deps.get_db),
        auth_id: str,
        auth_in: schemas.AuthUpdate,
        current_user: models.User = Security(deps.get_current_user, scopes=["/auth/{auth_id}"])
) -> Any:
    auth = crud.auth.get(db, id=auth_id)
    if not auth:
        raise HTTPException(
            status_code=404,
            detail="权限不存在"
        )
    auth = crud.auth.update(db, db_obj=auth, obj_in=auth_in)
    return auth


@router.delete("/auth/delete/{auth_id}", response_model=schemas.Auth, summary="根据权限id删除权限")
async def delete_auth(
        *,
        db: Session = Depends(deps.get_db),
        auth_id: str,
        current_user: models.Auth = Security(deps.get_current_user, scopes=["/auth/delete/{auth_id}"])
) -> Any:
    auth = crud.auth.get(db, id=auth_id)
    if not auth:
        raise HTTPException(
            status_code=404,
            detail="权限不存在"
        )
    auth_in = schemas.AuthUpdate(is_active=False)

    return crud.auth.update(db, db_obj=auth, obj_in=auth_in)