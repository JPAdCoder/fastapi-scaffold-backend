from typing import List
import secrets


class Settings:
    API_V1_STR: str = "/generate/api/v1"
    OPENAPI_JSON_URL = "/generate/api/v1/openapi.json"
    OPENAPI_DOC_URL = "/generate/api/v1/docs"
    OPENAPI_REDOC_URL = "/generate/api/v1/redoc"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 80
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = "FastAPI通用接口生成接口文档"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    BACKEND_CORS_ORIGINS: List[str] = ['*']

    # POSTGRESQL
    POSTGRES_SERVER: str = "192.168.31.29"
    POSTGRES_PORT: int = 54334
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "96241158a0"
    POSTGRES_DB: str = "fastapi-generate"
    # postgresql://scott:tiger@localhost:5432/database
    SQLALCHEMY_DATABASE_URL: str = "postgresql://{}:{}@{}:{}/{}".format(
        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER,
        POSTGRES_PORT, POSTGRES_DB
    )
    MINIO_HOST: str = "192.168.31.29"
    MINIO_PORT: int = 4000
    MINIO_BUCKET: str = "fastapi-generate"

    APP_PATH = "/Users/adcoder/PycharmProjects/generate-fastapi-be/app"
    STATICS_FILE_DIRECTORY: str = "{}\\statics".format(APP_PATH)


settings = Settings()
