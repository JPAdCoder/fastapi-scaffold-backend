from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound


ModelType = TypeVar("ModelType")
model_obj = TypeVar("model_obj")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id and self.model.is_active == True).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> Any:
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

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update(db: Session, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: str) -> ModelType:
        obj = db.query(self.model).get(id)
        if not obj:
            raise NoResultFound(id, "不存在".format(str(ModelType)))
        db.delete(obj)
        db.commit()
        return obj

