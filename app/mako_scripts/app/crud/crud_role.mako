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


class CRUDRole(CRUDBase[Role, RoleCreate, RoleUpdate, RolePage]):
    query_params = {
        "id": "Role.id == role.id",
        "name": "Role.name == role.name"
    }

    def create(self, db: Session, *, obj_in: RoleCreate) -> Role:
        """
        创建角色 \n
        :param db:  \n
        :param obj_in: \n
        :return:  \n
        """
        db_obj = Role(
            id=uuid1().hex,
            name=obj_in.name
        )
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(self, db: Session, *, db_obj: Role, obj_in: RoleUpdate | Dict[str, Any]) -> Role:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    @staticmethod
    def get_by_name(db: Session, name: str) -> Optional[Role]:
        return db.query(Role).filter(Role.name == name).first()

    def get_roles_search(self, db: Session, *, skip: int = 0, limit: int = 100, name_like: str = "") -> RolePage:
        if limit == -1:
            data = db.query(Role).filter(Role.name.like('%{}%'.format(name_like))).all()
        else:
            data = db.query(Role).filter(Role.name.like('%{}%'.format(name_like))).offset(skip).limit(limit).all()
        return RolePage(
            data=data,
            total=self.get_roles_search_count(db=db, name_like=name_like)
        )

    def get_roles_by_filter(self, db: Session, skip: int = 0,
                            limit: int = 100, role: RoleBase = None):
        condition_str = ''
        for param in self.query_params.keys():
            if eval('role.%s == None' % param):
                continue
            condition_str += self.query_params[param] + ','
        # 截取掉最后一个条件的逗号
        if len(condition_str) > 1:
            condition_str = condition_str[:-1]
        if limit == -1:
            data = eval("db.query(Role).filter({}).all()".format(condition_str))
        else:
            data = eval("db.query(Role).filter({}).offset({}).limit({}).all()".format(condition_str, skip, limit))
        return RolePage(
            data=data,
            total=self.get_roles_by_filter_count(db, role)
        )

    @staticmethod
    def get_roles_search_count(db: Session, *, skip: int = 0, limit: int = 100, name_like: str = "") -> int:
        return db.query(func.count(Role.id)).filter(Role.name.like('%{}%'.format(name_like))).scalar()

    def get_roles_by_filter_count(self, db: Session, role: RoleBase = None):
        condition_str = ''
        for param in self.query_params.keys():
            if eval('role.%s == None' % param):
                continue
            condition_str += self.query_params[param] + ','
        # 截取掉最后一个条件的逗号
        if len(condition_str) > 1:
            condition_str = condition_str[:-1]
        return eval("db.query(func.count(Role.id)).filter({}).scalar()".format(condition_str))


role = CRUDRole(Role, RolePage)