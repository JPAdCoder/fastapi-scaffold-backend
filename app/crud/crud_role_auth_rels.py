from app.schemas.role_auth_rels import RoleAuthRelsCreate, RoleAuthRelsUpdate, RoleAuthRelsBase, RoleAuthRelsPage
from app.models.role_auth_rels import RoleAuthRels
from typing import Any, Dict, Union
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.auth import Auth
from sqlalchemy import func
from uuid import uuid1


class CRUDRoleAuthRels(CRUDBase[RoleAuthRels, RoleAuthRelsCreate, RoleAuthRelsUpdate, RoleAuthRelsPage]):
    query_params = {
        "id": "RoleAuthRels.id == role_auth_rels.id",
        "role_id": "RoleAuthRels.role_id == role_auth_rels.role_id",
        "auth_id": "RoleAuthRels.auth_id == role_auth_rels.auth_id"
    }

    def create(self, db: Session, *, obj_in: RoleAuthRelsCreate) -> RoleAuthRels:
        """
        创建角色权限关系 \n
        :param db:  \n
        :param obj_in: \n
        :return:  \n
        """
        db_obj = RoleAuthRels(
            id=uuid1().hex,
            role_id=obj_in.role_id,
            auth_id=obj_in.auth_id
        )
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(self, db: Session, *, db_obj: RoleAuthRels,
               obj_in: Union[RoleAuthRelsUpdate, Dict[str, Any]]) -> RoleAuthRels:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_role_auth_rels_by_filter(self, db: Session, skip: int = 0,
                                     limit: int = 100, role_auth_rels_req: RoleAuthRelsBase = None):
        condition_str = ''
        for param in self.query_params.keys():
            if eval('role_auth_rels.%s == None' % param):
                continue
            condition_str += self.query_params[param] + ','
        # 截取掉最后一个条件的逗号
        if len(condition_str) > 1:
            condition_str = condition_str[:-1]
        if limit == -1:
            data = eval("db.query(RoleAuthRels).filter({}).all()".format(condition_str))
        else:
            data = eval(
                "db.query(RoleAuthRels).filter({}).offset({}).limit({}).all()".format(condition_str, skip, limit))
        return RoleAuthRelsPage(
            data=data,
            total=self.get_role_auth_rels_by_filter_count(db, role_auth_rels_req)
        )

    @staticmethod
    def get_auth_by_role_id(db: Session, role_id: str):
        result = db.query(RoleAuthRels.id, Auth.path) \
            .outerjoin(Auth, RoleAuthRels.auth_id == Auth.id) \
            .filter(RoleAuthRels.role_id == role_id) \
            .all()
        return [v.path for v in result]

    def get_role_auth_rels_by_filter_count(self, db: Session, role_auth_rels_req: RoleAuthRelsBase = None):
        conditions = []
        for param in self.query_params.keys():
            if getattr(role_auth_rels_req, param) is None:
                continue
            conditions.append(self.query_params[param])
        # 条件list判空
        if not conditions:
            return db.query(func.count(RoleAuthRels.id)).scalar()
        return db.query(func.count(RoleAuthRels.id)).filter(*conditions).scalar()


role_auth_rels = CRUDRoleAuthRels(RoleAuthRels, RoleAuthRelsPage)
