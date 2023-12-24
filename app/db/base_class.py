# coding=utf8
"""
Time:   2022/2/9 9:38 AM
Author: AdCoder
Email:  17647309108@163.com
"""
from sqlalchemy.ext.declarative import as_declarative
from typing import Any


@as_declarative()
class Base:
    id: Any
    __name__: str
