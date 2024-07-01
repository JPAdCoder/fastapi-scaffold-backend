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


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate, UserPage]):
    query_params = {
        "id": "User.id == user.id",
        "name": "User.name == user.name",
        "role_id": "User.role_id == user.role_id"
    }

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """
        创建用户
        :param db: 数据库连接对象 \n
        :param obj_in: 创建用户对应的Pydantic对象 \n
        :return: User 类型对象 \n
        """
        db_obj = User(
            id=uuid1().hex,
            name=obj_in.name,
            hashed_password=get_password_hash(obj_in.password),
            role_id=obj_in.role_id,
            is_superuser=obj_in.is_superuser,
            division_id=obj_in.division_id
        )
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(self, db: Session, *, db_obj: User, obj_in: UserUpdate | Dict[str, Any]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        if 'password' in update_data.keys():
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    @staticmethod
    def is_active(user_in: User) -> bool:
        return user_in.is_active

    @staticmethod
    def is_superuser(user_in: User) -> bool:
        return user_in.is_superuser

    @staticmethod
    def get_by_name(db: Session, *, name: str) -> Optional[User]:
        return db.query(User).filter(User.name == name).first()

    def get_users_search(self, db: Session, *, skip: int = 0, limit: int = 100, name_like: str = "") -> UserPage:
        if limit == -1:
            data = db.query(User).filter(User.name.like('%{}%'.format(name_like))).all()
        else:
            data = db.query(User).filter(User.name.like('%{}%'.format(name_like))).offset(skip).limit(limit).all()
        return UserPage(
            data=data,
            total=self.get_users_search_count(db=db, name_like=name_like)
        )

    def authenticate(self, db: Session, *, name: str, password: str) -> Optional[User]:
        user_out = self.get_by_name(db, name=name)
        if not user_out:
            return None
        if not verify_password(password, user_out.hashed_password):
            return None
        return user_out

    @staticmethod
    def get_users_search_count(db: Session, *, name_like: str = "") -> int:
        return db.query(func.count(User.id)).filter(User.name.like('%{}%'.format(name_like))).scalar()

    def get_users_by_filter_count(self, db: Session, user_req: UserBase = None):
        condition_str = ''
        for param in self.query_params.keys():
            if eval('user_req.%s == None' % param):
                continue
            condition_str += self.query_params[param] + ','
        # 截取掉最后一个条件的逗号
        if len(condition_str) > 1:
            condition_str = condition_str[:-1]
        return eval("db.query(func.count(Auth.id)).filter({}).scalar()".format(condition_str))


user = CRUDUser(User, UserPage)