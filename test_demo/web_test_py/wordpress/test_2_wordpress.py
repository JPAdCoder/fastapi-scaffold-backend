import pytest


def test_03(start, open_blog):
    print("测试用例test_03")
    assert 1


def test_04(start, open_blog):
    print("测试用例test_04")
    assert 1


def test_05(start, open_baidu):
    print("测试用例test_05")
    assert 1


if __name__ == '__main__':
    pytest.main(["-s", "test_2_wordpress.py"])

