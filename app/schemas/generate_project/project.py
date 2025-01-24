# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/16 15:55
Author:     AdCoder
Email:      17647309108@163com
"""
from pydantic import BaseModel, Field
from app.schemas.generate_project.db import DBParam
from app.schemas.generate_project.crud import CRUDParam
from app.schemas.generate_project.core import CoreParam
from app.schemas.generate_project.models import ModelsParam
from app.schemas.generate_project.schemas import SchemasParam
from app.schemas.generate_project.api import ApiParam
from app.schemas.generate_project.utils import UtilsParam
from app.schemas.generate_project.config_files import (
    DroneYmlFileParam,
    GitIgnoreFileParam,
    DockerfileFileParam,
    VersionTxtFileParam
)
from app.schemas.base import FileBaseParam


class FormParam(FileBaseParam):
    name: str = Field(
        title="项目名称"
    )
    core_param: CoreParam = Field(
        title="core文件配置参数"
    )
    db_param: DBParam = Field(
        title="db模块配置参数"
    )
    crud_param: CRUDParam = Field(
        title="crud模块配置参数"
    )
    models_param: ModelsParam = Field(
        title="models模块配置参数"
    )
    schemas_param: SchemasParam = Field(
        title="schemas模块配置参数"
    )
    api_param: ApiParam = Field(
        title="api模块配置参数"
    )
    utils_param: UtilsParam = Field(
        title="utils模块配置参数"
    )
    drone_yml_file_param: DroneYmlFileParam = Field(
        title=".drone.yml文件配置参数"
    )
    gitignore_file_param: GitIgnoreFileParam = Field(
        title=".gitignore文件配置参数"
    )
    dockerfile_file_param: DockerfileFileParam = Field(
        title="Dockerfile文件配置参数"
    )
    version_txt_file_param: VersionTxtFileParam = Field(
        title="version.txt文件配置参数"
    )
