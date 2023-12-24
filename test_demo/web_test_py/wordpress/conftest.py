import pytest


@pytest.fixture(scope="function")
def open_blog():
    print("打开wordpress页面_function")
