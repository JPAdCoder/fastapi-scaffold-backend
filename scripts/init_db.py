import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from app.db.session import SessionLocal
from app.crud.crud_user import user
from app.schemas.user import UserCreate
from uuid import uuid1


def init_db() -> None:
    db = SessionLocal()
    try:
        # 创建超级管理员用户
        super_admin = UserCreate(
            name="admin",
            password="admin123",  # 请在创建后立即修改此密码
            role_id=uuid1().hex,  # 由于是初始用户，我们创建一个临时角色ID
            division_id=uuid1().hex,  # 临时部门ID
            is_superuser=True,
            is_active=True
        )

        # 检查是否已存在超级用户
        existing_user = db.query(user.model).filter(user.model.name == "admin").first()
        if not existing_user:
            user.create(db, obj_in=super_admin)
            print("Successfully created super admin user")
        else:
            print("Super admin user already exists")

    finally:
        db.close()


if __name__ == "__main__":
    print("Creating initial super admin user...")
    init_db()
    print("Initial setup completed")
