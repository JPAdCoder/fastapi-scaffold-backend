from sqlalchemy.orm import Session

from app.crud.crud_user import user
from app.schemas.user import UserCreate
from app.db.session import SessionLocal
from uuid import uuid1

def init_db(db: Session) -> None:
    # 创建超级用户
    super_user = UserCreate(
        name="admin",
        password="admin123",
        is_superuser=True,
        division_id="1",  # 默认部门ID
        role_id="1"      # 默认角色ID
    )
    
    # 检查用户是否已存在
    existing_user = user.get_by_name(db, name=super_user.name)
    if not existing_user:
        user.create(db, obj_in=super_user)
        print("Created superuser: admin")
    else:
        print("Superuser already exists")

def main() -> None:
    db = SessionLocal()
    init_db(db)
    db.close()

if __name__ == "__main__":
    main()
