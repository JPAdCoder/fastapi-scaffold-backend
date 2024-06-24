"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in api_param["api_v1_endpoints_role_file_param"]["merged_import_pkg_list"]:
% if v["from"] != "null":
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor

router = APIRouter()


@router.get("/roles", response_model=schemas.RolePage, summary="根据分页获取多个角色信息")
async def get_roles(
        db: Session = Depends(deps.get_db),
        skip: int = Query(0, title="分页中当前分页需要跳过的数据个数", description="(当前分页数 - 1) x 每页数据个数"),
        limit: int = Query(10, title="分页中每页数据个数"),
        current_user: models.User = Security(deps.get_current_user, scopes=["/roles"])
) -> Any:
    """
    获取多个角色信息 \n
    :param db:  \n
    :param skip:  \n
    :param limit:  \n
    :param current_user:  \n
    :return:  \n
    """
    roles = crud.role.get_multi(db, skip=skip, limit=limit)
    return roles


@router.get("/role/{role_id}", response_model=schemas.Role, summary="根据角色id获取角色信息")
async def get_role_by_id(
        role_id: str,
        current_user: models.User = Security(deps.get_current_user, scopes=["/role/{role_id}"]),
        db: Session = Depends(deps.get_db)
) -> Any:
    role = crud.role.get(db, id=role_id)
    return role


@router.get("/roles/search", response_model=schemas.RolePage, summary="根据角色名搜索分页角色信息")
async def get_roles_search(
        db: Session = Depends(deps.get_db),
        skip: int = Query(0, title="分页中当前分页需要跳过的数据个数", description="(当前分页数 - 1) x 每页数据个数"),
        limit: int = Query(10, title="分页中每页数据个数"),
        name_like: str = "",
        current_user: models.User = Security(deps.get_current_user, scopes=["/roles/search"])
) -> Any:
    return crud.role.get_roles_search(db, skip=skip, limit=limit, name_like=name_like)


@router.post("/role", response_model=schemas.Role, summary="创建角色")
async def create_role(
        *,
        db: Session = Depends(deps.get_db),
        role_in: schemas.RoleCreate,
        current_user: models.Role = Security(deps.get_current_user, scopes=["/role"])
) -> Any:
    """
    创建角色
    :param db:
    :param role_in:
    :param current_user:
    :return:
    """
    role = crud.role.get_by_name(db, role_in.name)
    if role:
        raise HTTPException(
            status_code=400,
            detail="角色已存在"
        )
    return crud.role.create(db, obj_in=role_in)


@router.put("/role/{role_id}", response_model=schemas.Role, summary="根据角色id更新角色")
async def update_role(
        *,
        db: Session = Depends(deps.get_db),
        role_id: str,
        role_in: schemas.RoleUpdate,
        current_user: models.User = Security(deps.get_current_user, scopes=["/role/{role_id}"])
) -> Any:
    role = crud.role.get(db, id=role_id)
    if not role:
        raise HTTPException(
            status_code=404,
            detail="角色不存在"
        )
    role = crud.role.update(db, db_obj=role, obj_in=role_in)
    return role


@router.delete("/role/delete/{role_id}", response_model=schemas.Role, summary="根据角色id删除角色")
async def delete_role(
        *,
        db: Session = Depends(deps.get_db),
        role_id: str,
        current_user: models.Role = Security(deps.get_current_user, scopes=["/role/delete/{role_id}"])
) -> Any:
    role = crud.role.get(db, id=role_id)
    if not role:
        raise HTTPException(
            status_code=404,
            detail="角色不存在"
        )
    role_in = schemas.RoleUpdate(is_active=False)

    return crud.role.update(db, db_obj=role, obj_in=role_in)