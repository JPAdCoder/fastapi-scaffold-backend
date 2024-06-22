"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in core_param["config_file_param"]["merged_import_pkg_list"]:
% if v["from"] != "null":
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor


class Settings:
    API_V1_STR: str = "${core_param["api_config"]["api_v1_str"]}"
    OPENAPI_JSON_URL = "${core_param["api_config"]["openapi_json_url"]}"
    OPENAPI_DOC_URL = "${core_param["api_config"]["openapi_doc_url"]}"
    OPENAPI_REDOC_URL = "${core_param["api_config"]["openapi_redoc_url"]}"
    SERVER_HOST: str = "${core_param["api_config"]["server_host"]}"
    SERVER_PORT: int = ${core_param["api_config"]["server_port"]}
    SECRET_KEY: str = "${core_param["api_config"]["secret_key"]}"
    PROJECT_NAME: str = "${core_param["api_config"]["project_name"]}"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = ${core_param["api_config"]["access_token_expire_minutes"]}

    BACKEND_CORS_ORIGINS: List[str] = ${core_param["api_config"]["backend_cors_origins"]}

    # POSTGRESQL
    POSTGRES_SERVER: str = "${core_param["database_config"]["database_host"]}"
    POSTGRES_PORT: int = ${core_param["database_config"]["database_port"]}
    POSTGRES_USER: str = "${core_param["database_config"]["database_user"]}"
    POSTGRES_PASSWORD: str = "${core_param["database_config"]["database_password"]}"
    POSTGRES_DB: str = "${core_param["database_config"]["database_db"]}"
    SQLALCHEMY_DATABASE_URL: str = "${core_param["database_config"]["sqlalchemy_database_url"]}"
    MINIO_HOST: str = "${core_param["minio_config"]["minio_host"]}"
    MINIO_PORT: int = ${core_param["minio_config"]["minio_port"]}
    MINIO_BUCKET: str = "${core_param["minio_config"]["minio_bucket"]}"

    APP_PATH = "${core_param["general_config"]["app_path"]}"
    STATICS_FILE_DIRECTORY: str = "${core_param["general_config"]["statics_file_directory"]}"


settings = Settings()
