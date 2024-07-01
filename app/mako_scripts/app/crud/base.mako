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

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
PageSchemaType = TypeVar("PageSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType, PageSchemaType]):
    def __init__(self, model: Type[ModelType], page_model: Type[PageSchemaType]):
        """
        CRUD object with default_param methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.page_model = page_model

    def get(self, db: Session, model_id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == model_id and self.model.is_active is True).first()

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 10) -> Any:
        if limit == -1:
            data = db.query(self.model).filter(self.model.is_active == True).all()
        else:
            data = db.query(self.model).filter(self.model.is_active == True).offset(skip).limit(limit).all()
        return {
            "data": data,
            "total": self.get_multi_count(db)
        }

    def get_multi_count(self, db: Session) -> int:
        return db.query(func.count(self.model.id)).filter(self.model.is_active == True).scalar()

    def get_search_by_name_count(self, db: Session, *, name_like: str = "") -> int:
        return db.query(func.count(self.model.id)).filter(self.model.name.like('%{}%'.format(name_like))).scalar()

    def search_by_name(self, db: Session, skip: int = 0, limit: int = 10, name_like: str = "") -> PageSchemaType:
        if limit == -1:
            data = db.query(self.model).filter(self.model.name.like('%{}%'.format(name_like))).all()
        else:
            data = db.query(self.model).filter(self.model.like('%{}%'.format(name_like))).offset(skip).limit(
                limit).all()
        return self.page_model(data=data, total=self.get_search_by_name_count(db=db, name_like=name_like))

    # 获取所有对象，没有是否激活状态限制
    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update(db: Session, *, db_obj: ModelType, obj_in: UpdateSchemaType | Dict[str, Any]) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, model_id: int) -> ModelType:
        obj = db.query(self.model).get(model_id)
        db.delete(obj)
        db.commit()
        return obj