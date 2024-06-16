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


def get_${model_name_lower_case}_rep(db_obj: ${model_name}):
    rep_obj = ${schema_rep_model}(
        **jsonable_encoder(db_obj)
    )
    return rep_obj


@router.get("/${model_name_lower_case}/multi",
            response_model=${schema_page_rep_model},
            summary="分页获取${model_name_comment}")
def get_${model_name_lower_case}s(
        db: Session = Depends(deps.get_db),
        skip: int = Query(0, title="分页中当前分页需要跳过的数据个数", description="(当前分页数 - 1) x 每页数据个数"),
        limit: int = Query(10, title="分页中每页数据个数"),
        current_user: models.User = Security(deps.get_current_user, scopes=["/${model_name_lower_case}/multi"])
) -> Any:
    ${model_name_lower_case}_page = crud.${model_name_lower_case}.get_multi(db, skip=skip, limit=limit)
    if not ${model_name_lower_case}_page:
        raise HTTPException(status_code=404, detail="没有符合条件的${model_name_comment}")
    rep_data = []
    for v in ${model_name_lower_case}_page.data:
        rep_data.append(get_${model_name_lower_case}_rep(v))
    return ${schema_page_rep_model}(
        data=rep_data,
        total=${model_name_lower_case}_page.total
    )


@router.get("/${model_name_lower_case}/{${model_name_lower_case}_id}",
            response_model=${schema_rep_model},
            summary="根据id获取${model_name_comment}")
def get_${model_name_lower_case}_by_id(
        ${model_name_lower_case}_id: str,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Security(deps.get_current_user,
                                             scopes=["/${model_name_lower_case}/{${model_name_lower_case}_id}"])
) -> Any:
    ${model_name_lower_case} = crud.${model_name_lower_case}.get(db, id=${model_name_lower_case}_id)
    if not ${model_name_lower_case}:
        raise HTTPException(status_code=404, detail="${model_name_comment}不存在")
    return get_${model_name_lower_case}_rep(${model_name_lower_case})


@router.put("/${model_name_lower_case}/update",
            response_model=${schema_rep_model},
            summary="根据${model_name_comment}id更新${model_name_comment}")
def update_${model_name_lower_case}(
        ${model_name_lower_case}_in: ${schema_update_model},
        db: Session = Depends(deps.get_db),
        current_user: models.User = Security(deps.get_current_user,
                                             scopes=["${model_name_lower_case}/update"])
) -> Any:
    ${model_name_lower_case} = crud.${model_name_lower_case}.get(db, id=${model_name_lower_case}_in.id)
    if not ${model_name_lower_case}:
        raise HTTPException(
            status_code=404,
            detail="${model_name_comment}不存在"
        )
    return get_${model_name_lower_case}_rep(crud.${model_name_lower_case}.update(db=db, db_obj=${model_name_lower_case}, obj_in=${model_name_lower_case}_in))


@router.delete("/${model_name_lower_case}/remove/{id}",
               response_model=${schema_rep_model},
               summary="根据${model_name_comment}id移除${model_name_comment}(彻底删除)")
def delete_${model_name_lower_case}(
        id: str,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Security(deps.get_current_user,
                                             scopes=["/${model_name_lower_case}/remove/{id}"])
) -> Any:
    ${model_name_lower_case} = crud.${model_name_lower_case}.remove(db=db, id=id)
    if not ${model_name_lower_case}:
        raise HTTPException(
            status_code=404,
            detail="${model_name_comment}不存在"
        )
    return get_${model_name_lower_case}_rep(${model_name_lower_case})


@router.delete("/${model_name_lower_case}/delete/{id}",
               response_model=${schema_rep_model},
               summary="根据${model_name_comment}id删除${model_name_comment}")
def delete_${model_name_lower_case}(
        id: str,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Security(deps.get_current_user,
                                             scopes=["/${model_name_lower_case}/delete/{id}"])
) -> Any:
    ${model_name_lower_case} = crud.${model_name_lower_case}.get(db, id)
    if not ${model_name_lower_case}:
        raise HTTPException(
            status_code=404,
            detail="${model_name_comment}不存在"
        )
    return crud.${model_name_lower_case}.update(db=db,db_obj=${model_name_lower_case},obj_in=${schema_update_model}(is_active=False,id=id))


@router.post("/${model_name_lower_case}/add",
             response_model=${schema_rep_model},
             summary="添加${model_name_comment}信息")
def add_${model_name_lower_case}(
        ${model_name_lower_case}_in: ${schema_create_model},
        db: Session = Depends(deps.get_db),
        current_user: models.User = Security(deps.get_current_user,
                                             scopes=["/${model_name_lower_case}/add"])
) -> Any:
    return crud.${model_name_lower_case}.create(db, obj_in=${model_name_lower_case}_in)



