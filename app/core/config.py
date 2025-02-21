from typing import List, ClassVar
import secrets
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()


class Settings(BaseSettings):
    # API 配置
    API_V1_STR: str = os.getenv("API_V1_STR", "/generate/api/v1")

    # OpenAPI 文档配置
    OPENAPI_JSON_URL: str = os.getenv("OPENAPI_JSON_URL", "/openapi.json")
    OPENAPI_DOC_URL: str = os.getenv("OPENAPI_DOC_URL", "/docs")
    OPENAPI_REDOC_URL: str = os.getenv("OPENAPI_REDOC_URL", "/redoc")

    # 服务器配置
    SERVER_HOST: str = os.getenv("SERVER_HOST", "127.0.0.1")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8000"))

    # 安全配置
    SECRET_KEY: str = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # 项目配置
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FastAPI Code Generator")

    # CORS 配置
    BACKEND_CORS_ORIGINS: List[str] = eval(os.getenv("BACKEND_CORS_ORIGINS", '["http://localhost:3000"]'))

    # 数据库配置
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "fastapi_generator")
    SQLALCHEMY_DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    # MinIO 配置
    MINIO_HOST: str = os.getenv("MINIO_HOST", "localhost")
    MINIO_PORT: int = int(os.getenv("MINIO_PORT", "9000"))
    MINIO_BUCKET: str = os.getenv("MINIO_BUCKET", "fastapi-generate")

    # 测试配置
    TEST_USER_PASSWORD: str = os.getenv("TEST_USER_PASSWORD", "test-password-123")
    TEST_USER_NAME: str = os.getenv("TEST_USER_NAME", "test.user")
    TEST_ROLE_ID: str = os.getenv("TEST_ROLE_ID", "test-role-id")
    TEST_DIVISION_ID: str = os.getenv("TEST_DIVISION_ID", "test-division-id")

    # 静态文件配置
    APP_PATH: ClassVar[str] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATICS_FILE_DIRECTORY: ClassVar[str] = os.path.join(APP_PATH, "statics")

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
