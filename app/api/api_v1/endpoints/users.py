from fastapi import APIRouter, Depends, HTTPException, Security, Query
from app import crud, schemas, models
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.api import deps
from typing import Any

router = APIRouter()


@router.get("/users", response_model=schemas.UserPage, summary="获取分页用户信息")
async def get_users(
        db: Session = Depends(deps.get_db),
        skip: int = Query(0, title="分页中当前分页需要跳过的数据个数", description="(当前分页数 - 1) x 每页数据个数"),
        limit: int = Query(10, title="分页中每页数据个数"),
        current_user: models.User = Security(deps.get_current_user, scopes=["/users"])
) -> Any:
    """
    获取多个用户
    :param db: \n
    :param skip: \n
    :param limit: \n
    :param current_user: \n
    :return:
    """
    return crud.user.get_multi(db, skip=skip, limit=limit)


@router.get("/user/{user_id}", response_model=schemas.User, summary="根据用户id获取用户信息")
async def get_user_by_id(
        user_id: str,
        current_user: models.User = Security(deps.get_current_user, scopes=["user/{user_id}"]),
        db: Session = Depends(deps.get_db)
) -> Any:
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    return user


@router.get("/users/search", response_model=schemas.UserPage, summary="根据用户名称搜索分页用户信息")
async def get_users_search(
        db: Session = Depends(deps.get_db),
        skip: int = Query(0, title="分页中当前分页需要跳过的数据个数", description="(当前分页数 - 1) x 每页数据个数"),
        limit: int = Query(10, title="分页中每页数据个数"),
        name_like: str = "",
        current_user: models.User = Security(deps.get_current_user, scopes=["/users/search"])
) -> Any:
    return crud.user.get_users_search(db, skip=skip, limit=limit, name_like=name_like)


@router.get("/user/me", response_model=schemas.User, summary="当前用户获取用户信息")
async def read_user_me(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Security(deps.get_current_user, scopes=["/user/me"])
) -> Any:
    return current_user


@router.post("/user", response_model=schemas.User, summary="创建用户")
async def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate,
        current_user: models.User = Security(deps.get_current_user, scopes=["/user"])
) -> Any:
    """
    :param db: \n
    :param user_in:  \n
    :param current_user:  \n
    :return:
    """
    user = crud.user.get_by_name(db, name=user_in.name)
    if user:
        raise HTTPException(
            status_code=400,
            detail="用户已存在"
        )
    return crud.user.create(db, obj_in=user_in)


@router.put("/user/{user_id}", response_model=schemas.User, summary="根据用户id更新用户信息")
async def update_user(
        *,
        db: Session = Depends(deps.get_db),
        user_id: str,
        user_in: schemas.UserUpdate,
        current_user: models.User = Security(deps.get_current_user, scopes=["/user/{user_id}"])
) -> Any:
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在"
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user


@router.delete("/user/delete/{user_id}", response_model=schemas.User, summary="根据用户id删除用户")
async def delete_user(
        *,
        db: Session = Depends(deps.get_db),
        user_id: str,
        current_user: models.User = Security(deps.get_current_user, scopes=["/user/delete/{user_id}"])
) -> Any:
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在"
        )
    user_in = schemas.UserUpdate(is_active=False)

    return crud.user.update(db, db_obj=user, obj_in=user_in)
