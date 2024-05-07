from app.schemas.auth import AuthCreate, AuthUpdate, AuthBase, AuthPage
from typing import Any, Dict, Union
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.auth import Auth
from sqlalchemy import func
from uuid import uuid1


class CRUDAuth(CRUDBase[Auth, AuthCreate, AuthUpdate, AuthPage]):
    query_params = {
        "id": "Auth.id == auth.id",
        "name": "Auth.name == auth.name"
    }

    def create(self, db: Session, *, obj_in: AuthCreate) -> Auth:
        """
        创建权限 \n
        :param db: 数据库连接对象 \n
        :param obj_in: 创建权限对应的Pydantic对象 \n
        :return: Auth  类型对象 \n
        """
        db_obj = Auth(
            id=uuid1().hex,
            name=obj_in.name,
            path=obj_in.path,
            is_active=obj_in.is_active
        )
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(self, db: Session, *, db_obj: Auth, obj_in: Union[AuthUpdate, Dict[str, Any]]) -> Auth:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    @staticmethod
    def get_by_name(db: Session, name: str) -> Auth | None:
        return db.query(Auth).filter(Auth.name == name).first()

    def get_auths_search(self, db: Session, *, skip: int = 0, limit: int = 100, name_like: str = "") \
            -> AuthPage:
        if limit == -1:
            data = db.query(Auth).filter(Auth.name.like('%{}%'.format(name_like))).all()
        else:
            data = db.query(Auth).filter(Auth.name.like('%{}%'.format(name_like))).offset(skip).limit(limit).all()
        return AuthPage(
            data=data,
            total=self.get_auths_search_count(db=db, name_like=name_like)
        )

    def get_auths_by_filter(self, db: Session, skip: int = 0,
                            limit: int = 100, auth: AuthBase = None):
        condition_str = ''
        for param in self.query_params.keys():
            if eval('auth.%s == None' % param):
                continue
            condition_str += self.query_params[param] + ','
        # 截取掉最后一个条件的逗号
        if len(condition_str) > 1:
            condition_str = condition_str[:-1]
        if limit == -1:
            data = eval("db.query(Auth).filter({}).all()".format(condition_str))
        else:
            data = eval("db.query(Auth).filter({}).offset({}).limit({}).all()".format(condition_str, skip, limit))
        return AuthPage(
            data=data,
            total=self.get_auths_by_filter_count()
        )

    @staticmethod
    def get_auths_search_count(db: Session, *, name_like: str = "") \
            -> int:
        return db.query(func.count(Auth.id)).filter(Auth.name.like('%{}%'.format(name_like))).scalar()

    def get_auths_by_filter_count(self):
        condition_str = ''
        for param in self.query_params.keys():
            if eval('auth.%s == None' % param):
                continue
            condition_str += self.query_params[param] + ','
        # 截取掉最后一个条件的逗号
        if len(condition_str) > 1:
            condition_str = condition_str[:-1]
        return eval("db.query(func.count(Auth.id)).filter({}).scalar()".format(condition_str))


auth = CRUDAuth(Auth, AuthPage)
