# coding=utf8
"""
Project :   generate-fastapi-be
Time:       2024/6/22 22:44
Author:     AdCoder
Email:      17647309108@163com

This module contains parameter definitions for various project configuration files
such as Dockerfile, .drone.yml, .gitignore, and version.txt.
"""
from app.schemas.base import FileBaseParam
from pydantic import BaseModel, Field


class DockerfileFileParam(FileBaseParam):
    """Parameters for generating Dockerfile"""
    base_image: str = Field(
        "python:3.9-slim",
        description="Base Docker image to use"
    )
    working_dir: str = Field(
        "/app",
        description="Working directory in container"
    )
    copy_files: str = Field(
        ".",
        description="Files to copy into container"
    )
    requirements_file: str = Field(
        "requirements.txt",
        description="Python requirements file"
    )
    expose_port: int = Field(
        8000,
        description="Port to expose"
    )
    command: str = Field(
        "uvicorn main:app --host 0.0.0.0 --port 8000",
        description="Command to run the application"
    )


class DroneYmlFileParam(FileBaseParam):
    """Parameters for generating .drone.yml file"""
    pass


class GitIgnoreFileParam(FileBaseParam):
    """Parameters for generating .gitignore file"""
    pass


class VersionTxtFileParam(FileBaseParam):
    """Parameters for generating version.txt file"""
    pass
